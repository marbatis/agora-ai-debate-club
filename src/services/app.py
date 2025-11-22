
from __future__ import annotations

import os

from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from loguru import logger
from pydantic import BaseModel, Field

from src.agents.debaters import DebaterA, DebaterB
from src.agents.judge import Judge
from src.services.debate import DebateManager
from src.services.runtime import GeminiLLM
from src.tools.factcheck import FactChecker

app = FastAPI(title="AGORA — AI Debate Club")

# Enable CORS for browser access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for local development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

llm_client = GeminiLLM()
fact_checker = FactChecker()
debater_a = DebaterA(name="Debater Alice", stance="pro", llm=llm_client, fact_checker=fact_checker)
debater_b = DebaterB(name="Debater Blake", stance="con", llm=llm_client, fact_checker=fact_checker)
judge = Judge(llm=llm_client)
manager = DebateManager(debater_a=debater_a, debater_b=debater_b, judge=judge)

ENABLE_ADK = os.getenv("ENABLE_ADK_RUNTIME", "0") == "1"
adk_runtime = None
if ENABLE_ADK:
    try:
        from src.services.adk_runner import ADKDebateRuntime

        adk_runtime = ADKDebateRuntime(fact_checker=fact_checker)
        if not adk_runtime.available():
            logger.warning("ENABLE_ADK_RUNTIME=1 but ADK runtime is unavailable.")
    except Exception as exc:  # pragma: no cover
        logger.warning("Failed to initialize ADK runtime: {}", exc)
        adk_runtime = None


class DebateRequest(BaseModel):
    topic: str = Field(..., min_length=4, max_length=280)
    rounds: int = Field(1, ge=1, le=3)
    context: dict = Field(default_factory=dict, description="Optional session context/memory.")


class ADKRunRequest(BaseModel):
    prompt: str = Field(..., min_length=4, max_length=500)
    session_id: Optional[str] = Field(default=None, description="Reuse to maintain ADK session state.")


@app.get("/healthz")
def health():
    return {
        "status": "ok",
        "mock_llm": llm_client.mock_mode,
        "adk_runtime": bool(adk_runtime and adk_runtime.available()),
    }


@app.get("/demo")
def demo():
    logger.info("Running demo debate round")
    return manager.run(topic="Should cities ban private cars?", rounds=1)


@app.post("/debate")
def run_debate(payload: DebateRequest):
    try:
        result = manager.run(topic=payload.topic, rounds=payload.rounds, context=payload.context)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    return result


@app.post("/adk/run")
async def run_adk(payload: ADKRunRequest):
    if not adk_runtime or not adk_runtime.available():
        raise HTTPException(status_code=503, detail="ADK runtime disabled or not configured.")
    return await adk_runtime.run(prompt=payload.prompt, session_id=payload.session_id)
