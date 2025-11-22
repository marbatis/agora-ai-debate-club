# Keynote Slide Content - Copy & Paste Guide

**File to create:** `AGORA-Debate-Video.key`

**Instructions:** Open Keynote → New Document → Choose "White" or "Basic" theme → Copy the content below into each slide.

---

## Slide 1: Title Slide

**Layout:** Title & Subtitle

**Title (large, centered):**
```
AGORA AI Debate Club
```

**Subtitle (medium, centered):**
```
Multi-Agent Debates with LLM-as-Judge
```

**Bottom text (small):**
```
[Your Name]
Kaggle AI Agents Intensive - Capstone Project
```

**Design notes:**
- Keep it clean and minimal
- Use dark text on white background
- Optional: Add a subtle icon (Insert → Choose... → search "debate" or "discussion")

---

## Slide 2: The Problem

**Layout:** Title & Body

**Title:**
```
The Challenge
```

**Body (3 bullet points):**
```
• How do you validate AI reasoning quality?

• How do you compare different AI strategies?

• How do you build structured thinking into AI systems?
```

**Optional visual:**
- Add an icon: Insert → Choose... → search "question" or "thinking"
- Place icon on left or right side of bullets

---

## Slide 3: Why Multi-Agent?

**Layout:** Title & Body (use 2 columns)

**Title:**
```
Traditional AI vs Multi-Agent Debates
```

**Left Column (Single AI):**
```
Single AI
─────────
× One perspective
× Hard to validate
× Confirmation bias
× No adversarial testing
```

**Right Column (Multi-Agent):**
```
Multi-Agent System
──────────────────
✓ Adversarial testing
✓ Objective judging
✓ Better reasoning
✓ Structured evaluation
```

**Design notes:**
- Use text boxes: Insert → Text Box
- Left column: Add subtle red/gray background
- Right column: Add subtle green/blue background
- Or use Keynote's "Comparison" slide layout if available

---

## Slide 4: Architecture

