from manim import *

class Outro(Scene):
    def construct(self):
        # Create the text "TO BE" with each letter in red
        text = Text("TO BE", font_size=300, font="onepiece")
        
        # Change the color of the 'O' to yellow
        o_letter = text[1]  # The second character is 'O'
        o_letter.set_color(YELLOW)
        
        # Change the color of the other letters to red
        for char in text:
            if char != o_letter:
                char.set_color(PURE_RED)

        # Create the second line "CONTINUED" in red
        continued_text = Text("CoNtInUeD", font_size=300, color=PURE_RED, font="onepiece")
        
        # Calculate total height of the two lines, including extra space between them
        extra_space = 0.3  # Add extra space
        total_height = text.height + continued_text.height + extra_space

        # Center both lines, adjusting for the extra space
        text.move_to(UP * total_height / 4)  # Move the first line (TO BE)
        continued_text.move_to(DOWN * total_height / 4)  # Move the second line (CONTINUED)

        # Add the text and the multiplication symbol to the scene
        self.play(Write(text))
        self.play(Write(continued_text))
        self.wait(2)