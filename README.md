## Manim Projects

This Repo features all the animated math videos I use in my youtube channel. The respective folders contain the python source codes as well as final rendered outputs, feel free to check them out.


All videos are made using `Manim`, an open source Python based Animation Engine.
For more details about manim - [https://github.com/3b1b/manim](https://github.com/3b1b/manim)

---

## ManimGL Installation & Workflow Setup

### Requirements for ManimGL
- **ffmpeg** (for video rendering)
- **LaTeX** (MiKTeX recommended for Windows)
- **Python 3.7+** (Python 3.10 is ideal for ManimGL; Python >3.11 may cause issues)

> If you want to use ManimCE (Community Edition), the latest Python is fine, but ManimCE does not have the live OpenGL interactive workflow. ManimGL is the version Grant Sanderson (3Blue1Brown) uses personally, while ManimCE is community-driven and well-optimized. This repo mainly features ManimGL for an interactive workflow like Grant's.

**Note:** OpenGL is not supported in WSL (Windows Subsystem for Linux), so GPU acceleration won't work for OpenGL-based apps like ManimGL. Use ManimGL directly on Windows or on native Linux (dual boot) for best results.

### Installation Steps

1. **Install ffmpeg**
	- Use Windows Package Manager:
	  ```powershell
	  winget install ffmpeg
	  ```
	- Check installation:
	  ```powershell
	  ffmpeg -version
	  ```

2. **Install MiKTeX (LaTeX for Windows)**
	- Download and install [MiKTeX](https://miktex.org/download) (basic is enough).
	- Run installer as administrator and install for all users.
	- Check installation:
	  ```powershell
	  latex --version
	  pdflatex --version
	  ```

3. **Install Python 3.10**
	- Download from [python.org](https://www.python.org/downloads/release/python-3100/)
	- Add Python to PATH during installation.

4. **Create a folder for your Manim projects**
	- Open terminal in your project folder.
	- Create and activate a virtual environment:
	  ```powershell
	  py -3.10 -m venv .venv
	  ```

5. **Update PATH in Activate.ps1**
	- Edit `.venv\Scripts\Activate.ps1` and add these lines at the end (replace `username` with your Windows username):
	  ```powershell
	  $Env:PATH += ";C:\Program Files\MiKTeX\miktex\bin\x64"
	  $Env:PATH += ";C:\Users\username\AppData\Local\Microsoft\WinGet\Links"
	  ```

6. **Install ManimGL and dependencies**
    - Activate the virtual environment:
      ```powershell
      .venv\Scripts\activate
      ```
    - Install ManimGL and dependencies:
	  ```powershell
	  pip install manimgl pycairo pygame pyqt5 setuptools python-dotenv ipython jupyter
	 ```

7. **Edit default_config.yml**
	- After installation, edit `manimlib/default_config.yml` in your venv (`.venv/Lib/site-packages/manimlib/`) to set your preferred background color, fps, resolution, etc.

---

## Example Usage

Create a sample script:

```python
from manimlib import *

class SquareToCircle(InteractiveScene):
	 def construct(self):
		  square = Square(side_length=2)
		  circle = Circle(radius=5)
		  self.add(square, circle)
		  self.play(Transform(square, circle))
```

Save as `MyScene.py`. To enter interactive mode, run:

```powershell
manimgl MyScene.py SquareToCircle -se 6
```

![Screenshot of ManimGL Interactive Window](Screenshot.png)
An OpenGL interactive window will open. You can interact live with the scene using your mouse and the following keybindings:

**Key Bindings (hold key + move mouse):**
  - pan_3d: `d`
  - pan: `f`
  - reset: `r`
  - quit: `q` (with command)
  - select: `s`
  - unselect: `u`
  - grab: `g`
  - x_grab: `h`
  - y_grab: `v`
  - resize: `t`
  - color: `c`
  - information: `i`
  - cursor: `k`

To test code instantly in the interactive window, type commands like `circle.shift(RIGHT)` in the terminal and hit enter.

To render a scene as a video file:

```powershell
manimgl --uhd MyScene.py SquareToCircle -w
```

---

For detailed documentation, see: https://3b1b.github.io/manim/



