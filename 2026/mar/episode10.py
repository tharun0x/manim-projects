from manimlib import *

class Episode10(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK — Misconception
        # =================================================================
        wrong_eq = Tex("(a - b)^2 = a^2 - b^2", font_size=50, fill_color=RED)
        wrong_eq.move_to(ORIGIN)
        self.play(Write(wrong_eq), run_time=1.5)
        self.wait(2)

        cross = Cross(wrong_eq, stroke_color=RED, stroke_width=8)
        self.play(ShowCreation(cross), run_time=1.0)
        self.wait(2)

        question = Tex("(a - b)^2 \\ = \\ ?", font_size=50, fill_color=WHITE)
        question.move_to(ORIGIN)
        self.play(
            FadeOut(cross),
            ReplacementTransform(wrong_eq, question),
            run_time=1.5
        )
        self.wait(2)
        self.play(FadeOut(question), run_time=1.5)

        # =================================================================
        # SECTION 2: VISUAL PROOF
        # =================================================================
        a_val = 3.0
        b_val = 1.0

        sq_center = ORIGIN + UP * 0.5
        sq_left = sq_center[0] - a_val / 2
        sq_right = sq_center[0] + a_val / 2
        sq_top = sq_center[1] + a_val / 2
        sq_bottom = sq_center[1] - a_val / 2

        # Title
        proof_title = Text("Visual Proof", font_size=40, fill_color=TEAL)
        proof_title.to_edge(UP, buff=1)
        self.play(Write(proof_title), run_time=1.5)
        self.wait(2)

        # Big square of side a
        main_square = Square(side_length=a_val, stroke_color=TEAL, stroke_width=3)
        main_square.move_to(sq_center)
        a_label = Tex("a^2", font_size=40, fill_color=TEAL)
        a_label.move_to(sq_center)
        self.play(ShowCreation(main_square), Write(a_label), run_time=2)
        self.wait(2)

        # Split lines for (a-b) and b
        split_x = sq_right - b_val   # vertical line from right
        split_y = sq_bottom + b_val  # horizontal line from bottom

        # Braces for side lengths BEFORE split lines
        # Bottom brace — full side "a"
        brace_a = Brace(main_square, DOWN, buff=0.1)
        lbl_a = Tex("a", font_size=35, fill_color=TEAL)
        lbl_a.next_to(brace_a, DOWN, buff=0.1)
        self.play(GrowFromCenter(brace_a), Write(lbl_a), run_time=1.5)
        self.wait(2)

        # Left brace — full side "a"
        brace_a2 = Brace(main_square, LEFT, buff=0.1)
        lbl_a2 = Tex("a", font_size=35, fill_color=TEAL)
        lbl_a2.next_to(brace_a2, LEFT, buff=0.1)
        self.play(GrowFromCenter(brace_a2), Write(lbl_a2), run_time=1.5)
        self.wait(2)

        # Top brace — right portion "b"
        top_b_line = Line(
            np.array([split_x, sq_top, 0]),
            np.array([sq_right, sq_top, 0])
        )
        brace_b_top = Brace(top_b_line, UP, buff=0.1)
        lbl_b_top = Tex("b", font_size=35, fill_color=RED)
        lbl_b_top.next_to(brace_b_top, UP, buff=0.1)
        self.play(GrowFromCenter(brace_b_top), Write(lbl_b_top), run_time=1.5)
        self.wait(2)

        # Right brace — bottom portion "b"
        right_b_line = Line(
            np.array([sq_right, sq_bottom, 0]),
            np.array([sq_right, split_y, 0])
        )
        brace_b_right = Brace(right_b_line, RIGHT, buff=0.1)
        lbl_b_right = Tex("b", font_size=35, fill_color=RED)
        lbl_b_right.next_to(brace_b_right, RIGHT, buff=0.1)
        self.play(GrowFromCenter(brace_b_right), Write(lbl_b_right), run_time=1.5)
        self.wait(2)

        # Now draw the split lines (intersecting at brace endpoints)
        v_line = DashedLine(
            np.array([split_x, sq_top, 0]),
            np.array([split_x, sq_bottom, 0]),
            stroke_color=WHITE, stroke_width=2
        )
        h_line = DashedLine(
            np.array([sq_left, split_y, 0]),
            np.array([sq_right, split_y, 0]),
            stroke_color=WHITE, stroke_width=2
        )
        self.play(ShowCreation(v_line), ShowCreation(h_line), run_time=1.5)
        self.wait(2)

        # Fade out center label
        self.play(FadeOut(a_label), run_time=0.5)

        # Top-left brace — (a-b) side
        top_ab_line = Line(
            np.array([sq_left, sq_top, 0]),
            np.array([split_x, sq_top, 0])
        )
        brace_ab = Brace(top_ab_line, UP, buff=0.1)
        lbl_ab = Tex("a - b", font_size=35, fill_color=TEAL)
        lbl_ab.next_to(brace_ab, UP, buff=0.1)
        self.play(GrowFromCenter(brace_ab), Write(lbl_ab), run_time=1.5)
        self.wait(2)
        # (a-b)² remaining square — show FIRST with Indicate
        remaining = Square(
            side_length=a_val - b_val,
            fill_color=TEAL, fill_opacity=0.3, stroke_width=2, stroke_color=TEAL
        )
        remaining.move_to(np.array([sq_left + (a_val - b_val) / 2, sq_top - (a_val - b_val) / 2, 0]))
        self.play(FadeIn(remaining), run_time=1)
        self.play(Indicate(remaining, color=TEAL, scale_factor=1.05), run_time=1.5)

        remaining_label = Tex("(a-b)^2", font_size=30, fill_color=WHITE)
        remaining_label.move_to(remaining)
        self.play(Write(remaining_label), run_time=1)
        self.wait(2)

        # Now explain HOW — subtract the strips
        # Right strip (a × b) — RED
        right_strip = Rectangle(
            width=b_val, height=a_val,
            fill_color=RED, fill_opacity=0.5, stroke_width=0
        )
        right_strip.move_to(np.array([split_x + b_val / 2, sq_center[1], 0]))
        right_label = Tex("a \\times b", font_size=30, fill_color=WHITE)
        right_label.move_to(right_strip)

        self.play(FadeIn(right_strip), Write(right_label), run_time=1.5)
        self.wait(2)

        # Bottom strip (a × b) — RED
        bottom_strip = Rectangle(
            width=a_val, height=b_val,
            fill_color=RED, fill_opacity=0.5, stroke_width=0
        )
        bottom_strip.move_to(np.array([sq_center[0], sq_bottom + b_val / 2, 0]))
        bottom_label = Tex("a \\times b", font_size=30, fill_color=WHITE)
        bottom_label.move_to(bottom_strip)

        self.play(FadeIn(bottom_strip), Write(bottom_label), run_time=1.5)
        self.wait(2)

        # Corner overlap (b²) — GOLD
        corner = Square(
            side_length=b_val,
            fill_color=GOLD, fill_opacity=0.7, stroke_width=0
        )
        corner.move_to(np.array([split_x + b_val / 2, sq_bottom + b_val / 2, 0]))
        corner_label = Tex("b^2", font_size=30, fill_color=WHITE)
        corner_label.move_to(corner)

        self.play(Indicate(corner, color=GOLD), run_time=1.5)
        self.play(FadeIn(corner), Write(corner_label), run_time=1.5)
        self.wait(2)
        # =================================================================
        # FORMULA ASSEMBLY — TransformFromCopy from geometry parts
        # =================================================================
        # Position formula below the square
        formula_y = sq_bottom - 1.2

        # Stage 1: (a-b)² = a² - ab - ab + b²
        f_ab2 = Tex("(a-b)^2", font_size=35, fill_color=TEAL)
        f_eq = Tex("=", font_size=35)
        f_a2 = Tex("a^2", font_size=35, fill_color=TEAL)
        f_minus1 = Tex("-", font_size=35, fill_color=RED)
        f_ab_1 = Tex("ab", font_size=35, fill_color=RED)
        f_minus2 = Tex("-", font_size=35, fill_color=RED)
        f_ab_2 = Tex("ab", font_size=35, fill_color=RED)
        f_plus = Tex("+", font_size=35, fill_color=GOLD)
        f_b2 = Tex("b^2", font_size=35, fill_color=GOLD)

        formula_1 = VGroup(f_ab2, f_eq, f_a2, f_minus1, f_ab_1, f_minus2, f_ab_2, f_plus, f_b2)
        formula_1.arrange(RIGHT, buff=0.15)
        formula_1.move_to(np.array([0, formula_y, 0]))

        # (a-b)² copies from remaining square label
        self.play(TransformFromCopy(remaining_label, f_ab2), run_time=1)
        self.play(Write(f_eq), run_time=0.5)
        # a² copies from brace_a label
        self.play(TransformFromCopy(lbl_a, f_a2), run_time=1)
        # -ab from right strip
        self.play(Write(f_minus1), run_time=0.3)
        self.play(TransformFromCopy(right_label, f_ab_1), run_time=1)
        # -ab from bottom strip
        self.play(Write(f_minus2), run_time=0.3)
        self.play(TransformFromCopy(bottom_label, f_ab_2), run_time=1)
        # +b² from corner
        self.play(Write(f_plus), run_time=0.3)
        self.play(TransformFromCopy(corner_label, f_b2), run_time=1)
        self.wait(2)

        # Stage 2: simplify to (a-b)² = a² - 2ab + b² (right below stage 1, same screen)
        formula_2_y = formula_y - 0.8

        s_ab2 = Tex("(a-b)^2", font_size=35, fill_color=TEAL)
        s_eq = Tex("=", font_size=35)
        s_a2 = Tex("a^2", font_size=35)
        s_minus = Tex("-", font_size=35)
        s_2ab = Tex("2ab", font_size=35, fill_color=RED)
        s_plus = Tex("+", font_size=35)
        s_b2 = Tex("b^2", font_size=35, fill_color=GOLD)

        formula_2 = VGroup(s_ab2, s_eq, s_a2, s_minus, s_2ab, s_plus, s_b2)
        formula_2.arrange(RIGHT, buff=0.15)
        formula_2.move_to(np.array([0, formula_2_y, 0]))

        # (a-b)² = a² copies down
        self.play(
            TransformFromCopy(f_ab2, s_ab2),
            TransformFromCopy(f_eq, s_eq),
            TransformFromCopy(f_a2, s_a2),
            run_time=1
        )
        # -ab - ab transforms into -2ab
        ab_group = VGroup(f_minus1, f_ab_1, f_minus2, f_ab_2)
        self.play(Write(s_minus), run_time=0.3)
        self.play(TransformFromCopy(ab_group, s_2ab), run_time=1)
        # +b² copies down
        self.play(
            TransformFromCopy(f_plus, s_plus),
            TransformFromCopy(f_b2, s_b2),
            run_time=1
        )
        self.wait(2)

        # Box around final formula
        box = SurroundingRectangle(formula_2, color=TEAL, buff=0.2)
        self.play(ShowCreation(box), run_time=1)
        self.wait(2)

        # Fade EVERYTHING at the end
        self.play(
            FadeOut(proof_title), FadeOut(main_square), FadeOut(v_line), FadeOut(h_line),
            FadeOut(brace_a), FadeOut(lbl_a),
            FadeOut(brace_b_top), FadeOut(lbl_b_top),
            FadeOut(brace_b_right), FadeOut(lbl_b_right),
            FadeOut(brace_ab), FadeOut(lbl_ab),
            FadeOut(brace_a2), FadeOut(lbl_a2),
            FadeOut(right_strip), FadeOut(right_label),
            FadeOut(bottom_strip), FadeOut(bottom_label),
            FadeOut(corner), FadeOut(corner_label),
            FadeOut(remaining), FadeOut(remaining_label),
            FadeOut(formula_1), FadeOut(formula_2), FadeOut(box),
            run_time=1.5
        )

        # =================================================================
        # SECTION 3: NUMERICAL EXAMPLE
        # =================================================================
        ex_title = Text("Try 17 squared", font_size=40, fill_color=TEAL)
        ex_title.to_edge(UP, buff=1.5)
        self.play(Write(ex_title), run_time=1.5)
        self.wait(2)

        n1 = Tex("17^2 \\ = \\ (20 - 3)^2", font_size=45)
        n1.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(n1), run_time=1.5)
        self.wait(2)

        n1b = Tex("= \\ 20^2 - 2(20)(3) + 3^2", font_size=40)
        n1b.next_to(n1, DOWN, buff=0.5)
        self.play(Write(n1b), run_time=1.5)
        self.wait(2)

        n2 = Tex("= \\ 400 - 120 + 9", font_size=45)
        n2.next_to(n1b, DOWN, buff=0.5)
        self.play(Write(n2), run_time=1.5)
        self.wait(2)

        n3 = Tex("= \\ 289", font_size=50, fill_color=BLUE)
        n3.next_to(n2, DOWN, buff=0.5)
        self.play(Write(n3), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(ex_title), FadeOut(n1), FadeOut(n1b), FadeOut(n2), FadeOut(n3), run_time=1.5)

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("19^2 \\ = \\ (20 - 1)^2 \\ = \\ ?", font_size=40)
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
            run_time=5,
            rate_func=linear
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
            run_time=0.5,
            lag_ratio=0.1
        )
        self.wait(2)
