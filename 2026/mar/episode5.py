from manimlib import *

class Episode5(Scene):
    def construct(self):
        # Watermark
        # watermark = Text("@tharun0x", font="Arial", font_size=15, fill_color=WHITE)
        # watermark.set_opacity(0.2)
        # watermark.to_edge(DOWN, buff=1).to_edge(RIGHT, buff=0.5)
        # self.add(watermark)

        # =================================================================
        # SECTION 1: HOOK
        # =================================================================
        problem = Tex("8", "\\%", " \\text{ of } ", "25", " \\ = \\ ?", font_size=50)
        problem.move_to(ORIGIN)
        self.play(Write(problem), run_time=2)
        self.wait(2)

        hard_text = Text("Most people grab a\n calculator", font_size=30, fill_color=RED)
        hard_text.next_to(problem, DOWN, buff=0.6)
        self.play(Write(hard_text), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(problem), FadeOut(hard_text), run_time=1.5)

        # =================================================================
        # SECTION 2: THE TRICK
        # =================================================================
        secret = Text("The Secret", font_size=40, fill_color=TEAL)
        secret.to_edge(UP, buff=2.5)
        self.play(Write(secret), run_time=1.5)
        self.wait(2)

        rule = Tex(
            "X", "\\%", " \\text{ of } ", "Y",
            " \\ = \\ ",
            "Y", "\\%", " \\text{ of } ", "X",
            font_size=45
        )
        rule[0].set_color(TEAL)   # X
        rule[4].set_color(GOLD)   # Y
        rule[6].set_color(GOLD)   # Y
        rule[10].set_color(TEAL)   # X
        rule.next_to(secret, DOWN, buff=0.5)
        self.play(Write(rule), run_time=2)
        self.wait(2)

        # Demo: 8% of 25 = 25% of 8
        demo_left = Tex("8\\% \\text{ of } 25", font_size=45)
        demo_eq = Tex("=", font_size=45)
        demo_right = Tex("25\\% \\text{ of } 8", font_size=45)

        demo = VGroup(demo_left, demo_eq, demo_right).arrange(RIGHT, buff=0.2)
        demo.next_to(rule, DOWN, buff=0.8)
        self.play(Write(demo), run_time=2)
        self.wait(2)

        # Solution
        sol = Tex(
            "= \\ \\frac{1}{4} \\times 8 \\ = \\ 2",
            font_size=45, fill_color=GREEN_C
        )
        sol.next_to(demo, DOWN, buff=0.5)
        self.play(Write(sol), run_time=2)
        self.wait(2)

        self.play(FadeOut(secret), FadeOut(rule), FadeOut(demo), FadeOut(sol), run_time=1.5)

        # =================================================================
        # SECTION 3: MORE EXAMPLES
        # =================================================================
        more = Text("More\nExamples", font_size=40, fill_color=TEAL)
        more.to_edge(UP, buff=2.5)
        self.play(Write(more), run_time=1.5)
        self.wait(2)

        # Example 2: 4% of 75
        ex2 = Tex("4\\% \\text{ of } 75 \\ = \\ ?", font_size=45)
        ex2.next_to(more, DOWN, buff=0.5)
        self.play(Write(ex2), run_time=1.5)
        self.wait(2)

        ex2_sol = Tex("= \\ 75\\% \\text{ of } 4 \\ = \\ 3", font_size=45, fill_color=GREEN_C)
        ex2_sol.next_to(ex2, DOWN, buff=0.4)
        self.play(Write(ex2_sol), run_time=2)
        self.wait(2)

        self.play(FadeOut(ex2), FadeOut(ex2_sol), run_time=1.5)

        # Example 3: 2% of 50
        ex3 = Tex("2\\% \\text{ of } 50 \\ = \\ ?", font_size=45)
        ex3.next_to(more, DOWN, buff=0.5)
        self.play(Write(ex3), run_time=1.5)
        self.wait(2)

        ex3_sol = Tex("= \\ 50\\% \\text{ of } 2 \\ = \\ 1", font_size=45, fill_color=GREEN_C)
        ex3_sol.next_to(ex3, DOWN, buff=0.4)
        self.play(Write(ex3_sol), run_time=2)
        self.wait(2)

        self.play(FadeOut(more), FadeOut(ex3), FadeOut(ex3_sol), run_time=1.5)

        # =================================================================
        # SECTION 4: WHY IT WORKS
        # =================================================================
        why = Text("Why does this\nwork?", font_size=40, fill_color=TEAL)
        why.to_edge(UP, buff=1.5)
        self.play(Write(why), run_time=1.5)
        self.wait(2)

        p1 = Tex("X\\% \\text{ of } Y \\ = \\ \\frac{X}{100} \\times Y", font_size=40)
        p1.next_to(why, DOWN, buff=0.5)
        self.play(Write(p1), run_time=2)
        self.wait(2)

        p2 = Tex("= \\ \\frac{X \\times Y}{100}", font_size=40)
        p2.next_to(p1, DOWN, buff=0.5)
        self.play(Write(p2), run_time=1.5)
        self.wait(2)

        p3 = Tex("= \\ \\frac{Y}{100} \\times X", font_size=40)
        p3.next_to(p2, DOWN, buff=0.5)
        self.play(Write(p3), run_time=1.5)
        self.wait(2)

        p4 = Tex("= \\ Y\\% \\text{ of } X", font_size=40, fill_color=TEAL)
        p4.next_to(p3, DOWN, buff=0.5)
        self.play(Write(p4), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(why), FadeOut(p1), FadeOut(p2), FadeOut(p3), FadeOut(p4), run_time=1.5)

        # =================================================================
        # SECTION 5: CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("15\\% \\text{ of } 40 \\ = \\ ?", font_size=50)
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
