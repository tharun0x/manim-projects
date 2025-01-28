from manim import *

# Set resolution to 4K portrait and 60 FPS
config.pixel_height = 3840
config.pixel_width = 2160
config.frame_height = 16.0  # 9:16 aspect ratio
config.frame_width = 9.0
config.frame_rate = 60

class Gear2intro(Scene):
    def construct(self):
        # Create text for the center: "Gear 2" and "Geometry"
        gear_text = Text("GEAR 2", font_size=96, color=RED, weight=BOLD)
        geometry_text = Text("GEOMETRY", font_size=64, color=WHITE, weight=BOLD).next_to(gear_text, DOWN, buff=0.5)

        # Animate "Gear 2" and "Geometry" letter by letter
        self.play(LaggedStart(*[Write(letter) for letter in gear_text], lag_ratio=0.1), run_time=2)
        self.play(LaggedStart(*[Write(letter) for letter in geometry_text], lag_ratio=0.1), run_time=2)
        
        # Diverse geometric shapes scattered around the corners, ensuring visibility
        shapes = VGroup(
            Circle(color=BLUE).scale(1.5).shift(LEFT * 3 + UP * 5),
            Square(color=GREEN).scale(1.2).shift(RIGHT * 3 + UP * 5),
            Triangle(color=YELLOW).scale(1.5).shift(LEFT * 3 + DOWN * 5),
            RegularPolygon(n=6, color=PURPLE).scale(1.5).shift(RIGHT * 3 + DOWN * 4),
            Line(start=LEFT * 3 + UP * 5, end=RIGHT * 3 + UP * 5, color=RED),
            Line(start=UP * 5 + LEFT * 3, end=DOWN * 7 + LEFT * 3, color=WHITE),
            Arrow(start=UP * 5 + RIGHT * 3, end=DOWN * 2 + RIGHT * 3, color=WHITE),
            Cube(fill_color=GREEN, fill_opacity=0.5).scale(0.5).shift(UP * 4 + RIGHT * 2),
            Sphere(fill_color=RED, fill_opacity=0.5).scale(0.5).shift(UP * 6 + LEFT * 2),
        )

        # Add and animate geometric shapes
        self.play(*[Create(shape) for shape in shapes], run_time=4)
        self.wait(2)

        # Center text zooms out while shapes animate
        self.play(
            gear_text.animate.scale(0.7),
            geometry_text.animate.scale(0.5),
            AnimationGroup(*[shape.animate.rotate(PI / 4) for shape in shapes], lag_ratio=0.2),
            run_time=5,
        )

        # Fade out the center text and shapes
        self.play(
            FadeOut(gear_text),
            FadeOut(geometry_text),
            *[FadeOut(shape) for shape in shapes],
            run_time=2,
        )

        # "Stay Tuned" text zooms in
        stay_tuned = VGroup(
            Text("STAY", font_size=96, color=RED, weight=BOLD),
            Text("TUNED", font_size=96, color=WHITE)
        ).arrange(DOWN, buff=0.5)

        self.play(Write(stay_tuned), run_time=1)
        self.play(stay_tuned.animate.scale(50), run_time=6)
        self.wait(1)

        # Fade out to black
        self.play(FadeOut(stay_tuned), run_time=2)
        self.wait(1)
