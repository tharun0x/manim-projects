# Manim Projects - AI Coding Agent Instructions

## Project Overview
This is a **ManimGL**-based animation project for creating math education content, primarily YouTube shorts. ManimGL is Grant Sanderson's (3Blue1Brown) original version with live OpenGL interactive workflow—NOT Manim Community Edition.

## Critical: ManimGL vs ManimCE
- **Always use `from manimlib import *`** (not `from manim import *`)
- Use `Scene` or `InteractiveScene` base classes (not `MovingCameraScene` for basic scenes)
- Portrait/resolution handled via CLI flags, NOT config in code: `-r 2160x4320` for 9:16 vertical
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
manimgl 2025/shorts/Nov25/episode1.py Episode1 -se 5 -r 2160x4320
```
- `-se 5`: Start execution at line 5
- `-r 2160x4320`: Portrait resolution (9:16 aspect ratio)
- Opens OpenGL window; use keybindings to interact (see README.md)

**Render to video (4K portrait):**
```bash
manimgl --uhd 2025/shorts/Nov25/episode1.py Episode1 -r 2160x4320 -w
```
- `--uhd`: Ultra HD quality
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
- **Positioning:** `.to_edge(UP, buff=2.0)`, `.next_to(other, DOWN, buff=1.0)`, `.move_to(ORIGIN)`
- **Groups:** `VGroup(obj1, obj2).arrange(RIGHT, buff=0.1)`
- **Colors:** `BLUE`, `RED`, `GREEN`, `YELLOW` (capital, from manimlib.constants)

### Portrait Layout Best Practices
- **Vertical stacking:** Heavy use of `.to_edge(UP/DOWN)` and `.next_to(..., DOWN, buff=X)`
- **Font sizes:** 40-60 for titles, 70-120 for key numbers, 80 for equations
- **Spacing:** `buff=1.0` to `2.0` between elements (more breathing room in portrait)
- **Avoid horizontal spread:** Keep elements centered or vertically aligned

## Content Creation Workflow (Shorts)
1. **Receive storyboard** with timing (0-2s hook, 2-6s method, 6-14s reveal, etc.)
2. **Code in phases:** Match each time segment with `# --- X.X–Y.Ys Section ---` comments
3. **Sync with VO:** Use `self.wait(X)` to leave space for voice-over beats
4. **Iterate:** Run with `-se 5`, test timing, adjust `run_time` and `buff` values

## Custom Assets
- **Custom fonts:** Install to system, reference by name (e.g., `font="onepiece"` in `outro/outro.py`)
- **Images/sounds:** Place in directories defined in `default_config.yml` (raster_images, sounds, etc.)
- **Geometry utils:** Check `geometry.py` for custom shapes/helpers before writing from scratch

## Common Gotchas
- **Don't mix ManimCE and ManimGL syntax:** If you see `from manim import *`, that's ManimCE (wrong)
- **Portrait resolution:** Always specify `-r 2160x4320` in CLI, never hardcode in scene
- **LaTeX rendering:** If `Tex()` fails, check MiKTeX is in PATH (see `.venv/Scripts/Activate.ps1`)
- **Colors:** Use constants like `BLUE` (not strings `"blue"`)
- **InteractiveScene vs Scene:** Use `InteractiveScene` only for test files; use `Scene` for production shorts

## Content Guidelines (YouTube Shorts)
- **Target:** Middle-school level math (Pythagorean theorem, mental math tricks, visual proofs)
- **Duration:** 30-60s (no longer)
- **Hook:** 2-3s, punchy question or challenge
- **Structure:** Hook → Method → Example → Edge case → CTA
- **Avoid jargon:** No "vedic math" (just "speed math tricks")
- **CTA:** "Follow for daily math hacks" at 20-28s mark

## Testing Checklist
- [ ] Scene runs with `-r 2160x4320` (portrait)
- [ ] Timing comments match storyboard
- [ ] `self.wait()` gaps for voice-over
- [ ] Text readable at small screen size (font_size ≥ 40)
- [ ] All imports from `manimlib` (not `manim`)
- [ ] No hardcoded config (resolution, FPS)

## Examples to Reference
- **Short structure:** `2025/shorts/Nov25/episode1.py` (multiply by 11, 30s, complete timing)
- **Interactive testing:** `2025/MyScene.py` (basic transform example)
- **Custom fonts:** `2025/outro/outro.py` + `outro/README.md`
- **ManimCE syntax (avoid):** `2025/teasers/gear2_intro_4k.py` (has `config.pixel_height`, wrong for ManimGL)
