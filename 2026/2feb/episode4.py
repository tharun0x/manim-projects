from manimlib import DOWN
from manimlib import *

class Episode4(Scene):
    def construct(self):
        # Setup dimensions
        a_val = 2.0
        b_val = 1.2
        total = a_val + b_val
        
        # 1. Hook
        wrong_eq = Tex("(a + b)^2 = a^2 + b^2", font_size=50, fill_color=RED)
        wrong_eq.move_to(ORIGIN)
        self.play(Write(wrong_eq), run_time=1.5)
        
        cross = Cross(wrong_eq, stroke_color=RED, stroke_width=8)
        self.play(ShowCreation(cross), run_time=1.0)
        
        question = Tex("(a + b)^2 =\ ?", font_size=50, fill_color=WHITE)
        question.move_to(ORIGIN)
        self.play(
            FadeOut(cross),
            ReplacementTransform(wrong_eq, question),
            run_time=1.0
        )
        self.wait(1.5)
        self.play(FadeOut(question), run_time=0.5)
        
        # 2. Geometry Setup (Line to Square)
        sq_center = ORIGIN
        sq_left = -total / 2
        sq_right = total / 2
        sq_top = total / 2
        sq_bottom = -total / 2
        split_x = sq_left + a_val
        split_y = sq_top - a_val
        
        line = Line(
            np.array([sq_left, sq_bottom, 0]),
            np.array([sq_right, sq_bottom, 0]),
            stroke_color=BLUE, stroke_width=6
        )
        self.play(ShowCreation(line), run_time=1.0)
        
        a_brace = Brace(Line(np.array([sq_left, sq_bottom, 0]), np.array([split_x, sq_bottom, 0])), DOWN, buff=0.1)
        a_label = Tex("a", font_size=45, fill_color=TEAL).next_to(a_brace, DOWN, buff=0.1)
        
        b_brace = Brace(Line(np.array([split_x, sq_bottom, 0]), np.array([sq_right, sq_bottom, 0])), DOWN, buff=0.1)
        b_label = Tex("b", font_size=45, fill_color=GOLD).next_to(b_brace, DOWN, buff=0.1)
        
        self.play(
            GrowFromCenter(a_brace), Write(a_label),
            GrowFromCenter(b_brace), Write(b_label),
            run_time=1.0
        )
        self.wait(0.5)
        
        main_square = Square(side_length=total, stroke_color=WHITE, stroke_width=3)
        main_square.move_to(sq_center)
        self.play(Transform(line, main_square), run_time=2.0)
        self.wait(1.5)
        
        # 3. Grid Split
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
        self.play(ShowCreation(v_line), run_time=1.0)
        self.play(ShowCreation(h_line), run_time=1.0)
        self.wait(1.0)
        
        # 4. Squares (a^2, b^2)
        a_sq = Square(side_length=a_val, fill_color=TEAL, fill_opacity=0.7, stroke_width=0)
        a_sq.move_to(np.array([sq_left + a_val/2, sq_top - a_val/2, 0]))
        a_sq_label = Tex("a^2", font_size=45, fill_color=WHITE).move_to(a_sq)
        self.play(FadeIn(a_sq), Write(a_sq_label), run_time=1.5)
        
        b_sq = Square(side_length=b_val, fill_color=GOLD, fill_opacity=0.7, stroke_width=0)
        b_sq.move_to(np.array([sq_right - b_val/2, sq_bottom + b_val/2, 0]))
        b_sq_label = Tex("b^2", font_size=45, fill_color=WHITE).move_to(b_sq)
        self.play(FadeIn(b_sq), Write(b_sq_label), run_time=1.5)
        self.wait(1.0)
        
        # 5. Rectangles (ab)
        ab_rect1 = Rectangle(width=b_val, height=a_val, stroke_color=GREEN, stroke_width=2)
        ab_rect1.move_to(np.array([sq_right - b_val/2, sq_top - a_val/2, 0]))
        ab_label1 = Tex("ab", font_size=40, fill_color=WHITE).move_to(ab_rect1)
        self.play(Indicate(ab_rect1, color=RED), Write(ab_label1), run_time=1.0)
        
        ab_rect2 = Rectangle(width=a_val, height=b_val, stroke_color=GREEN, stroke_width=2)
        ab_rect2.move_to(np.array([sq_left + a_val/2, sq_bottom + b_val/2, 0]))
        ab_label2 = Tex("ab", font_size=40, fill_color=WHITE).move_to(ab_rect2)
        self.play(Indicate(ab_rect2, color=RED), Write(ab_label2), run_time=1.0)
        
        ab_rect1_fill = Rectangle(width=b_val, height=a_val, fill_color=GREEN_C, fill_opacity=0.7, stroke_width=0)
        ab_rect1_fill.move_to(ab_rect1)
        ab_rect2_fill = Rectangle(width=a_val, height=b_val, fill_color=GREEN_C, fill_opacity=0.7, stroke_width=0)
        ab_rect2_fill.move_to(ab_rect2)
        self.play(FadeIn(ab_rect1_fill), FadeIn(ab_rect2_fill), run_time=1.0)
        self.wait(1.0)
        
        # 6. Formula Assembly
        geometry = VGroup(
            line, v_line, h_line, a_brace, a_label, b_brace, b_label,
            a_sq, a_sq_label, b_sq, b_sq_label,
            ab_rect1, ab_rect2, ab_label1, ab_label2, ab_rect1_fill, ab_rect2_fill
        )
        self.play(geometry.animate.shift(UP * 1.2), run_time=0.8)
        
        eq_parts = VGroup(
            Tex("a^2", font_size=50, fill_color=TEAL),
            Tex("+", font_size=50),
            Tex("2ab", font_size=50, fill_color=GREEN_C),
            Tex("+", font_size=50),
            Tex("b^2", font_size=50, fill_color=GOLD)
        ).arrange(RIGHT, buff=0.15)
        eq_parts.next_to(geometry, DOWN, buff=0.8)
        
        self.play(TransformFromCopy(a_sq_label, eq_parts[0]), run_time=0.6)
        self.play(Write(eq_parts[1]), run_time=0.2)
        self.play(TransformFromCopy(VGroup(ab_label1, ab_label2), eq_parts[2]), run_time=0.6)
        self.play(Write(eq_parts[3]), run_time=0.2)
        self.play(TransformFromCopy(b_sq_label, eq_parts[4]), run_time=0.6)
        
        full_formula = Tex("(a + b)^2", "=", "a^2", "+", "2ab", "+", "b^2", font_size=40)
        full_formula[2].set_color(TEAL)
        full_formula[4].set_color(GREEN_C)
        full_formula[6].set_color(GOLD)
        full_formula.move_to(eq_parts)
        
        self.play(
            ReplacementTransform(eq_parts, full_formula[2:]),
            Write(full_formula[:2]),
            run_time=1.0
        )
        self.wait(2.0)
        self.play(FadeOut(geometry), FadeOut(full_formula), run_time=1.0)
        
        # 7. Example 13^2
        try_text = Text("Try this!", font_size=50, fill_color=BLUE)
        try_text.to_edge(UP, buff=1.5)
        
        num_eq = Tex("13^2 = (10 + 3)^2", font_size=50)
        num_eq.next_to(try_text, DOWN, buff=0.3)
        self.play(Write(try_text), Write(num_eq), run_time=2.0)
        
        n_sq_a = Square(side_length=2.0, fill_color=TEAL, fill_opacity=0.5, stroke_color=WHITE, stroke_width=2)
        n_sq_b = Square(side_length=1.2, fill_color=GOLD, fill_opacity=0.5, stroke_color=WHITE, stroke_width=2)
        n_rect1 = Rectangle(width=1.2, height=2.0, fill_color=GREEN_C, fill_opacity=0.5, stroke_color=WHITE, stroke_width=2)
        n_rect2 = Rectangle(width=2.0, height=1.2, fill_color=GREEN_C, fill_opacity=0.5, stroke_color=WHITE, stroke_width=2)
        
        grid_center = DOWN * 0.5
        n_sq_a.move_to(grid_center + np.array([-0.6, 0.6, 0]))
        n_rect1.move_to(grid_center + np.array([1.0, 0.6, 0]))
        n_rect2.move_to(grid_center + np.array([-0.6, -1.0, 0]))
        n_sq_b.move_to(grid_center + np.array([1.0, -1.0, 0]))
        
        num_grid = VGroup(n_sq_a, n_sq_b, n_rect1, n_rect2)
        self.play(ShowCreation(num_grid), run_time=1.0)
        
        # Braces
        brace_10 = Brace(n_rect2, DOWN, buff=0.1)
        lbl_10 = Tex("10", font_size=35).next_to(brace_10, DOWN, buff=0.1)
        brace_3 = Brace(n_sq_b, DOWN, buff=0.1)
        lbl_3 = Tex("3", font_size=35).next_to(brace_3, DOWN, buff=0.1)
        
        self.play(
            GrowFromCenter(brace_10), Write(lbl_10),
            GrowFromCenter(brace_3), Write(lbl_3),
            run_time=1.0
        )
        
        # Initial squares
        lbl_10sq = Tex("10^2", font_size=40).move_to(n_sq_a)
        lbl_3sq = Tex("3^2", font_size=35).move_to(n_sq_b)
        self.play(Write(lbl_10sq), Write(lbl_3sq), run_time=1.0)
        self.wait(0.5)
        
        # Transform to numbers
        lbl_100 = Tex("100", font_size=45).move_to(n_sq_a)
        lbl_9 = Tex("9", font_size=40).move_to(n_sq_b)
        
        self.play(
            Transform(lbl_10sq, lbl_100),
            Transform(lbl_3sq, lbl_9),
            run_time=1.0
        )
        
        lbl_30_1 = Tex("30", font_size=35).move_to(n_rect1)
        lbl_30_2 = Tex("30", font_size=35).move_to(n_rect2)
        self.play(Write(lbl_30_1), Write(lbl_30_2), run_time=1.0)
        
        sum_parts = VGroup(
            Tex("100", font_size=50, fill_color=TEAL),
            Tex("+", font_size=50),
            Tex("2(30)", font_size=50, fill_color=GREEN_C),
            Tex("+", font_size=50),
            Tex("9", font_size=50, fill_color=GOLD),
            Tex("=", font_size=50),
            Tex("169", font_size=50)
        ).arrange(RIGHT, buff=0.15)
        sum_parts.next_to(num_grid, DOWN, buff=1.0)
        
        self.play(TransformFromCopy(lbl_100, sum_parts[0]), run_time=0.6)
        self.play(Write(sum_parts[1]), run_time=0.2)
        self.play(TransformFromCopy(VGroup(lbl_30_1, lbl_30_2), sum_parts[2]), run_time=0.6)
        self.play(Write(sum_parts[3]), run_time=0.2)
        self.play(TransformFromCopy(lbl_9, sum_parts[4]), run_time=0.6)
        self.play(Write(sum_parts[5:]), run_time=0.5)
        self.wait(1.0)
        
        formula_match = VGroup(
            Tex("a^2", font_size=50, fill_color=TEAL),
            Tex("+", font_size=50),
            Tex("2ab", font_size=50, fill_color=GREEN_C),
            Tex("+", font_size=50),
            Tex("b^2", font_size=50, fill_color=GOLD)
        ).arrange(RIGHT, buff=0.15)
        formula_match.move_to(sum_parts[:5])
        formula_match.shift(RIGHT*0.7) # Align with 100 + 2(30) + 9

        self.play(
            ReplacementTransform(sum_parts[:5], formula_match),
            FadeOut(sum_parts[5:]),
            run_time=1.5
        )
        self.wait(1.0)
        
        self.play(
            FadeOut(try_text), FadeOut(num_eq), FadeOut(num_grid),
            FadeOut(lbl_10sq), FadeOut(lbl_3sq), FadeOut(lbl_30_1), FadeOut(lbl_30_2),
            FadeOut(brace_10), FadeOut(lbl_10), FadeOut(brace_3), FadeOut(lbl_3),
            FadeOut(formula_match),
            run_time=1.0
        )
        
        # 8. Challenge 21^2
        # 8. Challenge 21^2
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("21^2 = (20+1)^2", font_size=50)
        challenge_group = VGroup(c_title, c_eq).arrange(DOWN, buff=0.3)
        challenge_group.to_edge(UP, buff=2.5)
        
        self.play(Write(challenge_group), run_time=2.0)
        
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
        self.play(FadeOut(clock), FadeOut(challenge_group), run_time=1.0)
        
        # 9. CTA
        like_text = Text("LIKE", font_size=40, fill_color=TEAL)
        like_text.move_to(ORIGIN).shift(UP * 1)
        self.play(Write(like_text), run_time=0.5)
        
        share_text = Text("SHARE", font_size=40, fill_color=WHITE)
        share_text.next_to(like_text, DOWN, buff=0.5)
        self.play(TransformFromCopy(like_text, share_text), run_time=0.5)
        
        subscribe_text = Text("SUBSCRIBE", font_size=40, fill_color=RED)
        subscribe_text.next_to(share_text, DOWN, buff=0.5)
        self.play(TransformFromCopy(share_text, subscribe_text), run_time=0.5)
        self.wait(1)
        
        self.play(
            like_text.animate.shift(LEFT * 10),
            share_text.animate.shift(RIGHT * 10),
            subscribe_text.animate.shift(LEFT * 10),
            run_time=0.5,
            lag_ratio=0.1
        )
        self.wait(1)
