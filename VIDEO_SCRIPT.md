# AGORA AI Debate Club - 3-Minute Video Script

**Total Time: ~180 seconds**

---

## [0:00-0:30] Opening & Problem Statement (30 seconds)

**[Screen: Title slide with project name]**

> Hi! I'm presenting AGORA AI Debate Club, built for the Kaggle AI Agents Intensive.
>
> **The problem?** Evaluating AI arguments is incredibly difficult. How do you know if an AI's reasoning is sound? How do you test different prompting strategies? And most importantly—how do you build AI systems that can engage in nuanced, structured reasoning?
>
> AGORA solves this by creating **adversarial multi-agent debates** where AI agents argue opposing sides, and an LLM judge evaluates them using an objective rubric.

**[Transition to architecture]**

---

## [0:30-1:00] Why Multi-Agent? The Value Proposition (30 seconds)

**[Screen: Simple diagram showing traditional vs multi-agent approach]**

> Why use multiple agents instead of one?
>
> **Three key benefits:**
>
> 1. **Better reasoning through adversarial testing** - Just like human debates, opposing arguments expose weak logic and force deeper thinking
>
> 2. **Objective evaluation** - The judge agent uses a standardized rubric (logic, factuality, persuasion) to score both sides independently
>
> 3. **Extensibility** - This architecture works for any debate topic, integrates fact-checking tools, and can be embedded in larger workflows
>
> This isn't just AI talking to itself—it's a **structured reasoning system**.

**[Transition to architecture details]**

---

## [1:00-2:00] Architecture Deep Dive (60 seconds)

**[Screen: Architecture diagram with annotations]**

> Let me show you how it works:
>
> **The flow has four main components:**
>
> **1. Debate Manager** (the orchestrator)
> - Takes a debate topic as input
> - Assigns positions (Pro vs Con) to two debater agents
> - Runs 1-3 rounds of back-and-forth arguments
> - Collects judge scores after each round
>
> **2. Debater Agents** (A and B)
> - Each uses Google Gemini 2.5 Flash as their LLM
> - Agent A argues PRO, Agent B argues CON
> - They generate opening arguments, then rebuttals based on opponent's last argument
> - They have access to a fact-checking tool via Model Context Protocol
>
> **3. The Judge Agent**
> - Also powered by Gemini 2.5 Flash
> - Scores each argument on three dimensions: Logic (0-10), Factual Accuracy (0-10), and Persuasive Power (0-10)
> - Returns structured JSON with scores and reasoning
> - We enhanced the JSON parser to handle markdown-wrapped responses
>
> **4. Tools Integration**
> - Debaters can call a fact-checking tool to verify claims
> - Built using Model Context Protocol (MCP) for standardized tool interfaces
> - This demonstrates how agents can augment reasoning with external data
>
> **Key technical details:**
> - FastAPI backend with CORS for browser access
> - Loguru for observability and structured logging
> - Pydantic for type-safe data validation
> - Built-in session memory tracks the debate history across rounds

**[Transition to live demo]**

---

## [2:00-2:45] Live Demo (45 seconds)

**[Screen: Browser showing demo_client.html]**

> Here's the web interface in action.
>
> **[Type topic]** Let's debate: "Should schools require coding classes?"
>
> **[Click "Start Debate"]** 
>
> The system is now:
> - Generating opening arguments from both sides
> - Running rebuttals where each agent responds to their opponent
> - Having the judge score each round
>
> **[Results appear]**
>
> And here are the results!
> - Agent B (arguing CON) won with a score of 7.60
> - Agent A (arguing PRO) scored 7.20
> - You can see the full transcript with each argument
> - The rubric breakdown shows: Logic, Factuality, and Persuasion scores
> - Each judge decision includes reasoning for the scores
>
> The whole debate took about 2 minutes with Gemini's fast responses.

**[Transition to closing]**

---

## [2:45-3:00] The Build & Next Steps (15 seconds)

**[Screen: Code snippets or project stats]**

> **What I learned building this:**
> - Multi-agent coordination is powerful but requires careful prompt engineering
> - LLM-as-judge works well when you provide explicit rubrics and JSON schemas
> - The Model Context Protocol makes tool integration clean and standardized
>
> **Next steps:**
> - Add more sophisticated tools (web search, knowledge graphs)
> - Implement persistent storage for debate history
> - Build a tournament mode where multiple agents compete
>
> Check out the full code on GitHub - link in the description. Thanks!

**[End screen: GitHub URL + "Built for Kaggle AI Agents Intensive"]**

---

## Recording Tips

### Timing Checkpoints:
- **0:30** - Should be done with problem statement
- **1:00** - Should be done with "why multi-agent"
- **2:00** - Should be done with architecture
- **2:45** - Should be done with demo
- **3:00** - DONE

### Pacing Strategy:
- Speak at **~150 words per minute** (normal conversational pace)
- Total script is ~450 words = 3 minutes
- **Practice 2-3 times** to hit timing naturally
- Speed up slightly during architecture (most dense section)
- Slow down for key phrases like "adversarial multi-agent debates" and "structured reasoning system"

### Screen Recording Plan:

1. **[0:00-0:30]** - Title slide with project name, then simple problem/solution visual
2. **[0:30-1:00]** - Comparison diagram: "Traditional AI" vs "Multi-Agent System"
3. **[1:00-2:00]** - Architecture diagram (can use the one from assets/screenshots/architecture-diagram.png once created)
4. **[2:00-2:45]** - Screen recording of demo_client.html with pre-recorded debate or live (risky if slow)
5. **[2:45-3:00]** - Code snippets or GitHub repo, then end screen

### Visual Assets Needed:
- Title slide
- Problem/solution comparison
- Architecture diagram (create in Excalidraw or Draw.io)
- Pre-recorded debate results (screenshot or video)
- End screen with GitHub URL

### Recording Tools:
- **Screen recording**: macOS QuickTime Player (Cmd+Shift+5) or Loom
- **Video editing**: iMovie (Mac), DaVinci Resolve (free), or CapCut
- **Slides**: Canva (free templates), Google Slides, or Keynote

### Pro Tips:
- ✅ Record in a quiet room with good lighting
- ✅ Use a decent microphone (even AirPods are better than laptop mic)
- ✅ Record each section separately, then edit together (easier to fix mistakes)
- ✅ Add captions/subtitles for accessibility (YouTube auto-generates these)
- ✅ Keep mouse movements smooth and purposeful during screen shares
- ✅ **For the demo**: Either pre-record a debate or use a canned response to avoid API delays

### Kaggle Upload:
- Max file size: **100 MB**
- Recommended format: **MP4** (H.264 codec)
- Recommended resolution: **1080p** (1920x1080) or **720p** (1280x720)
- Upload to: Kaggle submission form or YouTube (unlisted) and link it

---

## Quick Rehearsal Checklist

Before recording:
- [ ] Server running on localhost:8000
- [ ] demo_client.html tested and working
- [ ] All slides/visuals created
- [ ] Architecture diagram ready
- [ ] Script practiced 2-3 times
- [ ] Recording software tested
- [ ] Microphone tested
- [ ] Quiet environment confirmed

---

**Good luck! This project demonstrates all 5 required features beautifully—your demo will be impressive! 🎥**