**Layout:** Blank (you'll draw a flowchart)

**Title:**
```
System Architecture
```

**Flowchart to create using shapes:**

1. **User Input** (top, rectangle with rounded corners)
   - Text: "User Input\n(Debate Topic)"
   - Color: Light blue

2. **Arrow down** (Insert → Line → Arrow)

3. **Debate Manager** (rectangle)
   - Text: "Debate Manager\n(Orchestrator)"
   - Color: Purple/violet

4. **Two arrows splitting left and right**

5. **Debater A** (left rectangle)
   - Text: "Debater A\n(PRO Position)\n\nGemini 2.5 Flash"
   - Color: Green

6. **Debater B** (right rectangle)
   - Text: "Debater B\n(CON Position)\n\nGemini 2.5 Flash"
   - Color: Red/orange

7. **Two arrows converging down**

8. **Judge Agent** (rectangle)
   - Text: "Judge Agent\n\nScores Arguments\nLogic | Factuality | Persuasion"
   - Color: Gold/yellow

9. **Arrow down**

10. **Results** (rounded rectangle)
    - Text: "Results\nScores & Winner"
    - Color: Light gray

**Additional labels (text boxes):**
- Next to Debaters: "MCP Fact-Checking Tool"
- Bottom: "FastAPI Backend | Loguru Logging | Pydantic Validation"

**Keynote instructions:**
1. Insert → Shape → Rounded Rectangle (for components)
2. Insert → Line → Connection Line (for arrows)
3. Double-click shape to add text
4. Format → Style → Fill Color (to change colors)
5. Arrange → Align → Center (to align elements)

---

## Slide 5: Live Demo Title

**Layout:** Title Only (centered, large)

**Title (huge, centered):**
```
Live Demo
```

**Design notes:**
- Use maximum font size
- Center both horizontally and vertically
- This is a transition slide before you switch to browser
- Keep it on screen for 2-3 seconds

---

## Slide 6: [SCREEN RECORDING PLACEHOLDER]

**This is NOT a Keynote slide - this is where you'll insert your browser demo video in iMovie**

**What to record:**
1. Open `demo_client.html` in browser
2. Enter topic: "Should schools require coding classes?"
3. Click "Start Debate"
4. Wait for results (or use pre-recorded debate)
5. Show the results:
   - Winner announcement
   - Scores (Agent A vs Agent B)
   - Rubric breakdown
   - Full debate transcript

**Recording duration:** ~40 seconds (2:05-2:45 in the script)

**Recording method:**
- Press Cmd+Shift+5
- Click "Record Selected Portion"
- Select just the browser window
- Click Record
- Do the demo
- Click Stop in menu bar
- Save as `demo-recording.mov`

---

## Slide 7: What I Learned

**Layout:** Title & Body

**Title:**
```
What I Learned Building This
```

**Body (3 bullet points):**
```
• Multi-agent coordination requires careful prompt engineering
  
• LLM-as-judge works well with explicit rubrics and JSON schemas

• Model Context Protocol makes tool integration clean and standardized
```

**Design notes:**
- Keep bullets concise
- Use medium font size
- Add spacing between bullets for readability

---

## Slide 8: End Screen

**Layout:** Title & Body (centered)

**Title:**
```
Check It Out on GitHub
```

**Body (large, centered text):**
```
github.com/marbatis/agora-ai-debate-club
```

**Bottom text:**
```
Built for Kaggle AI Agents Intensive
November 2024
```

**Optional:**
- Add GitHub logo icon (Insert → Choose... → search "github")
- Add QR code linking to your repo (generate at qr-code-generator.com)

---

## Quick Keynote Building Guide

### Step-by-Step Process:

1. **Open Keynote** → New Document → Choose "White" theme
2. **Slide 1 already exists** - Select "Title & Subtitle" layout
3. **Add Slide 2** - Click "+" button or press Cmd+Shift+N
4. **Continue adding slides** - For each new slide:
   - Click "+" to add slide
   - Choose appropriate layout (Title & Body, Blank, etc.)
   - Copy text from this document
   - Paste into Keynote (Cmd+V)
   - Format as needed

### Formatting Tips:

**Changing layouts:**
- Click slide in navigator (left panel)
- Format panel (top right) → Slide Layout
- Choose: Title & Subtitle, Title & Body, Blank, etc.

**Adding shapes (for architecture diagram):**
1. Click Slide 4
2. Insert → Shape → Rounded Rectangle
3. Drag to create shape
4. Double-click to add text
5. Format → Style → Fill Color to change color
6. Repeat for all components

**Adding arrows:**
1. Insert → Line → Connection Line
2. Click and drag from one shape to another
3. Format → Style → Endpoints → Choose arrow type

**Text formatting:**
- Bold: Cmd+B
- Increase size: Cmd+Plus
- Decrease size: Cmd+Minus
- Align center: Cmd+Shift+{
- Align left: Cmd+Shift+|

### Color Recommendations:

- **Debater A (PRO):** Green (#34C759)
- **Debater B (CON):** Red/Orange (#FF6B6B)
- **Judge:** Gold/Yellow (#FFD60A)
- **Debate Manager:** Purple (#AF52DE)
- **User Input:** Light Blue (#007AFF)
- **Results:** Gray (#8E8E93)

To apply colors:
1. Select shape
2. Format panel (right) → Style → Fill
3. Click color picker → enter hex code

---

## Recording Your Presentation

### Option 1: Keynote Built-in Recording (RECOMMENDED)

1. **Finish all slides except demo** (Slides 1-5, 7-8)
2. **Play → Record Slideshow** (Cmd+Option+R)
3. **Start speaking** and click/arrow to advance slides
4. **Stop at Slide 5** ("Live Demo")
5. **Press Cmd+.** to stop recording
6. **File → Export To → Movie → 1080p**
7. Save as `keynote-recording.mov`

### Option 2: Record Browser Demo Separately

1. **Close Keynote**
2. **Open demo_client.html** in browser
3. **Press Cmd+Shift+5** → Record Selected Portion
4. **Record the demo** (40 seconds)
5. **Stop recording** → Save as `demo-recording.mov`

### Option 3: Combine in iMovie

1. **Open iMovie** → New Movie
2. **Import both videos:**
   - `keynote-recording.mov` (slides 1-5)
   - `demo-recording.mov` (browser demo)
   - `keynote-ending.mov` (slides 7-8) - record these separately
3. **Drag to timeline in order:**
   - Keynote part 1 (0:00-2:05)
   - Browser demo (2:05-2:45)
   - Keynote part 2 (2:45-3:00)
4. **Trim if needed** to hit exactly 3:00
5. **File → Share → File → 1080p**
6. Save as `AGORA-Final-Video.mp4`

---

## Final Checklist

Before recording:
- [ ] All 8 slides created in Keynote
- [ ] Architecture diagram complete with shapes and arrows
- [ ] Colors applied to shapes
- [ ] Text is readable at presentation size
- [ ] Spell-check done (Edit → Spelling and Grammar)
- [ ] Browser demo works (test demo_client.html)
- [ ] Script printed or on second screen
- [ ] Microphone tested
- [ ] Quiet recording environment

After recording:
- [ ] Video is exactly 3 minutes (or under)
- [ ] Audio is clear and audible
- [ ] All slides are visible and readable
- [ ] Browser demo shows results clearly
- [ ] File size is under 100MB
- [ ] Format is MP4 (H.264)
- [ ] Exported at 1080p resolution

---

**You're all set! Build the Keynote presentation using this guide, record your voiceover, and you'll have a professional 3-minute video for Kaggle. Good luck! 🎥**
