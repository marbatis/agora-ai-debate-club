# 🎭 AGORA — AI Debate Club

> **An AI-powered multi-agent debate system where two agents argue opposing sides of any topic, with a judge agent scoring arguments based on logic, factuality, and persuasion.**

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115+-green.svg)](https://fastapi.tiangolo.com/)
[![Gemini](https://img.shields.io/badge/Powered%20by-Gemini%202.5-orange.svg)](https://ai.google.dev/)

**Track:** Freestyle | **Course:** 5-Day AI Agents Intensive with Google  
**Last Updated:** November 22, 2025

**🎥 [Watch the Demo Video](https://youtu.be/jfo-z-_Le2I)** - See AGORA in action!

---

## 📖 Table of Contents
- [Problem Statement](#-problem-statement)
- [Why Multi-Agent System?](#-why-multi-agent-system)
- [Features](#-features)
- [Architecture](#%EF%B8%8F-architecture)
- [Demo](#-demo)
- [Quick Start](#-quick-start)
- [Usage Examples](#-usage-examples)
- [API Documentation](#-api-documentation)
- [Project Structure](#-project-structure)
- [Testing](#-testing)

---

## 🎯 Problem Statement

**The Challenge:** Online debates are often chaotic, lacking structure, evidence, and fair judgment. Participants talk past each other, claims go unchecked, and there's no objective way to determine which arguments are stronger.

**The Solution:** AGORA creates a controlled, transparent debate environment where:
- Arguments are structured and turn-based
- Evidence is cited and fact-checked (optional)
- Scoring is objective and rubric-based
- All reasoning is visible and explainable

---

## 🤖 Why Multi-Agent System?

A single LLM can't effectively debate itself while maintaining distinct perspectives. Our multi-agent architecture solves this by:

1. **Debater A (Pro)** - Argues in favor of the proposition with dedicated context and strategy
2. **Debater B (Con)** - Argues against with independent reasoning and evidence
3. **Judge** - Provides impartial scoring based on a structured rubric

This separation enables:
- ✅ **Authentic opposing viewpoints** - Each agent maintains its stance
- ✅ **Turn-taking discipline** - Structured rounds prevent chaos
- ✅ **Transparent evaluation** - Judge explains scoring rationale
- ✅ **Evidence integration** - Agents can use tools for fact-checking

---

## ✨ Features

This project demonstrates **5+ key AI agent concepts** from the Google AI Agents Intensive:

### ✅ Required Features (3+ needed):
1. **Multi-Agent System** - Sequential agent pattern with specialized roles
2. **Tools Integration** - Optional fact-checking via Google Custom Search (MCP-compatible)
3. **Sessions & Memory** - Round transcripts, claim indexing, conversation history
4. **Observability** - Structured logging of arguments, citations, and scores
5. **Agent Evaluation** - LLM-as-judge with rubric scoring (logic, factuality, persuasion)

### 🎁 Bonus Features:
- ⚡ **FastAPI Server** with CORS support for web applications
- 🎨 **Beautiful Web Interface** for interactive debates
- 🧪 **Comprehensive Testing** with pytest
- 📊 **Structured JSON Responses** for easy integration

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                        User Input                                │
│                    (Debate Topic)                                │
└────────────────────────┬────────────────────────────────────────┘
                         │
                         ▼
               ┌─────────────────────┐
               │  Debate Manager     │
               │  (Orchestrator)     │
               └─────────┬───────────┘
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
    ┌─────────┐    ┌─────────┐   ┌──────────┐
    │Debater A│    │Debater B│   │  Judge   │
    │  (Pro)  │    │  (Con)  │   │(Evaluator)│
    └────┬────┘    └────┬────┘   └─────┬────┘
         │              │               │
         │    ┌─────────▼──────┐        │
         └───►│ Optional Tools │◄───────┘
              │ (Fact Check)   │
              └────────────────┘
```

### Component Breakdown:

- **Debate Manager** (`src/services/debate.py`)
  - Orchestrates multi-round debates
  - Manages turn-taking between agents
  - Aggregates scores and determines winner

- **Debater Agents** (`src/agents/debaters.py`)
  - Gemini 2.5-powered reasoning
  - Maintain stance-specific context
  - Optional fact-checking via Google Search
  - Citation management

- **Judge Agent** (`src/agents/judge.py`)
  - LLM-as-judge pattern
  - Structured rubric evaluation
  - JSON-formatted scoring with rationale

- **FastAPI Service** (`src/services/app.py`)
  - `/healthz` - Health check endpoint
  - `/demo` - Quick demo debate
  - `/debate` - Custom topic debates (1-3 rounds)

---

## 🎬 Demo

### Web Interface
![Web Interface](assets/screenshots/web-interface.png)
*Beautiful web interface for running interactive debates*

### Example Debate Output
```json
{
  "topic": "Should artificial intelligence be regulated?",
  "rounds": [
    {
      "round": 1,
      "A": {
        "argument": {
          "agent": "Debater Alice",
          "stance": "pro",
          "text": "Requiring regulation for AI is essential..."
        },
        "rebuttal": {
          "text": "My opponent overlooks..."
        }
      },
      "B": {
        "argument": {
          "agent": "Debater Blake",
          "stance": "con",
          "text": "Mandating regulation risks..."
        }
      },
      "judgement": {
        "rubric_scores": {
          "logic": {"A": 7.5, "B": 8.0},
          "factuality": {"A": 6.5, "B": 7.5},
          "persuasion": {"A": 8.0, "B": 7.0}
        },
        "winner": "B",
        "rationale": "Debater B presented stronger logical structure..."
      }
    }
  ],
  "final_scores": {
    "totals": {"A": 7.20, "B": 7.60},
    "winner": "B"
  }
}
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- Gemini API key ([Get one here](https://ai.google.dev/))
- (Optional) Google Custom Search API for fact-checking

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/marbatis/agora-ai-debate-club.git
cd agora-ai-debate-club
```

2. **Create virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment**
```bash
cp .env.example .env
# Edit .env and add your GEMINI_API_KEY
```

**.env file:**
```bash
GEMINI_API_KEY=your_api_key_here
GEMINI_MODEL=gemini-2.5-flash
ENABLE_ADK_RUNTIME=0
FACTCHECK_SEARCH_API_KEY=  # Optional
FACTCHECK_SEARCH_ENGINE_ID=  # Optional
```

5. **Run the server**
```bash
# Method 1: Direct Python
python -m uvicorn src.services.app:app --reload --port 8000

# Method 2: Using the full path
PYTHONPATH=$PWD .venv/bin/python -m uvicorn src.services.app:app --reload --port 8000
```

6. **Open the web interface**
```bash
# Open demo_client.html in your browser
open demo_client.html  # On Mac
# Or navigate to http://127.0.0.1:8000/docs for API docs
```

---

## 💡 Usage Examples

### Example 1: Using the Web Interface

1. Start the server (see Quick Start)
2. Open `demo_client.html` in your browser
3. Enter a debate topic: "Should social media have age restrictions?"
4. Select number of rounds (1-3)
5. Click "Start Debate"
6. Wait 30-90 seconds for results

### Example 2: Using the API with curl

```bash
# Quick demo
curl http://127.0.0.1:8000/demo

# Custom topic debate
curl -X POST http://127.0.0.1:8000/debate \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Is remote work better than office work?",
    "rounds": 2
  }'
```

### Example 3: Using Python

```python
import requests

# Run a debate
response = requests.post(
    "http://127.0.0.1:8000/debate",
    json={
        "topic": "Should voting be mandatory?",
        "rounds": 1
    }
)

data = response.json()
print(f"Winner: {data['final_scores']['winner']}")
print(f"Score A: {data['final_scores']['totals']['A']:.2f}")
print(f"Score B: {data['final_scores']['totals']['B']:.2f}")
```

### Example Topics to Try:
- "Should artificial intelligence be regulated?"
- "Is climate change the biggest threat to humanity?"
- "Should social media platforms be held liable for user content?"
- "Are electric cars the future of transportation?"
- "Should schools ban smartphones in classrooms?"

---

## 📚 API Documentation

### Endpoints

#### `GET /healthz`
Health check endpoint.

**Response:**
```json
{
  "status": "ok",
  "mock_llm": false,
  "adk_runtime": false
}
```

#### `GET /demo`
Run a demo debate on a default topic.

**Response:** Full debate JSON (see Example Debate Output above)

#### `POST /debate`
Run a custom debate.

**Request Body:**
```json
{
  "topic": "Your debate topic",
  "rounds": 1,  // 1-3
  "context": {}  // Optional session context
}
```

**Response:** Full debate JSON with rounds, arguments, rebuttals, and scores

---

## 📁 Project Structure

```
agora-ai-debate-club/
├── src/
│   ├── agents/
│   │   ├── debaters.py      # Debater A & B agents
│   │   └── judge.py          # Judge agent with rubric
│   ├── services/
│   │   ├── app.py            # FastAPI application
│   │   ├── debate.py         # Debate orchestration
│   │   ├── runtime.py        # Gemini LLM wrapper
│   │   └── adk_runner.py     # ADK integration (optional)
│   ├── tools/
│   │   └── factcheck.py      # Fact-checking tool (MCP)
│   └── evaluation/
│       └── rubric.py         # Scoring rubric
├── tests/
│   └── test_smoke.py         # Integration tests
├── assets/
│   └── screenshots/          # Demo screenshots
├── docs/
│   └── architecture.mmd      # Architecture diagrams
├── demo_client.html          # Web interface
├── requirements.txt          # Python dependencies
├── .env.example              # Environment template
├── .gitignore
└── README.md
```

---

## 🧪 Testing

Run the test suite:

```bash
# Run all tests
pytest tests/ -v

# Run with coverage
pytest tests/ --cov=src --cov-report=html

# Run specific test
pytest tests/test_smoke.py::test_debate_endpoint_returns_rounds -v
```

**Test Coverage:**
- ✅ Debate endpoint returns proper structure
- ✅ Health endpoint reports status
- ✅ ADK endpoint behavior
- ✅ All tests pass with mock mode (no API key needed for CI/CD)

---

## 🎓 Learning Outcomes

This project demonstrates key concepts from the **5-Day AI Agents Intensive Course**:

1. **Day 1 - Introduction to Agents**: Multi-agent architecture with specialized roles
2. **Day 2 - Agent Tools**: Custom fact-checking tool, MCP compatibility
3. **Day 3 - Sessions & Memory**: Conversation history, claim indexing
4. **Day 4 - Agent Quality**: Observability (logging), Evaluation (LLM-as-judge)
5. **Day 5 - Production**: FastAPI deployment, CORS, testing

---

## 🛠️ Technologies Used

- **Google Gemini 2.5 Flash** - LLM for agents
- **FastAPI** - Web framework
- **Pydantic** - Data validation
- **Python 3.9+** - Programming language
- **Pytest** - Testing framework
- **Google Custom Search API** - Optional fact-checking
- **Loguru** - Structured logging

---

## 🔐 Security Notes

- ⚠️ **Never commit your `.env` file** - API keys are sensitive
- 🔒 **`.env` is in `.gitignore`** by default
- 🛡️ **Use environment variables** for all secrets
- 📝 **Share `.env.example`** instead for documentation

---

## 🤝 Contributing

This is a capstone project for the Kaggle AI Agents Intensive. While direct contributions aren't expected, feedback and suggestions are welcome!

---

## 📄 License

MIT License - See LICENSE file for details

---

## 👨‍💻 Author

**Marcelo Silveira** ([@marbatis](https://github.com/marbatis))

Built for the **5-Day AI Agents Intensive Course with Google** - Freestyle Track

---

## 🙏 Acknowledgments

- Google AI Agents Intensive Course team
- Kaggle community
- Google Gemini team for the powerful LLM API

---

## 📞 Support

- 📧 Issues: [GitHub Issues](https://github.com/marbatis/agora-ai-debate-club/issues)
- 💬 Discussions: [Kaggle Discord](https://kaggle.com/discord)
- 📺 Video Demo: [Coming soon]

---

**⭐ If you find this project helpful, please star the repository!**
