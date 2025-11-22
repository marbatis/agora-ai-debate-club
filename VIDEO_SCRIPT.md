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

### Keynote Presentation Plan:

Create a single Keynote presentation with these slides:

1. **Slide 1 - Title** [0:00-0:10]
   - Title: "AGORA AI Debate Club"
   - Subtitle: "Multi-Agent Debates with LLM-as-Judge"
   - Your name + "Kaggle AI Agents Intensive"

2. **Slide 2 - The Problem** [0:10-0:30]
   - Headline: "The Challenge"
   - 3 bullet points: Testing AI reasoning, Comparing strategies, Building structured thinking
   - Visual: Icon of confused person looking at AI output

3. **Slide 3 - Why Multi-Agent?** [0:30-1:00]
   - Headline: "Traditional AI vs Multi-Agent Debates"
   - Two columns comparing:
     - Left: "Single AI" → One perspective, Hard to validate, Confirmation bias
     - Right: "Multi-Agent" → Adversarial testing, Objective judging, Better reasoning
   - Use Keynote's "Basic" or "Bold" theme for clean comparison

4. **Slide 4 - Architecture** [1:00-2:00]
   - Use Keynote's shapes to create flow diagram:
     - Rectangle: "User Input (Topic)"
     - Arrow down
     - Rectangle: "Debate Manager"
     - Arrows splitting to two rectangles: "Debater A (PRO)" and "Debater B (CON)"
     - Both arrows pointing to: "Judge Agent"
     - Arrow to: "Scores & Winner"
   - Add text boxes for: "Gemini 2.5 Flash", "MCP Tools", "Structured Logging"

5. **Slide 5 - Live Demo Title** [2:00-2:05]
   - Simple text: "Live Demo"
   - Then transition to **screen recording** of browser

6. **[Screen Recording]** [2:05-2:45]
   - **Switch from Keynote to browser** showing demo_client.html
   - Show the debate running (pre-record this or use live)
   - Show results with scores

7. **Slide 6 - What I Learned** [2:45-2:55]
   - 3 bullet points:
     - Multi-agent coordination needs careful prompts
     - LLM-as-judge works with explicit rubrics
     - MCP makes tool integration standardized
   - Keep it minimal and punchy

8. **Slide 7 - End Screen** [2:55-3:00]
   - "Check it out on GitHub"
   - Large text with URL: github.com/marbatis/agora-ai-debate-club
   - "Built for Kaggle AI Agents Intensive"

### Keynote Tips for Mac:

**Setup:**
- Open Keynote → "New Document" → Choose "White" or "Basic" theme (clean, professional)
- Set slide size: Keynote Preferences → "Widescreen (16:9)" for better video format
- Use consistent fonts: SF Pro Display (macOS native) or Helvetica

**Design Guidelines:**
- **Keep it minimal** - Max 3 bullet points per slide
- **Use Keynote's built-in shapes** for the architecture diagram (Insert → Shape → Flowchart)
- **Consistent colors** - Use blue (#007AFF) for agents, green (#34C759) for success/judge
- **Animations** - Use "Dissolve" or "Move In" transitions (subtle, not distracting)

**Creating the Architecture Diagram in Keynote:**
1. Insert → Shape → Rectangle (for components)
2. Insert → Line → Connection Line (for arrows)
3. Text Box for labels
4. Group related shapes (select all → right-click → Group)
5. Align using Keynote's alignment guides (they appear automatically)

### Recording Workflow:

**Step 1: Create Keynote Presentation**
- Build all 8 slides as described above
- Practice advancing slides manually (not auto-advance)
- Export architecture diagram: Select slide 4 → File → Export To → Images → PNG (save to `assets/screenshots/architecture-diagram.png`)

**Step 2: Record with Keynote's Built-in Feature**
- Keynote → Play → Record Slideshow (Cmd+Option+R)
- This records your voiceover + slide advances
- Speak clearly and advance slides at the timestamps above
- Stop recording after Slide 5

**Step 3: Record Browser Demo Separately**
- Use macOS Screenshot tool (Cmd+Shift+5) → "Record Selected Portion"
- Select just the browser window
- Record the debate demo (2:05-2:45 section)
- Save as `demo-recording.mov`

**Step 4: Edit Together in iMovie**
1. Open iMovie → Create New Movie
2. Import Keynote recording (File → Export To → Movie → 1080p)
3. Import browser demo recording
4. Drag Keynote recording to timeline
5. Split at 2:00 mark (where you transition to demo)
6. Insert browser recording
7. Add final Keynote slides (6-7) after browser demo
8. Add background music if desired (subtle, low volume)
9. Export: File → Share → File → 1080p (H.264)

**Alternative: Record Everything in One Take**
- Start Keynote in full screen (Play → Play Slideshow)
- Use Cmd+Shift+5 → Record Entire Screen
- Advance through Keynote slides while speaking
- When you reach Slide 5, Cmd+Tab to switch to browser
- Show demo
- Cmd+Tab back to Keynote for final slides
- Stop recording
- This creates one video file (easier but riskier if you make mistakes)

### Export Settings:
- **Format**: MP4 (H.264)
- **Resolution**: 1080p (1920×1080)
- **Frame rate**: 30fps
- **File size**: Keep under 100MB for Kaggle upload
- **Audio**: AAC codec, 128kbps

### Pro Tips:

- ✅ **Keynote makes this easy** - Built-in recording, no external tools needed
- ✅ Record each section separately in Keynote, then stitch in iMovie (easier to fix mistakes)
- ✅ Use **SF Pro Display** font (native macOS font, looks professional)
- ✅ **Pre-record the browser demo** - Don't risk API delays during final recording
- ✅ Keep mouse movements smooth during screen shares
- ✅ Test audio levels: Keynote → Preferences → Slideshow → Check "Record audio"
- ✅ Use **Cmd+Option+R** in Keynote to start recording immediately
- ✅ Add subtle background music from iMovie's library (optional, keep volume low)

### Keynote Shortcuts You'll Need:

- **Cmd+Option+R** - Start recording slideshow
- **Cmd+.** (period) - Stop recording
- **Cmd+Shift+5** - macOS screen recording tool
- **Cmd+Tab** - Switch between apps (Keynote ↔ Browser)
- **Esc** - Exit Keynote presentation mode
- **Space** or **→** - Advance to next slide
- **File → Export To → Movie** - Export final Keynote recording

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
