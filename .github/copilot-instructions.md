# Manim Projects - AI Coding Agent Instructions

## Project Overview
This is a **ManimGL**-based animation project for creating math education content, primarily YouTube shorts. ManimGL is Grant Sanderson's (3Blue1Brown) original version with live OpenGL interactive workflow—NOT Manim Community Edition.

## Critical: ManimGL vs ManimCE
- **Always use `from manimlib import *`** (not `from manim import *`)
- Use `Scene` or `InteractiveScene` base classes (not `MovingCameraScene` for basic scenes)
- Portrait/resolution handled via CLI flags, NOT config in code: `-r 1080x2160` for 9:18 vertical
- No `config.pixel_height` or `config.frame_height` in ManimGL scenes (that's ManimCE syntax)

## Project Structure
```
2025/
  ├── shorts/Nov25/        # YouTube shorts (portrait, 30-60s, middle-school math)
  ├── outro/               # Custom font projects (see outro/README.md)
  ├── teasers/             # Channel intro/teaser animations
  └── MyScene.py           # Scratch/test file
geometry.py                # Custom geometry utilities (1100+ lines)
default_config.yml         # Global ManimGL config (directories, window, camera)
```

## Development Workflow

### Running Scenes
**Live interactive preview (portrait):**
```bash
manimgl 2025/shorts/Nov25/episode1.py Episode1 -se 5 -r 1080x2160
```
- `-se 5`: Start execution at line 5
- `-r 1080x2160`: Portrait resolution (9:18 aspect ratio)
- Opens OpenGL window; use keybindings to interact (see README.md)

**Render to video (Full HD portrait):**
```bash
manimgl --hd 2025/shorts/Nov25/episode1.py Episode1 -r 1080x2160 -w
```
- `--hd`: HD quality
- `-w`: Write to file

**Interactive testing:** In the live window terminal, type commands like `circle.shift(RIGHT)` to test immediately.

### Environment Setup
- **Python 3.10** (not 3.11+, compatibility issues)
- Virtual env at `.venv/` with `manimgl pycairo pygame pyqt5` installed
- **Windows only** for OpenGL (WSL doesn't support GPU acceleration)
- LaTeX (MiKTeX) and ffmpeg required (see README.md installation steps)

## Code Patterns for ManimGL

### Scene Structure (Shorts)
```python
from manimlib import *

class Episode1(Scene):  # Use Scene, not InteractiveScene for shorts
    def construct(self):
        # 0-2s: Hook with big text
        title = Text("Your Hook", font_size=40)
        title.to_edge(UP, buff=2.0)  # Portrait: use UP/DOWN heavily
        
        # Use VGroup for multi-element positioning
        group = VGroup(d1, d2).arrange(RIGHT, buff=0.2)
        group.move_to(ORIGIN)
        
        # Timing: explicit run_time + wait() for VO sync
        self.play(Write(title), run_time=1)
        self.wait(0.5)  # Space for voice-over
```

### Key ManimGL Syntax
- **Text:** `Text("string", font_size=X, color=BLUE)` or `Tex("latex", font_size=X)`
- **Animations:** `self.play(Write(...), run_time=2)`, `FadeIn(..., shift=UP)`, `Transform(a, b)`
  - **Note:** `ShrinkToCenter` does NOT take `shift`.
  - **Cleanup:** Use `FadeOut(Group(...))` for multiple items.
  - **Transformations:** When replacing a number with a calculated result, use `ReplacementTransform(calc_part, target)` AND `ReplacementTransform(original, target)` to merge them.
- **Resizing:** Use `set_width()` or `set_height()`. **Avoid** `scale_to_fit_width()` (ManimCE).
- **Positioning:** `.to_edge(UP, buff=2.0)`, `.next_to(other, DOWN, buff=1.0)`, `.move_to(ORIGIN)`
- **Groups:** `VGroup(obj1, obj2).arrange(RIGHT, buff=0.1)`
- **Colors:** Use matte pastel colors (3b1b style):
  - `TEAL` (not `BLUE`)
  - `GOLD` (not `YELLOW`)
  - `GREEN_C` (not `GREEN`)
  - `RED` and `WHITE` are standard.
  - `Triangle()` needs explicit color (e.g., `color=GOLD`).

### Portrait Layout Best Practices (9:18)
- **Resolution:** 1080x2160 (60fps).
- **Vertical Stacking:** Essential. Use `.next_to(..., DOWN)` or `.to_edge(UP/DOWN)`.
- **Buff Values:**
  - **Titles:** `buff=1.5` to `2.0` from `UP` edge (leaves room for UI).
  - **Between Sections:** `buff=1.0` to `1.5` (clear separation).
  - **Tight Grouping:** `buff=0.2` to `0.5` (e.g., equation steps).
- **Font Sizes:**
  - **Titles:** `35-40` (readable, not overwhelming).
  - **Main Equations:** `50-60`.
  - **Big Numbers (Visuals):** `120` (main focus), `30-40` (secondary).
  - **CTA/Footer:** `30-40`.
- **Avoid Horizontal Spread:** Keep elements centered or vertically aligned.

## Content Creation Workflow (Shorts)
1. **Receive storyboard** with timing.
2. **Code in phases:** Use comments to describe *actions* (e.g., `# Split 35`, `# Transform d1 -> 12`), NOT timestamps or brainstorming notes.
3. **Sync with VO:** Use `self.wait(X)` to leave space for voice-over beats.
4. **Iterate:** Run with `-se 5`, test timing, adjust `run_time` and `buff` values.

## Standard CTA Pattern
- **Text:** "LIKE" (Teal), "SHARE" (White), "SUBSCRIBE" (Red).
- **Font:** "American Captain" (if available) or default.
- **Animation:**
  1. Write "LIKE".
  2. `TransformFromCopy` "LIKE" -> "SHARE" (below).
  3. `TransformFromCopy` "SHARE" -> "SUBSCRIBE" (below).
  4. Exit: `animate.shift(LEFT/RIGHT * 10)` with `lag_ratio=0.1` (fast zip off-screen).

## Custom Assets
- **Custom fonts:** Install to system, reference by name (e.g., `font="onepiece"` in `outro/outro.py`)
- **Images/sounds:** Place in directories defined in `default_config.yml` (raster_images, sounds, etc.)
- **Geometry utils:** Check `geometry.py` for custom shapes/helpers before writing from scratch

## Common Gotchas
- **Don't mix ManimCE and ManimGL syntax:** If you see `from manim import *`, that's ManimCE (wrong)
- **Portrait resolution:** Always specify `-r 1080x2160` in CLI, never hardcode in scene
- **LaTeX rendering:** If `Tex()` fails, check MiKTeX is in PATH (see `.venv/Scripts/Activate.ps1`)
- **Colors:** Use constants like `TEAL` or `GOLD` (not strings `"blue"` or standard `BLUE`)
- **InteractiveScene vs Scene:** Use `InteractiveScene` only for test files; use `Scene` for production shorts

## Content Guidelines (YouTube Shorts)
- **Target:** Middle-school level math (Pythagorean theorem, mental math tricks, visual proofs)
- **Duration:** 30-60s (no longer)
- **Hook:** 2-3s, punchy question or challenge
- **Structure:** Hook → Method → Example → Edge case → CTA
- **Avoid jargon:** No "vedic math" (just "speed math tricks")
- **CTA:** Standard "LIKE, SHARE, SUBSCRIBE" animation at end

## Testing Checklist
- [ ] Scene runs with `-r 1080x2160` (portrait)
- [ ] Timing comments match storyboard
- [ ] `self.wait()` gaps for voice-over
- [ ] Text readable at small screen size (font_size ≥ 40)
- [ ] All imports from `manimlib` (not `manim`)
- [ ] No hardcoded config (resolution, FPS)

## Examples to Reference
- **Short structure:** `2025/shorts/Nov25/episode2.py` (squaring 5s, perfected workflow, standard CTA)
- **Interactive testing:** `2025/MyScene.py` (basic transform example)
- **Custom fonts:** `2025/outro/outro.py` + `outro/README.md`
- **ManimCE syntax (avoid):** `2025/teasers/gear2_intro_4k.py` (has `config.pixel_height`, wrong for ManimGL)
