
# Kaggle Writeup (≤1500 words)

## Title
AGORA — AI Debate Club

## Subtitle
An AI debate club where two agents argue both sides and a judge agent scores logic, facts, and persuasion.

## Track
Freestyle

## Problem
Online debates often lack structure, evidence, and a clear way to judge competing claims. AGORA aims to demonstrate a transparent, agent‑driven debate where arguments are turn‑based, evidence‑backed, and scored.

## Why Agents
We model a debate as a collaboration between specialized roles: two **debater agents** (opposing stances) and a **judge agent** (LLM‑as‑judge). This multi‑agent setup enables turn‑taking, targeted critiques, and rubric‑based scoring that a single‑agent chatbot doesn’t enforce well.

## Architecture
- **Agents:** Debater A, Debater B, Judge
- **Pattern:** Sequential rounds with optional rebuttal loop
- **Tools:** Optional fact‑check tool (web search/OpenAPI), citation extractor
- **Memory:** Round transcript + a simple claim index per side
- **Observability:** Logs capture each claim, evidence/citations, and per‑round scores
- **Evaluation:** Judge rubric (logic, factuality, persuasion); final verdict with rationale

## Implementation Highlights
- Clean interfaces for `propose_argument()`, `rebut()`, and `score_round()`
- Optional tool wrapper for fact‑checking to support citations
- Minimal state store for transcripts and claim indexing
- FastAPI demo route for running a short debate and returning structured results

## Results
- Example debates show coherent turn‑taking and judge rationales that cite specific claims and evidence.
- With fact‑checking enabled, the system surfaces citations and penalizes unsupported assertions.

## Limitations & Next Steps
- Factual verification is only as strong as the tool integration and prompt design; deeper retrieval may be required.
- Future: richer rubrics (fallacy detection), persona styles, and A2A protocol for explicit agent messaging.

## Links
- GitHub repo: <URL to your public repo>
- (Optional) Kaggle notebook: <URL>
- (Optional) Video: <URL>
