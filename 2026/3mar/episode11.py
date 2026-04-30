from manimlib import *

class Episode11(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK (light)
        # =================================================================
        problem = Tex("225 \\divisionsymbol 5 \\ = \\ ?", font_size=50)
        problem.move_to(ORIGIN)
        self.play(Write(problem), run_time=2)
        self.wait(2)

        self.play(FadeOut(problem), run_time=1)

        # =================================================================
        # SECTION 2: THE TRICK (dense)
        # =================================================================
        trick_title = Text("The Trick", font_size=40, fill_color=TEAL)
        trick_title.to_edge(UP, buff=2)
        self.play(Write(trick_title), run_time=1.5)
        self.wait(2)

        # Show the transformation: 225 ÷ 5 → 225 × 2 ÷ 10
        step1 = Tex("225 \\divisionsymbol 5", font_size=45)
        step1.next_to(trick_title, DOWN, buff=0.5)
        self.play(Write(step1), run_time=1.5)
        self.wait(2)

        step2 = Tex("225 \\times 2 \\divisionsymbol 10", font_size=45)
        step2.next_to(step1, DOWN, buff=0.5)
        self.play(TransformFromCopy(step1, step2), run_time=1.5)
        self.wait(2)

        step3 = Tex("= \\ 450 \\divisionsymbol 10", font_size=45)
        step3.next_to(step2, DOWN, buff=0.5)
        self.play(Write(step3), run_time=1)
        self.wait(2)

        ans1 = Tex("= \\ 45", font_size=50, fill_color=GREEN_C)
        ans1.next_to(step3, DOWN, buff=0.5)
        self.play(Write(ans1), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(trick_title), FadeOut(step1), FadeOut(step2), FadeOut(step3), FadeOut(ans1),
            run_time=1
        )

        # Why it works
        why_title = Text("Why?", font_size=40, fill_color=TEAL)
        why_title.to_edge(UP, buff=2.5)
        self.play(Write(why_title), run_time=1)
        self.wait(2)

        reason1 = Tex("5 \\ = \\ \\frac{10}{2}", font_size=45)
        reason1.next_to(why_title, DOWN, buff=0.5)
        self.play(Write(reason1), run_time=1.5)
        self.wait(2)

        reason2 = Tex("\\divisionsymbol 5 \\ = \\ \\times 2 \\divisionsymbol 10", font_size=45, fill_color=GREEN_C)
        reason2.next_to(reason1, DOWN, buff=0.5)
        self.play(Write(reason2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(why_title), FadeOut(reason1), FadeOut(reason2), run_time=1)

        # =================================================================
        # SECTION 3: FOR 25 AND 125
        # =================================================================
        ext_title = Text("Works for 25\nand 125 too", font_size=35, fill_color=TEAL)
        ext_title.to_edge(UP, buff=3)
        self.play(Write(ext_title), run_time=1.5)
        self.wait(2)

        rule25 = Tex("\\divisionsymbol 25 \\ = \\ \\times 4 \\divisionsymbol 100", font_size=42)
        rule25.next_to(ext_title, DOWN, buff=0.5)
        self.play(Write(rule25), run_time=1.5)
        self.wait(2)

        rule125 = Tex("\\divisionsymbol 125 \\ = \\ \\times 8 \\divisionsymbol 1000", font_size=42)
        rule125.next_to(rule25, DOWN, buff=0.5)
        self.play(Write(rule125), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(ext_title), FadeOut(rule25), FadeOut(rule125),
            run_time=1
        )

        # =================================================================
        # SECTION 4: EXAMPLE (1 only)
        # =================================================================
        ex_title = Text("Example", font_size=40, fill_color=TEAL)
        ex_title.to_edge(UP, buff=2)
        self.play(Write(ex_title), run_time=1)
        self.wait(2)

        ex1 = Tex("1750 \\divisionsymbol 25", font_size=45)
        ex1.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(ex1), run_time=1.5)
        self.wait(2)

        ex2 = Tex("1750 \\times 4 \\divisionsymbol 100", font_size=45)
        ex2.next_to(ex1, DOWN, buff=0.5)
        self.play(TransformFromCopy(ex1, ex2), run_time=1.5)
        self.wait(2)

        ex3 = Tex("= \\ 7000 \\divisionsymbol 100", font_size=45)
        ex3.next_to(ex2, DOWN, buff=0.5)
        self.play(Write(ex3), run_time=1)
        self.wait(2)

        ex_ans = Tex("= \\ 70", font_size=50, fill_color=GREEN_C)
        ex_ans.next_to(ex3, DOWN, buff=0.5)
        self.play(Write(ex_ans), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(ex_title), FadeOut(ex1), FadeOut(ex2), FadeOut(ex3), FadeOut(ex_ans),
            run_time=1
        )

        # =================================================================
        # SECTION 5: CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("4500 \\divisionsymbol 125 \\ = \\ ?", font_size=50)
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
