from manimlib import *

class Episode16(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK
        # =================================================================
        frac_l = Tex("\\frac{31}{37}", font_size=55)
        vs = Text("vs", font_size=35, fill_color=TEAL)
        frac_r = Tex("\\frac{64}{73}", font_size=55)
        hook_row = VGroup(frac_l, vs, frac_r).arrange(RIGHT, buff=0.6)
        hook_row.move_to(ORIGIN + UP * 0.5)
        self.play(Write(hook_row), run_time=1.5)
        self.wait(1)

        hook_q = Text("Which is BIGGER?", font_size=38, fill_color=RED)
        hook_q.next_to(hook_row, DOWN, buff=0.5)
        self.play(Write(hook_q), run_time=1)
        self.wait(2)

        self.play(FadeOut(hook_row), FadeOut(hook_q), run_time=1)

        # =================================================================
        # SECTION 2: THE TRICK — Gap Method (equal gaps)
        # =================================================================
        rule_title = Text("The Gap Method", font_size=40, fill_color=TEAL)
        rule_title.to_edge(UP, buff=1.5)
        self.play(Write(rule_title), run_time=1)
        self.wait(1)

        rule = Tex("\\text{Gap} = \\text{Denominator} - \\text{Numerator}", font_size=32)
        rule.next_to(rule_title, DOWN, buff=0.4)
        self.play(Write(rule), run_time=1)
        self.wait(1.5)

        # Simple case: equal gaps
        f1 = Tex("\\frac{7}{9}", font_size=45)
        g1 = Tex("\\text{gap} = 2", font_size=28, fill_color=TEAL)
        f2 = Tex("\\frac{11}{13}", font_size=45)
        g2 = Tex("\\text{gap} = 2", font_size=28, fill_color=TEAL)
        vs2 = Text("vs", font_size=28, fill_color=WHITE)

        f1.next_to(rule, DOWN, buff=0.5).shift(LEFT * 1.5)
        g1.next_to(f1, DOWN, buff=0.15)
        f2.next_to(rule, DOWN, buff=0.5).shift(RIGHT * 1.5)
        g2.next_to(f2, DOWN, buff=0.15)
        vs2.move_to((f1.get_center() + f2.get_center()) / 2 + DOWN * 0.1)

        self.play(Write(f1), Write(f2), Write(vs2), run_time=1)
        self.play(Write(g1), Write(g2), run_time=1)
        self.wait(1)

        same_rule = Text("Same gap? Bigger\nnumerator wins!", font_size=25, fill_color=GREEN_C)
        same_rule.next_to(g1, DOWN, buff=0.4).shift(RIGHT * 1.5)
        self.play(Write(same_rule), run_time=1)
        self.wait(1)

        ans1 = Tex("\\frac{11}{13} > \\frac{7}{9}", font_size=40, fill_color=GREEN_C)
        ans1.next_to(same_rule, DOWN, buff=0.3)
        self.play(Write(ans1), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(f1), FadeOut(f2), FadeOut(vs2),
            FadeOut(g1), FadeOut(g2), FadeOut(same_rule), FadeOut(ans1),
            run_time=1
        )

        # Different gaps case
        diff_title = Text("Different gaps?\nEqualize them!", font_size=28, fill_color=RED)
        diff_title.next_to(rule, DOWN, buff=0.4)
        self.play(Write(diff_title), run_time=1)
        self.wait(1)

        d1 = Tex("\\frac{31}{37}", font_size=40)
        dg1 = Tex("\\text{gap} = 6", font_size=25, fill_color=TEAL)
        d2 = Tex("\\frac{64}{73}", font_size=40)
        dg2 = Tex("\\text{gap} = 9", font_size=25, fill_color=TEAL)

        d1.next_to(diff_title, DOWN, buff=0.4).shift(LEFT * 1.5)
        dg1.next_to(d1, DOWN, buff=0.1)
        d2.next_to(diff_title, DOWN, buff=0.4).shift(RIGHT * 1.5)
        dg2.next_to(d2, DOWN, buff=0.1)

        self.play(Write(d1), Write(d2), run_time=0.8)
        self.play(Write(dg1), Write(dg2), run_time=0.8)
        self.wait(1)

        lcm_text = Tex("\\text{LCM}(6, 9) = 18", font_size=28, fill_color=TEAL)
        lcm_text.next_to(dg1, DOWN, buff=0.3).shift(RIGHT * 1.5)
        self.play(Write(lcm_text), run_time=0.8)
        self.wait(1)

        eq1 = Tex("\\frac{93}{111}", font_size=35)
        eq2 = Tex("\\frac{128}{146}", font_size=35)
        eq1.next_to(lcm_text, DOWN, buff=0.3).shift(LEFT * 1.5)
        eq2.next_to(lcm_text, DOWN, buff=0.3).shift(RIGHT * 1.5)
        self.play(Write(eq1), Write(eq2), run_time=1)
        self.wait(1)

        ans2 = Tex("128 > 93 \\to \\frac{64}{73} \\text{ wins!}", font_size=30, fill_color=GREEN_C)
        ans2.next_to(eq1, DOWN, buff=0.3).shift(RIGHT * 1.5)
        self.play(Write(ans2), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(rule_title), FadeOut(rule), FadeOut(diff_title),
            FadeOut(d1), FadeOut(d2), FadeOut(dg1), FadeOut(dg2),
            FadeOut(lcm_text), FadeOut(eq1), FadeOut(eq2), FadeOut(ans2),
            run_time=1
        )

        # =================================================================
        # SECTION 3: EXAMPLE
        # =================================================================
        ex_title = Text("Example", font_size=40, fill_color=TEAL)
        ex_title.to_edge(UP, buff=2)
        self.play(Write(ex_title), run_time=1)
        self.wait(0.5)

        ex_prob = Tex("\\frac{5}{8} \\text{ vs } \\frac{7}{11}", font_size=42)
        ex_prob.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(ex_prob), run_time=1)
        self.wait(1)

        ex_gaps = Tex("\\text{gaps: } 3 \\text{ vs } 4, \\quad \\text{LCM} = 12", font_size=30, fill_color=TEAL)
        ex_gaps.next_to(ex_prob, DOWN, buff=0.4)
        self.play(Write(ex_gaps), run_time=1)
        self.wait(1)

        ex_eq = Tex("\\frac{20}{32} \\quad \\text{vs} \\quad \\frac{21}{33}", font_size=38)
        ex_eq.next_to(ex_gaps, DOWN, buff=0.4)
        self.play(Write(ex_eq), run_time=1)
        self.wait(1)

        ex_ans = Tex("21 > 20 \\to \\frac{7}{11} \\text{ wins!}", font_size=35, fill_color=GREEN_C)
        ex_ans.next_to(ex_eq, DOWN, buff=0.4)
        self.play(Write(ex_ans), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(ex_title), FadeOut(ex_prob),
            FadeOut(ex_gaps), FadeOut(ex_eq), FadeOut(ex_ans),
            run_time=1
        )

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("\\frac{13}{17} \\text{ vs } \\frac{19}{24} = \\ ?", font_size=42)
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
