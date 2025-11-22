
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from loguru import logger

from src.services.runtime import GeminiLLM
from src.tools.factcheck import FactChecker, FactCheckResult


Citation = Dict[str, str]


@dataclass
class Debater:
    """Debater agent powered by Gemini with optional fact-checking support."""

    name: str
    stance: str  # 'pro' or 'con'
    llm: GeminiLLM
    fact_checker: Optional[FactChecker] = None

    def propose_argument(self, topic: str, context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        context = context or {}
        citations = self._fetch_citations(topic, context)
        system_prompt = (
            f"You are {self.name}, debating the topic '{topic}'. "
            f"You are taking the {self.stance} stance. Use evidence-driven reasoning."
        )
        prompt = self._argument_prompt(topic, citations, context)
        logger.debug("{} generating argument for topic '{}'", self.name, topic)
        text = self.llm.generate(system_prompt, prompt)
        return {
            "agent": self.name,
            "stance": self.stance,
            "text": text,
            "citations": citations,
            "type": "argument",
        }

    def rebut(self, opponent_claim: Dict[str, Any], context: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        context = context or {}
        opponent_text = opponent_claim.get("text", "")
        system_prompt = (
            f"You are {self.name}, debating as the {self.stance} side. "
            "Write a concise rebuttal that addresses weaknesses and highlights logical flaws."
        )
        prompt = self._rebuttal_prompt(opponent_text, context)
        logger.debug("{} generating rebuttal", self.name)
        text = self.llm.generate(system_prompt, prompt, temperature=0.4)
        return {
            "agent": self.name,
            "stance": self.stance,
            "text": text,
            "type": "rebuttal",
        }

    def _fetch_citations(self, topic: str, context: Dict[str, Any]) -> List[Citation]:
        if not self.fact_checker:
            return []
        query = f"{topic} {self.stance} position evidence"
        history = context.get("history", [])
        if history:
            query = f"{topic} {self.stance} rebuttal evidence {len(history)}"
        results: List[FactCheckResult] = self.fact_checker.search(query)
        citations: List[Citation] = [
            {"id": str(idx + 1), "title": hit["title"], "url": hit["link"]}
            for idx, hit in enumerate(results[:3])
        ]
        return citations

    def _argument_prompt(self, topic: str, citations: List[Citation], context: Dict[str, Any]) -> str:
        citation_block = "\n".join(f"[{c['id']}] {c['title']} — {c['url']}" for c in citations) or "None"
        history_summary = self._summarize_history(context.get("history", []))
        return (
            f"Topic: {topic}\n"
            f"Stance: {self.stance}\n"
            f"Previous turns summary: {history_summary}\n"
            f"Suggested citations:\n{citation_block}\n\n"
            "Write a persuasive, evidence-backed argument (2 short paragraphs). "
            "Reference citations inline as [id] when useful and keep tone respectful."
        )

    def _rebuttal_prompt(self, opponent_text: str, context: Dict[str, Any]) -> str:
        history_summary = self._summarize_history(context.get("history", []))
        return (
            f"Opponent claim:\n{opponent_text}\n\n"
            f"Conversation summary: {history_summary}\n"
            "Write a rebuttal with 2-3 crisp counterpoints. "
            "Highlight logical gaps, missing evidence, or trade-offs."
        )

    @staticmethod
    def _summarize_history(history: List[Dict[str, Any]]) -> str:
        if not history:
            return "No prior turns."
        snippets = []
        for turn in history[-4:]:
            agent = turn.get("agent", "agent")
            role = turn.get("type", "argument")
            text = turn.get("text", "")
            snippets.append(f"{agent} ({role}): {text[:120]}...")
        return " | ".join(snippets)


class DebaterA(Debater):
    """Alias kept for clarity."""


class DebaterB(Debater):
    """Alias kept for clarity."""
