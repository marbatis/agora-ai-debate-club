# Final Video Editing Steps

## What You Have
✅ **Keynote recording**: `AGORA_Keynote_Friendly2.mov`

## What You Need
⏳ **Browser demo recording**: Record the debate running in `demo_client.html`
⏳ **Final combined video**: Edit in iMovie to create 3-minute video

---

## Step 1: Record Browser Demo (Do This Now!)

### Before Recording:
1. ✅ Server is running on port 8000
2. Open `demo_client.html` in browser:
   ```
   file:///Users/marcelosilveira/MyGit_ProjectA/agora-ai-debate-club/demo_client.html
   ```

### Recording Process:

1. **Start screen recording**:
   - Press **Cmd+Shift+5**
   - Click "Record Selected Portion"
   - Draw rectangle around browser window only
   - Click **Record** button

2. **Perform the demo** (~40 seconds):
   - Type: **"Should schools require coding classes?"**
   - Click **"Start Debate"**
   - Wait for loading messages
   - When results appear, scroll to show:
     - Winner announcement
     - Scores (Agent A vs Agent B)
     - Full transcript
     - Rubric breakdown

3. **Stop recording**:
   - Click stop button in menu bar
   - Save as: `browser-demo.mov`
   - Save location: `/Users/marcelosilveira/MyGit_ProjectA/agora-ai-debate-club/`

---

## Step 2: Combine Videos in iMovie

### Open iMovie:
1. Launch **iMovie** (in Applications)
2. Click **"Create New"** → **"Movie"**
3. Name it: "AGORA AI Debate Club - Final"

### Import Videos:
1. **File → Import Media** (or drag and drop)
2. Select these files:
   - `AGORA_Keynote_Friendly2.mov`
   - `browser-demo.mov` (once you record it)
3. Click **Import Selected**

### Arrange Timeline:

1. **Drag Keynote video** to timeline first
2. **Check timing** - Keynote should end around 2:05
3. **Drag browser demo** to timeline after Keynote
4. **Trim if needed**:
   - Click video in timeline
   - Drag yellow handles to trim start/end
   - Target: Total video = 3:00 minutes (180 seconds)

### Timeline Should Look Like:
```
[Keynote Part 1: 0:00-2:05] → [Browser Demo: 2:05-2:45] → [Keynote Part 2: 2:45-3:00]
```

**Note**: If your Keynote recording includes all slides (1-8), you may need to split it:
- Click Keynote video in timeline
- Move playhead to 2:05 mark
- **Modify → Split Clip** (Cmd+B)
- Insert browser demo between the two Keynote sections

### Optional Enhancements:
- **Transitions**: Add subtle "Dissolve" between clips (0.5 seconds)
- **Titles**: Add text overlay for your name/GitHub at the end
- **Audio levels**: Ensure your voice is clear and consistent

---

## Step 3: Export Final Video

### Export Settings:
1. **File → Share → File**
2. Choose these settings:
   - **Resolution**: 1080p
   - **Quality**: High
   - **Compress**: Better Quality
3. **Name**: `AGORA-AI-Debate-Club-Final.mp4`
4. **Save to**: `/Users/marcelosilveira/MyGit_ProjectA/agora-ai-debate-club/`
5. Click **Save**

### Verify Final Video:
- [ ] Duration: ≤ 3:00 minutes (180 seconds)
- [ ] File size: < 100 MB (for Kaggle upload)
- [ ] Format: MP4
- [ ] Resolution: 1080p
- [ ] Audio is clear throughout
- [ ] All sections are visible and readable

---

## Step 4: Upload to Kaggle

### Option A: Direct Upload
1. Go to Kaggle submission page
2. Upload `AGORA-AI-Debate-Club-Final.mp4`
3. Max file size: 100 MB

### Option B: YouTube (Unlisted)
If file is too large:
1. Upload to YouTube as **Unlisted**
2. Copy the link
3. Submit link on Kaggle

---

## Quick Checklist

**Pre-Recording:**
- [x] Keynote video recorded: `AGORA_Keynote_Friendly2.mov`
- [ ] Server running on port 8000
- [ ] Browser demo recorded: `browser-demo.mov`

**Editing:**
- [ ] iMovie project created
- [ ] Both videos imported
- [ ] Videos arranged in timeline
- [ ] Total duration ≤ 3:00
- [ ] Trimmed/adjusted as needed

**Export:**
- [ ] Exported as MP4, 1080p
- [ ] File size < 100 MB
- [ ] Audio/video quality verified
- [ ] Saved as `AGORA-AI-Debate-Club-Final.mp4`

**Upload:**
- [ ] Video uploaded to Kaggle (or YouTube link)
- [ ] Submission confirmed

---

## Troubleshooting

**File too large (> 100 MB)?**
- Re-export with "Medium" quality instead of "High"
- Or trim video to exactly 3:00 (no extra seconds)
- Or upload to YouTube as unlisted

**Audio not syncing?**
- In iMovie: Right-click video → Detach Audio
- Realign audio track manually

**Video looks pixelated?**
- Ensure original recordings were high quality
- Don't scale up videos in iMovie (keep at 100%)

---

**Next step: Record the browser demo now! The server is ready at http://127.0.0.1:8000** 🎬
