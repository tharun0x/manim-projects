from manimlib import *

class Episode13(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK — show the completed square first (visual-first)
        # =================================================================
        hook_eq = Tex("1 + 3 + 5 + 7 = 16 = 4^2", font_size=40)
        hook_eq.to_edge(UP, buff=3)
        self.play(Write(hook_eq), run_time=1.5)
        self.wait(1)

        hook_q = Text("Why always a\nPERFECT SQUARE?", font_size=30, fill_color=RED)
        hook_q.next_to(hook_eq, DOWN, buff=0.5)
        self.play(Write(hook_q), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(hook_eq), FadeOut(hook_q), run_time=1)

        # =================================================================
        # SECTION 2: THE PROOF — L-shaped blocks forming squares
        # =================================================================
        cell = 0.55  # cell size
        origin = np.array([-1.0, -0.5, 0])  # bottom-left of grid

        def make_cell(row, col, color):
            sq = Square(side_length=cell)
            sq.set_fill(color, opacity=0.7)
            sq.set_stroke(WHITE, width=1.5)
            sq.move_to(origin + np.array([col * cell + cell / 2, row * cell + cell / 2, 0]))
            return sq

        # Layer 1: single cell (1) — BLUE
        layer1 = VGroup(make_cell(0, 0, BLUE))
        label1 = Tex("1", font_size=35)
        label1.next_to(layer1, DOWN, buff=0.3)

        eq1 = Tex("1 = 1^2", font_size=35, fill_color=BLUE)
        eq1.to_edge(UP, buff=1.5)
        self.play(FadeIn(layer1), Write(label1), Write(eq1), run_time=1.5)
        self.wait(2)

        # Layer 2: L-shape of 3 cells — GREEN (wrap to form 2×2)
        layer2 = VGroup(
            make_cell(1, 0, GREEN),
            make_cell(1, 1, GREEN),
            make_cell(0, 1, GREEN),
        )
        label2 = Tex("3", font_size=35)
        label2.next_to(label1, RIGHT, buff=0.4)

        eq2 = Tex("1 + 3 = 4 = 2^2", font_size=35, fill_color=GREEN)
        eq2.to_edge(UP, buff=1.5)
        self.play(FadeIn(layer2), Write(label2), Transform(eq1, eq2), run_time=1.5)
        self.wait(2)

        # Layer 3: L-shape of 5 cells — ORANGE (wrap to form 3×3)
        layer3 = VGroup(
            make_cell(2, 0, ORANGE),
            make_cell(2, 1, ORANGE),
            make_cell(2, 2, ORANGE),
            make_cell(1, 2, ORANGE),
            make_cell(0, 2, ORANGE),
        )
        label3 = Tex("5", font_size=35)
        label3.next_to(label2, RIGHT, buff=0.4)

        eq3 = Tex("1 + 3 + 5 = 9 = 3^2", font_size=35, fill_color=ORANGE)
        eq3.to_edge(UP, buff=1.5)
        self.play(FadeIn(layer3), Write(label3), Transform(eq1, eq3), run_time=1.5)
        self.wait(2)

        # Layer 4: L-shape of 7 cells — RED (wrap to form 4×4)
        layer4 = VGroup(
            make_cell(3, 0, RED),
            make_cell(3, 1, RED),
            make_cell(3, 2, RED),
            make_cell(3, 3, RED),
            make_cell(2, 3, RED),
            make_cell(1, 3, RED),
            make_cell(0, 3, RED),
        )
        label4 = Tex("7", font_size=35)
        label4.next_to(label3, RIGHT, buff=0.4)

        eq4 = Tex("1 + 3 + 5 + 7 = 16 = 4^2", font_size=35, fill_color=RED)
        eq4.to_edge(UP, buff=1.5)
        self.play(FadeIn(layer4), Write(label4), Transform(eq1, eq4), run_time=1.5)
        self.wait(2)

        formula = Tex("1 + 3 + 5 + \\cdots + (2n-1) = n^2", font_size=30, fill_color=BLUE)
        formula.to_edge(DOWN, buff=2.3)
        self.play(Write(formula), run_time=2)
        self.wait(2)

        caption = Text("Sum of first n odd\nnumbers is equal to n^2", font_size=30, fill_color=RED)
        caption.next_to(formula, DOWN, buff=0.5)
        self.play(Write(caption), run_time=2)
        self.wait(2)

        self.play(
            FadeOut(layer1), FadeOut(layer2), FadeOut(layer3), FadeOut(layer4),
            FadeOut(label1), FadeOut(label2), FadeOut(label3), FadeOut(label4),
            FadeOut(eq1), FadeOut(formula), FadeOut(caption),
            run_time=1
        )

        # =================================================================
        # SECTION 3: EXAMPLE
        # =================================================================
        ex_title = Text("Example", font_size=40, fill_color=TEAL)
        ex_title.to_edge(UP, buff=2.5)
        self.play(Write(ex_title), run_time=1)
        self.wait(1)

        ex1 = Text("First 5 odd numbers", font_size=30)
        ex1.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(ex1), run_time=1)
        self.wait(1)

        ex2 = Tex("1 + 3 + 5 + 7 + 9", font_size=40)
        ex2.next_to(ex1, DOWN, buff=0.4)
        self.play(Write(ex2), run_time=1.5)
        self.wait(1)

        ex3 = Tex("= 25 = 5^2", font_size=45, fill_color=GREEN_C)
        ex3.next_to(ex2, DOWN, buff=0.4)
        self.play(Write(ex3), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(ex_title), FadeOut(ex1), FadeOut(ex2), FadeOut(ex3),
            run_time=1
        )

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("1 + 3 + 5 + \\cdots + 19 = \\ ?", font_size=45)
        challenge_group = VGroup(c_title, c_eq).arrange(DOWN, buff=0.3)
        challenge_group.to_edge(UP, buff=2.5)

        self.play(Write(challenge_group), run_time=2)
        self.wait(2)

        clock = VGroup()
        face = Circle(radius=0.5, stroke_color=TEAL)
        ticks = VGroup()
        for i in range(4):
            tick = Line(UP * 0.4, UP * 0.5).rotate(i * PI / 2, about_point=ORIGIN)
            ticks.add(tick)
        hand = Line(ORIGIN, UP * 0.4, stroke_width=4)
        clock.add(face, ticks, hand)
        clock.next_to(challenge_group, DOWN, buff=1.0)

        self.play(Write(clock))
        self.play(
            Rotate(hand, angle=-TAU, about_point=face.get_center()),
            run_time=5, rate_func=linear
        )
        self.wait(2)
        self.play(FadeOut(clock), FadeOut(challenge_group), run_time=1.5)

        # =================================================================
        # CTA
        # =================================================================
        like_text = Text("LIKE", font_size=40, fill_color=TEAL)
        like_text.move_to(ORIGIN).shift(UP * 1)
        self.play(Write(like_text), run_time=0.5)

        share_text = Text("SHARE", font_size=40, fill_color=WHITE)
        share_text.next_to(like_text, DOWN, buff=0.5)
        self.play(TransformFromCopy(like_text, share_text), run_time=0.5)

        subscribe_text = Text("SUBSCRIBE", font_size=40, fill_color=RED)
        subscribe_text.next_to(share_text, DOWN, buff=0.5)
        self.play(TransformFromCopy(share_text, subscribe_text), run_time=0.5)
        self.wait(2)

        self.play(
            like_text.animate.shift(LEFT * 10),
            share_text.animate.shift(RIGHT * 10),
            subscribe_text.animate.shift(LEFT * 10),
            run_time=0.5, lag_ratio=0.1
        )
        self.wait(2)
