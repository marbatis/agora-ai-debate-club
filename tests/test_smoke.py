
from pathlib import Path
import sys

from fastapi.testclient import TestClient

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.services.app import app


client = TestClient(app)


def test_debate_endpoint_returns_rounds():
    response = client.post("/debate", json={"topic": "Should AI moderate debates?", "rounds": 1})
    assert response.status_code == 200
    body = response.json()
    assert body["topic"]
    assert body["rounds"]
    assert body["final_scores"]["totals"]["A"] >= 0


def test_health_endpoint_reports_status():
    response = client.get("/healthz")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_adk_endpoint_disabled_without_flag():
    response = client.post("/adk/run", json={"prompt": "Host a quick debate"})
    assert response.status_code == 503
