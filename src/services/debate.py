from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Dict, List, Optional

from loguru import logger

from src.agents.debaters import Debater
from src.agents.judge import Judge


@dataclass
class DebateManager:
    """Coordinates turns between two debaters and the judge."""

    debater_a: Debater
    debater_b: Debater
    judge: Judge

    def run(
        self,
        topic: str,
        *,
        rounds: int = 1,
        context: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        if not topic or not topic.strip():
            raise ValueError("Topic is required.")
        if rounds < 1:
            raise ValueError("At least one round is required.")

        context = context or {}
        transcript: List[Dict[str, Any]] = context.get("history", []).copy()
        round_results: List[Dict[str, Any]] = []

        for round_idx in range(1, rounds + 1):
            logger.info("Starting debate round {}", round_idx)
            round_context = {"history": transcript, "round": round_idx}
            a_argument = self.debater_a.propose_argument(topic, round_context)
            b_argument = self.debater_b.propose_argument(topic, round_context)
            a_rebuttal = self.debater_a.rebut(b_argument, round_context)
            b_rebuttal = self.debater_b.rebut(a_argument, round_context)

            transcript.extend([a_argument, b_argument, a_rebuttal, b_rebuttal])

            judge_context = {
                "history_summary": self._summarize_transcript(transcript),
                "topic": topic,
            }
            judgement = self.judge.score_round(
                {"argument": a_argument, "rebuttal": a_rebuttal},
                {"argument": b_argument, "rebuttal": b_rebuttal},
                judge_context,
            )

            round_results.append(
                {
                    "round": round_idx,
                    "A": {"argument": a_argument, "rebuttal": a_rebuttal},
                    "B": {"argument": b_argument, "rebuttal": b_rebuttal},
                    "judgement": judgement,
                }
            )

        final_scores = self._aggregate_series(round_results)
        return {
            "topic": topic,
            "rounds": round_results,
            "final_scores": final_scores,
            "transcript": transcript,
        }

    def _summarize_transcript(self, transcript: List[Dict[str, Any]]) -> str:
        if not transcript:
            return "No turns yet."
        snippets = []
        for entry in transcript[-6:]:
            snippets.append(f"{entry.get('agent', 'agent')}:{entry.get('text', '')[:80]}...")
        return " | ".join(snippets)

    def _aggregate_series(self, results: List[Dict[str, Any]]) -> Dict[str, Any]:
        totals = {"A": 0.0, "B": 0.0}
        per_round = []
        for result in results:
            scores = result["judgement"]["scores"]
            totals["A"] += scores.get("A", 0.0)
            totals["B"] += scores.get("B", 0.0)
            per_round.append(scores)
        winner = "draw"
        if totals["A"] > totals["B"]:
            winner = "A"
        elif totals["B"] > totals["A"]:
            winner = "B"
        return {"totals": totals, "winner": winner, "per_round": per_round}
