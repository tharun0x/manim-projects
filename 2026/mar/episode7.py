from manimlib import *

class Episode7(Scene):
    def construct(self):
        # Watermark
        # watermark = Text("@tharun0x", font="Arial", font_size=15, fill_color=WHITE)
        # watermark.set_opacity(0.2)
        # watermark.to_edge(DOWN, buff=1).to_edge(RIGHT, buff=0.5)
        # self.add(watermark)

        # =================================================================
        # SECTION 1: HOOK
        # =================================================================
        hook1 = Text("Your money at\n8% interest", font_size=35)
        hook1.to_edge(UP, buff=1.5)
        hook2 = Text("How many years\nto double?", font_size=40, fill_color=RED)
        hook2.next_to(hook1, DOWN, buff=0.5)
        self.play(Write(hook1), run_time=1.5)
        self.wait(2)
        self.play(Write(hook2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(hook1), FadeOut(hook2), run_time=1.5)

        # =================================================================
        # SECTION 2: THE RULE (dense — 5 items)
        # =================================================================
        title = Text("Rule of 72", font_size=45, fill_color=TEAL)
        title.to_edge(UP, buff=1.5)
        self.play(Write(title), run_time=1.5)
        self.wait(2)

        formula = Tex(
            "\\text{Years} \\ = \\ \\frac{72}{\\text{Rate}}",
            font_size=45, fill_color=TEAL
        )
        formula.next_to(title, DOWN, buff=0.5)
        self.play(Write(formula), run_time=2)
        self.wait(2)

        # Demo: 8% — step by step
        demo_step = Tex("= \\ \\frac{72}{8}", font_size=45)
        demo_step.next_to(formula, DOWN, buff=0.5)
        self.play(Write(demo_step), run_time=1.5)
        self.wait(2)

        # Final answer — separate line, highlighted
        demo_ans = Tex("= \\ 9 \\text{ years}", font_size=50, fill_color=GREEN_C)
        demo_ans.next_to(demo_step, DOWN, buff=0.5)
        self.play(Write(demo_ans), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(title), FadeOut(formula),
            FadeOut(demo_step), FadeOut(demo_ans),
            run_time=1.5
        )

        # =================================================================
        # SECTION 3: MORE EXAMPLES (light — cycling 3 items)
        # =================================================================
        more = Text("More\nExamples", font_size=40, fill_color=TEAL)
        more.to_edge(UP, buff=2)
        self.play(Write(more), run_time=1.5)
        self.wait(2)

        # Example 1: FD at 6%
        e1_title = Text("Fixed Deposit\nat 6%", font_size=35, fill_color=WHITE)
        e1_title.next_to(more, DOWN, buff=0.5)
        self.play(Write(e1_title), run_time=1.5)
        self.wait(2)

        e1_step = Tex("\\frac{72}{6}", font_size=45)
        e1_step.next_to(e1_title, DOWN, buff=0.5)
        self.play(Write(e1_step), run_time=1.5)
        self.wait(2)

        e1_ans = Tex("= \\ 12 \\text{ years}", font_size=50, fill_color=GREEN_C)
        e1_ans.next_to(e1_step, DOWN, buff=0.5)
        self.play(Write(e1_ans), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(e1_title), FadeOut(e1_step), FadeOut(e1_ans), run_time=1.5)

        # Example 2: Mutual Fund at 12%
        e2_title = Text("Mutual Fund\nat 12%", font_size=35, fill_color=WHITE)
        e2_title.next_to(more, DOWN, buff=0.5)
        self.play(Write(e2_title), run_time=1.5)
        self.wait(2)

        e2_step = Tex("\\frac{72}{12}", font_size=45)
        e2_step.next_to(e2_title, DOWN, buff=0.5)
        self.play(Write(e2_step), run_time=1.5)
        self.wait(2)

        e2_ans = Tex("= \\ 6 \\text{ years}", font_size=50, fill_color=GREEN_C)
        e2_ans.next_to(e2_step, DOWN, buff=0.5)
        self.play(Write(e2_ans), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(e2_title), FadeOut(e2_step), FadeOut(e2_ans), FadeOut(more), run_time=1.5)

        # =================================================================
        # CAVEAT — Rule of 72 is approximate
        # =================================================================
        caveat_title = Text("One caveat", font_size=40, fill_color=RED)
        caveat_title.to_edge(UP, buff=2.5)
        self.play(Write(caveat_title), run_time=1.5)
        self.wait(2)

        caveat1 = Text("This is an\napproximation", font_size=35)
        caveat1.next_to(caveat_title, DOWN, buff=0.5)
        self.play(Write(caveat1), run_time=1.5)
        self.wait(2)

        caveat2 = Text("Works best for\n6% to 10% rates", font_size=35, fill_color=TEAL)
        caveat2.next_to(caveat1, DOWN, buff=0.5)
        self.play(Write(caveat2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(caveat_title), FadeOut(caveat1), FadeOut(caveat2), run_time=1.5)

        # =================================================================
        # SECTION 4: REVERSE (dense — 5 items)
        # =================================================================
        rev = Text("Reverse it!", font_size=40, fill_color=TEAL)
        rev.to_edge(UP, buff=1.5)
        self.play(Write(rev), run_time=1.5)
        self.wait(2)

        rev_formula = Tex(
            "\\text{Rate} \\ = \\ \\frac{72}{\\text{Years}}",
            font_size=45, fill_color=TEAL
        )
        rev_formula.next_to(rev, DOWN, buff=0.5)
        self.play(Write(rev_formula), run_time=2)
        self.wait(2)

        # Double in 3 years
        r1 = Text("Double in\n3 years?", font_size=40)
        r1.next_to(rev_formula, DOWN, buff=0.5)
        self.play(Write(r1), run_time=1.5)
        self.wait(2)

        r1_step = Tex("\\frac{72}{3}", font_size=45)
        r1_step.next_to(r1, DOWN, buff=0.5)
        self.play(Write(r1_step), run_time=1.5)
        self.wait(2)

        r1_ans = Tex("= \\ 24\\%", font_size=50, fill_color=RED)
        r1_ans.next_to(r1_step, DOWN, buff=0.5)
        self.play(Write(r1_ans), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(r1), FadeOut(r1_step), FadeOut(r1_ans), run_time=1.5)

        self.play(
            FadeOut(rev), FadeOut(rev_formula),
            run_time=1.5
        )

        # =================================================================
        # SECTION 5: CHALLENGE — PPF at 7.1%
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("\\text{PPF at } 7.2\\%", font_size=40)
        c_eq2 = Text("Years to\ndouble?", font_size=40)
        challenge_group = VGroup(c_title, c_eq, c_eq2).arrange(DOWN, buff=0.3)
        challenge_group.to_edge(UP, buff=2.0)

        self.play(Write(challenge_group), run_time=2)
        self.wait(2)

        # Standard analog clock timer
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
        # SECTION 6: CTA (standard)
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
