
from typing import Dict, Optional


DEFAULT_RUBRIC = {
    "logic": 0.4,
    "factuality": 0.4,
    "persuasion": 0.2,
}


def aggregate(scores: dict) -> float:
    # scores: e.g., {'logic': 0.8, 'factuality': 0.7, 'persuasion': 0.6}
    return sum(scores.values()) / max(len(scores), 1)


def describe(rubric: Optional[Dict[str, float]] = None) -> str:
    """Return a human-readable summary of the rubric weights."""
    rubric = rubric or DEFAULT_RUBRIC
    parts = [f"{metric}:{weight}" for metric, weight in rubric.items()]
    return ", ".join(parts)
