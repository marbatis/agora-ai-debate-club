
from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, Optional

from loguru import logger

from src.evaluation.rubric import DEFAULT_RUBRIC
from src.services.runtime import GeminiLLM


Rubric = Dict[str, float]


@dataclass
class Judge:
    """LLM-as-judge that scores each round with the rubric."""

    llm: GeminiLLM
    rubric: Rubric = field(default_factory=lambda: DEFAULT_RUBRIC.copy())

    def score_round(
        self,
        a_claim: Dict[str, Any],
        b_claim: Dict[str, Any],
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        context = context or {}
        system_prompt = (
            "You are an impartial debate judge. Score each debater on logic, factuality, "
            "and persuasion using a 0-10 scale, then declare a winner."
        )
        prompt = self._assemble_prompt(a_claim, b_claim, context)
        response = self.llm.generate(system_prompt, prompt, temperature=0.2)
        result = self._parse_response(response)
        return result

    def _assemble_prompt(
        self,
        a_claim: Dict[str, Any],
        b_claim: Dict[str, Any],
        context: Dict[str, Any],
    ) -> str:
        rubric_text = ", ".join(f"{k}={v}" for k, v in self.rubric.items())
        history_summary = context.get("history_summary", "History provided in transcript.")
        return (
            "Topic: {topic}\n"
            "Debater A argument: {a_text}\n"
            "Debater B argument: {b_text}\n"
            "Debater A rebuttal: {a_rebuttal}\n"
            "Debater B rebuttal: {b_rebuttal}\n"
            "Transcript summary: {history}\n\n"
            "Rubric weights: {rubric}\n\n"
            "You MUST respond with ONLY a JSON object (no other text). "
            "Use this exact format:\n"
            '{{\n'
            '  "rubric_scores": {{\n'
            '    "logic": {{"A": 7.5, "B": 8.0, "notes": "explanation"}},\n'
            '    "factuality": {{"A": 6.0, "B": 7.5, "notes": "explanation"}},\n'
            '    "persuasion": {{"A": 8.0, "B": 6.5, "notes": "explanation"}}\n'
            '  }},\n'
            '  "winner": "A",\n'
            '  "rationale": "brief explanation"\n'
            '}}\n'
        ).format(
            topic=context.get("topic", "N/A"),
            a_text=a_claim.get("argument", {}).get("text") or a_claim.get("text", ""),
            b_text=b_claim.get("argument", {}).get("text") or b_claim.get("text", ""),
            a_rebuttal=a_claim.get("rebuttal", {}).get("text", ""),
            b_rebuttal=b_claim.get("rebuttal", {}).get("text", ""),
            history=history_summary,
            rubric=rubric_text,
        )

    def _parse_response(self, raw: str) -> Dict[str, Any]:
        data = self._safe_json(raw)
        rubric_scores = data.get("rubric_scores") or self._blank_rubric_scores()
        overall = self._aggregate_scores(rubric_scores)
        winner = data.get("winner") or self._determine_winner(overall)
        rationale = data.get("rationale") or "See rubric notes."
        return {
            "rubric_scores": rubric_scores,
            "scores": overall,
            "winner": winner,
            "rationale": rationale,
        }

    def _aggregate_scores(self, rubric_scores: Dict[str, Any]) -> Dict[str, float]:
        totals = {"A": 0.0, "B": 0.0}
        for metric, weight in self.rubric.items():
            metric_scores = rubric_scores.get(metric, {})
            totals["A"] += float(metric_scores.get("A", 0.0)) * weight
            totals["B"] += float(metric_scores.get("B", 0.0)) * weight
        return totals

    def _determine_winner(self, totals: Dict[str, float]) -> str:
        if totals["A"] > totals["B"]:
            return "A"
        if totals["B"] > totals["A"]:
            return "B"
        return "draw"

    def _blank_rubric_scores(self) -> Dict[str, Dict[str, float]]:
        return {
            metric: {"A": 0.0, "B": 0.0, "notes": "LLM not configured - placeholder."}
            for metric in self.rubric
        }

    def _safe_json(self, raw: str) -> Dict[str, Any]:
        if not raw:
            return {}
        candidate = raw.strip()
        
        # Handle markdown code blocks
        if "```json" in candidate:
            start = candidate.find("```json") + 7
            end = candidate.find("```", start)
            if end != -1:
                candidate = candidate[start:end].strip()
        elif "```" in candidate:
            start = candidate.find("```") + 3
            end = candidate.find("```", start)
            if end != -1:
                candidate = candidate[start:end].strip()
        
        # Extract JSON object
        if not candidate.startswith("{"):
            start = candidate.find("{")
            end = candidate.rfind("}")
            if start != -1 and end != -1:
                candidate = candidate[start : end + 1]
        
        try:
            return json.loads(candidate)
        except json.JSONDecodeError as e:
            logger.warning(f"Judge returned non-JSON response: {e}. Raw response: {raw[:200]}")
            return {}
