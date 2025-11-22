from __future__ import annotations

import os
from typing import Any, Dict, List, Optional

from loguru import logger

from src.tools.factcheck import FactChecker


class ADKDebateRuntime:
    """Multi-agent debate pipeline powered by Google ADK."""

    def __init__(
        self,
        fact_checker: FactChecker,
        *,
        app_name: str = "agora-adk",
        model_name: Optional[str] = None,
    ) -> None:
        self.fact_checker = fact_checker
        self.app_name = app_name
        self.model_name = model_name or os.getenv("ADK_MODEL") or os.getenv(
            "GEMINI_MODEL", "gemini-1.5-flash"
        )
        self._imports = self._load_dependencies()
        self.enabled = self._imports is not None
        self._app = self._build_app() if self.enabled else None

    def _load_dependencies(self):
        try:
            from google.adk.agents import LlmAgent, SequentialAgent
            from google.adk.apps.app import App
            from google.adk.models.google_llm import Gemini
            from google.adk.runners import InMemoryRunner
            from google.adk.tools import FunctionTool
            from google.genai import types
        except Exception as exc:  # pragma: no cover - only hit without ADK
            logger.warning("Google ADK unavailable: {}", exc)
            return None
        return {
            "LlmAgent": LlmAgent,
            "SequentialAgent": SequentialAgent,
            "App": App,
            "Gemini": Gemini,
            "InMemoryRunner": InMemoryRunner,
            "FunctionTool": FunctionTool,
            "types": types,
        }

    def available(self) -> bool:
        return self.enabled

    def _build_app(self):
        LlmAgent = self._imports["LlmAgent"]
        SequentialAgent = self._imports["SequentialAgent"]
        App = self._imports["App"]

        fact_tool = self._create_fact_tool()
        pro_agent = self._create_debater_agent(
            agent_cls=LlmAgent,
            name="debater_pro",
            stance="supporting",
            fact_tool=fact_tool,
        )
        con_agent = self._create_debater_agent(
            agent_cls=LlmAgent,
            name="debater_con",
            stance="opposing",
            fact_tool=fact_tool,
        )
        judge_agent = self._create_judge_agent(agent_cls=LlmAgent)

        pipeline = SequentialAgent(
            name="agora_pipeline",
            description="Runs PRO → CON → JUDGE for every debate topic.",
            sub_agents=[pro_agent, con_agent, judge_agent],
        )
        return App(name=self.app_name, root_agent=pipeline)

    def _create_model(self):
        Gemini = self._imports["Gemini"]
        types_mod = self._imports["types"]
        retry_config = types_mod.HttpRetryOptions(
            attempts=4,
            exp_base=2,
            initial_delay=1,
            http_status_codes=[429, 500, 503, 504],
        )
        return Gemini(model=self.model_name, retry_options=retry_config)

    def _create_fact_tool(self):
        fact_checker = self.fact_checker

        def fact_check(query: str) -> Dict[str, Any]:
            """Search for recent facts to cite in the debate."""
            results = fact_checker.search(query) if fact_checker else []
            payload = []
            for idx, hit in enumerate(results[:3]):
                payload.append(
                    {
                        "id": idx + 1,
                        "title": hit.get("title", "Reference"),
                        "url": hit.get("link", ""),
                        "snippet": hit.get("snippet", ""),
                    }
                )
            status = "ok" if payload else "empty"
            return {"status": status, "query": query, "results": payload}

        fact_check.__name__ = "fact_check"
        fact_check.__doc__ = "Look up recent citations for the debate topic."
        return self._imports["FunctionTool"](fact_check)

    def _create_debater_agent(
        self,
        agent_cls,
        *,
        name: str,
        stance: str,
        fact_tool,
    ):
        model = self._create_model()
        return agent_cls(
            name=name,
            model=model,
            description=f"Argues the {stance} view with citations.",
            instruction=(
                f"You are {name} arguing the {stance} view of the user's topic. "
                "When possible call `fact_check` to find high-quality references. "
                "Structure your response as:\n"
                "1. Short thesis sentence.\n"
                "2. Two supporting points with citations like [1], [2].\n"
                "3. Closing sentence summarizing your stance.\n"
                "Avoid hedging—take a clear position backed by evidence."
            ),
            tools=[fact_tool],
        )

    def _create_judge_agent(self, agent_cls):
        model = self._create_model()
        rubric = (
            "Score each side on logic, factuality, and persuasion (0-10). "
            "Return JSON with shape: "
            '{"rubric_scores": {"logic":{"A":x,"B":y,"notes":""}, ...}, '
            '"winner": "A|B|draw", "rationale": ""}. '
            "Use the debate transcript above as evidence."
        )
        return agent_cls(
            name="debate_judge",
            model=model,
            description="Scores both sides using the AGORA rubric.",
            instruction=(
                "You are the impartial AGORA judge. "
                "Read the full transcript from both debaters, then follow this rubric:\n"
                "• Logic: Are arguments coherent and structured?\n"
                "• Factuality: Are claims grounded in evidence/citations?\n"
                "• Persuasion: Does the tone/structure move the audience?\n"
                f"{rubric}\n"
                "Keep reasoning concise but specific."
            ),
        )

    async def run(
        self,
        prompt: str,
        *,
        session_id: Optional[str] = None,
        user_id: str = "adk-demo",
    ) -> Dict[str, Any]:
        """Executes the ADK debate app for a natural-language prompt."""
        if not self.enabled or not self._app:
            raise RuntimeError("ADK runtime not available")

        InMemoryRunner = self._imports["InMemoryRunner"]
        async with InMemoryRunner(app=self._app) as runner:
            events = await runner.run_debug(
                prompt,
                user_id=user_id,
                session_id=session_id or "adk-session",
                quiet=True,
                verbose=False,
            )
        return {
            "app": self.app_name,
            "prompt": prompt,
            "events": [self._serialize_event(event) for event in events],
        }

    def _serialize_event(self, event) -> Dict[str, Any]:
        """Convert ADK Event objects into API-safe dictionaries."""
        return {
            "id": getattr(event, "id", ""),
            "author": getattr(event, "author", ""),
            "timestamp": getattr(event, "timestamp", 0.0),
            "content": self._parts_to_list(getattr(event, "content", None)),
            "function_calls": self._function_calls(event),
            "function_responses": self._function_responses(event),
        }

    def _function_calls(self, event) -> List[Dict[str, Any]]:
        calls = []
        for call in getattr(event, "get_function_calls", lambda: [])() or []:
            args = getattr(call, "args", None) or {}
            if hasattr(args, "items"):
                args = dict(args)
            calls.append({"name": getattr(call, "name", ""), "args": args})
        return calls

    def _function_responses(self, event) -> List[Dict[str, Any]]:
        responses = []
        for response in getattr(event, "get_function_responses", lambda: [])() or []:
            payload = getattr(response, "response", None) or {}
            if hasattr(payload, "items"):
                payload = dict(payload)
            responses.append(
                {
                    "name": getattr(response, "name", ""),
                    "response": payload,
                }
            )
        return responses

    def _parts_to_list(self, content) -> List[str]:
        if not content or not getattr(content, "parts", None):
            return []
        texts = []
        for part in content.parts:
            if getattr(part, "text", None):
                texts.append(part.text)
            elif getattr(part, "function_call", None):
                texts.append(f"[function_call] {part.function_call.name}")
            elif getattr(part, "function_response", None):
                texts.append(f"[function_response] {part.function_response.name}")
        return texts
