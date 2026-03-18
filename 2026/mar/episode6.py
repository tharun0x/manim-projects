from manimlib import *

class Episode6(Scene):
    def construct(self):
        # Watermark
        # watermark = Text("@tharun0x", font="Arial", font_size=15, fill_color=WHITE)
        # watermark.set_opacity(0.2)
        # watermark.to_edge(DOWN, buff=1).to_edge(RIGHT, buff=0.5)
        # self.add(watermark)

        # =================================================================
        # SECTION 1: HOOK
        # =================================================================
        problem = Tex("99 \\times 56 \\ = \\ ?", font_size=50)
        problem.move_to(ORIGIN)
        self.play(Write(problem), run_time=2)
        self.wait(2)

        hard_text = Text("Forget long\nmultiplication", font_size=30, fill_color=RED)
        hard_text.next_to(problem, DOWN, buff=0.6)
        self.play(Write(hard_text), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(problem), FadeOut(hard_text), run_time=1.5)

        # =================================================================
        # SECTION 2: THE TRICK (dense — 6 items)
        # =================================================================
        trick_title = Text("The Trick", font_size=40, fill_color=TEAL)
        trick_title.to_edge(UP, buff=1.5)
        self.play(Write(trick_title), run_time=1.5)
        self.wait(2)

        rule = Tex("99 \\times N \\ = \\ 100N - N", font_size=45, fill_color=TEAL)
        rule.next_to(trick_title, DOWN, buff=0.5)
        self.play(Write(rule), run_time=2)
        self.wait(2)

        # Demo: 99 × 56 — with all intermediary steps
        s1 = Tex("99 \\times 56", font_size=45)
        s1.next_to(rule, DOWN, buff=0.8)
        self.play(Write(s1), run_time=1.5)
        self.wait(2)

        # Intermediary: apply the rule
        s2 = Tex("= \\ 100 \\times 56 - 56", font_size=45)
        s2.next_to(s1, DOWN, buff=0.5)
        self.play(Write(s2), run_time=1.5)
        self.wait(2)

        # Simplify
        s3 = Tex("= \\ 5600 - 56", font_size=45)
        s3.next_to(s2, DOWN, buff=0.5)
        self.play(Write(s3), run_time=1.5)
        self.wait(2)

        # Final answer — separate line, highlighted
        s4 = Tex("= \\ 5544", font_size=50, fill_color=GREEN_C)
        s4.next_to(s3, DOWN, buff=0.5)
        self.play(Write(s4), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(trick_title), FadeOut(rule),
            FadeOut(s1), FadeOut(s2), FadeOut(s3), FadeOut(s4),
            run_time=1.5
        )

        # =================================================================
        # SECTION 3: MORE EXAMPLES (light — cycling 3 items)
        # =================================================================
        more = Text("More\nExamples", font_size=40, fill_color=TEAL)
        more.to_edge(UP, buff=2.5)
        self.play(Write(more), run_time=1.5)
        self.wait(2)

        # Example 2: 99 × 23
        e2a = Tex("99 \\times 23", font_size=45)
        e2a.next_to(more, DOWN, buff=0.5)
        self.play(Write(e2a), run_time=1.5)
        self.wait(2)

        e2b = Tex("= \\ 2300 - 23", font_size=45)
        e2b.next_to(e2a, DOWN, buff=0.5)
        self.play(Write(e2b), run_time=1.5)
        self.wait(2)

        e2c = Tex("= \\ 2277", font_size=50, fill_color=GREEN_C)
        e2c.next_to(e2b, DOWN, buff=0.5)
        self.play(Write(e2c), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(e2a), FadeOut(e2b), FadeOut(e2c), run_time=1.5)

        # Example 3: 99 × 78
        e3a = Tex("99 \\times 78", font_size=45)
        e3a.next_to(more, DOWN, buff=0.5)
        self.play(Write(e3a), run_time=1.5)
        self.wait(2)

        e3b = Tex("= \\ 7800 - 78", font_size=45)
        e3b.next_to(e3a, DOWN, buff=0.5)
        self.play(Write(e3b), run_time=1.5)
        self.wait(2)

        e3c = Tex("= \\ 7722", font_size=50, fill_color=GREEN_C)
        e3c.next_to(e3b, DOWN, buff=0.5)
        self.play(Write(e3c), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(e3a), FadeOut(e3b), FadeOut(e3c), FadeOut(more), run_time=1.5)

        # =================================================================
        # SECTION 4: WHY IT WORKS (dense — 4 items)
        # =================================================================
        why = Text("Why does this\nwork?", font_size=40, fill_color=TEAL)
        why.to_edge(UP, buff=1.5)
        self.play(Write(why), run_time=1.5)
        self.wait(2)

        w1 = Tex("99 \\ = \\ 100 - 1", font_size=45)
        w1.next_to(why, DOWN, buff=0.5)
        self.play(Write(w1), run_time=1.5)
        self.wait(2)

        w2 = Tex("99 \\times N \\ = \\ (100 - 1) \\times N", font_size=40)
        w2.next_to(w1, DOWN, buff=0.5)
        self.play(Write(w2), run_time=1.5)
        self.wait(2)

        w3 = Tex("= \\ 100N - N", font_size=45, fill_color=TEAL)
        w3.next_to(w2, DOWN, buff=0.5)
        self.play(Write(w3), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(why), FadeOut(w1), FadeOut(w2), FadeOut(w3), run_time=1.5)

        # =================================================================
        # SECTION 5: CHALLENGE — 99 × 87
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("99 \\times 87 \\ = \\ ?", font_size=50)
        challenge_group = VGroup(c_title, c_eq).arrange(DOWN, buff=0.3)
        challenge_group.to_edge(UP, buff=2.5)

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
