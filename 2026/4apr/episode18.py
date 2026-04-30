from manimlib import *

class Episode18(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK
        # =================================================================
        hook1 = Tex("347 \\times 28 = 9716", font_size=45)
        hook1.move_to(ORIGIN + UP * 0.5)
        self.play(Write(hook1), run_time=1.5)
        self.wait(1)

        hook_q = Text("Right or Wrong?", font_size=42, fill_color=RED)
        hook_q.next_to(hook1, DOWN, buff=0.4)
        self.play(Write(hook_q), run_time=1)
        self.wait(1)

        hook2 = Text("I can verify WITHOUT\nrecalculating.", font_size=30, fill_color=TEAL)
        hook2.next_to(hook_q, DOWN, buff=0.3)
        self.play(Write(hook2), run_time=1)
        self.wait(2)

        self.play(FadeOut(hook1), FadeOut(hook_q), FadeOut(hook2), run_time=1)

        # =================================================================
        # SECTION 2: THE TRICK — Digit Sum (Casting Out 9s)
        # =================================================================
        title = Text("Digit Sum Check", font_size=40, fill_color=TEAL)
        title.to_edge(UP, buff=1.5)
        self.play(Write(title), run_time=1)
        self.wait(1)

        rule = Text("Add all digits until\nyou get a single digit", font_size=28)
        rule.next_to(title, DOWN, buff=0.3)
        self.play(Write(rule), run_time=1)
        self.wait(1.5)

        # Digit sum of 347
        ds1_a = Tex("347 \\to 3+4+7 = 14 \\to 1+4 = \\mathbf{5}", font_size=30)
        ds1_a.next_to(rule, DOWN, buff=0.5)
        self.play(Write(ds1_a), run_time=1.5)
        self.wait(1)

        # Digit sum of 28
        ds1_b = Tex("28 \\to 2+8 = 10 \\to 1+0 = \\mathbf{1}", font_size=30)
        ds1_b.next_to(ds1_a, DOWN, buff=0.3)
        self.play(Write(ds1_b), run_time=1.5)
        self.wait(1)

        # Multiply digit sums
        ds_mult = Tex("5 \\times 1 = \\mathbf{5}", font_size=35, fill_color=BLUE)
        ds_mult.next_to(ds1_b, DOWN, buff=0.4)
        self.play(Write(ds_mult), run_time=1)
        self.wait(1)

        # Digit sum of answer
        ds_ans = Tex("9716 \\to 9+7+1+6 = 23 \\to 2+3 = \\mathbf{5}", font_size=30)
        ds_ans.next_to(ds_mult, DOWN, buff=0.4)
        self.play(Write(ds_ans), run_time=1.5)
        self.wait(1)

        # Match!
        match = Tex("5 = 5 \\quad \\checkmark \\text{ CORRECT!}", font_size=38, fill_color=GREEN_C)
        match.next_to(ds_ans, DOWN, buff=0.4)
        self.play(Write(match), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(rule),
            FadeOut(ds1_a), FadeOut(ds1_b),
            FadeOut(ds_mult), FadeOut(ds_ans), FadeOut(match),
            run_time=1
        )

        # Warning
        warn = Text("If they DON'T match", font_size=35)
        warn.move_to(ORIGIN + UP * 0.3)
        self.play(Write(warn), run_time=1)

        warn2 = Text("DEFINITELY WRONG!", font_size=42, fill_color=RED)
        warn2.next_to(warn, DOWN, buff=0.4)
        self.play(Write(warn2), run_time=1)
        self.wait(2)

        self.play(FadeOut(warn), FadeOut(warn2), run_time=1)

        # =================================================================
        # SECTION 3: EXAMPLE
        # =================================================================
        ex_title = Text("Example", font_size=40, fill_color=TEAL)
        ex_title.to_edge(UP, buff=2)
        self.play(Write(ex_title), run_time=1)
        self.wait(0.5)

        ex_prob = Tex("123 \\times 45 = 5535", font_size=40)
        ex_prob.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(ex_prob), run_time=1)
        self.wait(1)

        ex1 = Tex("123 \\to 6, \\quad 45 \\to 9", font_size=32)
        ex1.next_to(ex_prob, DOWN, buff=0.4)
        self.play(Write(ex1), run_time=1)
        self.wait(0.5)

        ex2 = Tex("6 \\times 9 = 54 \\to 9", font_size=35, fill_color=BLUE)
        ex2.next_to(ex1, DOWN, buff=0.3)
        self.play(Write(ex2), run_time=1)
        self.wait(0.5)

        ex3 = Tex("5535 \\to 18 \\to 9", font_size=32)
        ex3.next_to(ex2, DOWN, buff=0.3)
        self.play(Write(ex3), run_time=1)
        self.wait(0.5)

        ex_match = Tex("9 = 9 \\quad \\checkmark", font_size=40, fill_color=GREEN_C)
        ex_match.next_to(ex3, DOWN, buff=0.4)
        self.play(Write(ex_match), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(ex_title), FadeOut(ex_prob),
            FadeOut(ex1), FadeOut(ex2), FadeOut(ex3), FadeOut(ex_match),
            run_time=1
        )

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("246 \\times 13 = \\ ?", font_size=45)
        c_hint = Text("Solve & verify with\ndigit sums!", font_size=28)
        challenge_group = VGroup(c_title, c_eq, c_hint).arrange(DOWN, buff=0.3)
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
