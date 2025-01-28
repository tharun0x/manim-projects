from manim import *

class logo(Scene):
    def construct(self):
        # Create each letter of "Tharun" using LaTeX-style math formatting
        letters = [
            MathTex(r"T", color=RED),
            MathTex(r"h", color=RED),
            MathTex(r"a", color=RED),
            MathTex(r"r", color=RED),
            MathTex(r"u", color=RED),
            MathTex(r"n", color=RED)
        ]
        
        # Position each letter appropriately to form the word "Tharun"
        letters[0].shift(LEFT * 2)
        letters[1].next_to(letters[0], RIGHT)
        letters[2].next_to(letters[1], RIGHT)
        letters[3].next_to(letters[2], RIGHT)
        letters[4].next_to(letters[3], RIGHT)
        letters[5].next_to(letters[4], RIGHT)
        
        # Display the letters one by one, animating them with "Write" (drawing effect)
        self.play(Write(letters[0], run_time=0.5))
        self.play(Write(letters[1], run_time=0.5))
        self.play(Write(letters[2], run_time=0.5))
        self.play(Write(letters[3], run_time=0.5))
        self.play(Write(letters[4], run_time=0.5))
        self.play(Write(letters[5], run_time=0.5))
        
        # Add a mathy effect with a simple line (like an axis) or function
        line = Line(start=LEFT * 4, end=RIGHT * 4, color=GREEN)
        self.play(Create(line, run_time=2))
        
        # Hold for a moment to let the logo appear fully
        self.wait(1)

        # Fade out everything
        self.play(FadeOut(letters[0], run_time=0.5))
        self.play(FadeOut(letters[1], run_time=0.5))
        self.play(FadeOut(letters[2], run_time=0.5))
        self.play(FadeOut(letters[3], run_time=0.5))
        self.play(FadeOut(letters[4], run_time=0.5))
        self.play(FadeOut(letters[5], run_time=0.5))
        self.play(FadeOut(line, run_time=1))

        # Set background color
        self.camera.background_color = WHITE

# Command to render the video
# manim -pql logo_script.py TharunLogo
