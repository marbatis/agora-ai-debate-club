
from __future__ import annotations

import os
from typing import Dict, List

import httpx
from dotenv import load_dotenv
from loguru import logger

load_dotenv()

FactCheckResult = Dict[str, str]


class FactChecker:
    """Thin wrapper around Google Custom Search for citations."""

    SEARCH_URL = "https://www.googleapis.com/customsearch/v1"

    def __init__(self) -> None:
        self.api_key = os.getenv("FACTCHECK_SEARCH_API_KEY")
        self.engine_id = os.getenv("FACTCHECK_SEARCH_ENGINE_ID")
        if not self.api_key or not self.engine_id:
            logger.warning(
                "FACTCHECK_SEARCH_API_KEY/ENGINE_ID not configured; fact-checking disabled."
            )

    def search(self, query: str, *, max_results: int = 3) -> List[FactCheckResult]:
        """Perform a lightweight search and return [{title, link, snippet}]."""
        if not self.api_key or not self.engine_id:
            return []
        params = {
            "key": self.api_key,
            "cx": self.engine_id,
            "q": query,
            "num": max_results,
        }
        try:
            with httpx.Client(timeout=10.0) as client:
                response = client.get(self.SEARCH_URL, params=params)
                response.raise_for_status()
                data = response.json()
        except httpx.HTTPError as exc:
            logger.warning("Fact-check HTTP error: {}", exc)
            return []
        except Exception as exc:  # pragma: no cover
            logger.exception("Unexpected fact-check error: {}", exc)
            return []

        hits = data.get("items", []) or []
        results: List[FactCheckResult] = []
        for item in hits:
            results.append(
                {
                    "title": item.get("title", "Reference"),
                    "link": item.get("link", ""),
                    "snippet": item.get("snippet", ""),
                }
            )
        return results
