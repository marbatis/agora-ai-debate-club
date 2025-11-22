from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional

from dotenv import load_dotenv
from loguru import logger

try:
    import google.generativeai as genai
except ImportError:  # pragma: no cover - handled via mock mode
    genai = None


load_dotenv()


@dataclass
class GeminiLLM:
    """Lightweight wrapper around Gemini for reuse across agents."""

    model_name: Optional[str] = None
    temperature: float = 0.6

    def __post_init__(self) -> None:
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model_name = self.model_name or os.getenv("GEMINI_MODEL", "gemini-1.5-flash")
        self._mock_mode = not self.api_key or genai is None
        if self._mock_mode:
            logger.warning(
                "GEMINI_API_KEY not set or google-generativeai missing; running in mock mode."
            )
        else:  # pragma: no cover - requires actual API access
            genai.configure(api_key=self.api_key)

    @property
    def mock_mode(self) -> bool:
        return self._mock_mode

    def generate(
        self,
        system_prompt: str,
        user_prompt: str,
        *,
        temperature: Optional[float] = None,
    ) -> str:
        """Generate text using Gemini or return a deterministic stub in mock mode."""
        if self._mock_mode:
            return self._mock_response(system_prompt, user_prompt)

        model = genai.GenerativeModel(
            model_name=self.model_name,
            system_instruction=system_prompt,
        )
        try:  # pragma: no cover - network interaction
            response = model.generate_content(
                user_prompt,
                generation_config={"temperature": temperature or self.temperature},
            )
            text = getattr(response, "text", "") or ""
            return text.strip()
        except Exception as exc:  # pragma: no cover
            logger.exception("Gemini generation failed: {}", exc)
            return ""

    def _mock_response(self, system_prompt: str, user_prompt: str) -> str:
        excerpt = user_prompt.replace("\n", " ")[:200]
        return f"[MOCK:{self.model_name}] {excerpt}"
