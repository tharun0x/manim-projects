from manimlib import *

class Episode14(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK — bold provocative statement
        # =================================================================
        hook1 = Tex("5^0 = 1", font_size=70)
        hook1.move_to(ORIGIN + UP * 0.5)
        self.play(Write(hook1), run_time=1.5)
        self.wait(1)

        hook2 = Text("WHY?!", font_size=50, fill_color=RED)
        hook2.next_to(hook1, DOWN, buff=0.4)
        self.play(Write(hook2), run_time=1)
        self.wait(2)

        self.play(FadeOut(hook1), FadeOut(hook2), run_time=1)

        # =================================================================
        # SECTION 2: THE PATTERN — descending powers
        # =================================================================
        # Build the pattern vertically with arrows between
        spacing = 0.7
        start_y = 2.8

        p4 = Tex("5^4 = 625", font_size=38)
        p4.move_to(np.array([0, start_y, 0]))
        self.play(Write(p4), run_time=1)
        self.wait(1)

        # Arrow + "divide by 5" label
        arr1 = Tex("\\downarrow \\divisionsymbol 5", font_size=28, fill_color=TEAL)
        arr1.next_to(p4, DOWN, buff=0.15)
        self.play(Write(arr1), run_time=0.5)

        p3 = Tex("5^3 = 125", font_size=38)
        p3.next_to(arr1, DOWN, buff=0.15)
        self.play(Write(p3), run_time=0.8)
        self.wait(1)

        arr2 = Tex("\\downarrow \\divisionsymbol 5", font_size=28, fill_color=TEAL)
        arr2.next_to(p3, DOWN, buff=0.15)
        self.play(Write(arr2), run_time=0.5)

        p2 = Tex("5^2 = 25", font_size=38)
        p2.next_to(arr2, DOWN, buff=0.15)
        self.play(Write(p2), run_time=0.8)
        self.wait(1)

        arr3 = Tex("\\downarrow \\divisionsymbol 5", font_size=28, fill_color=TEAL)
        arr3.next_to(p2, DOWN, buff=0.15)
        self.play(Write(arr3), run_time=0.5)

        p1 = Tex("5^1 = 5", font_size=38)
        p1.next_to(arr3, DOWN, buff=0.15)
        self.play(Write(p1), run_time=0.8)
        self.wait(1)

        arr4 = Tex("\\downarrow \\divisionsymbol 5", font_size=28, fill_color=TEAL)
        arr4.next_to(p1, DOWN, buff=0.15)
        self.play(Write(arr4), run_time=0.5)

        p0_q = Tex("5^0 = \\ ?", font_size=38)
        p0_q.next_to(arr4, DOWN, buff=0.15)
        self.play(Write(p0_q), run_time=0.8)
        self.wait(2)

        # Reveal: 5 ÷ 5 = 1
        reveal = Tex("5 \\divisionsymbol 5 = 1", font_size=35, fill_color=BLUE)
        reveal.next_to(p0_q, DOWN, buff=0.4)
        self.play(Write(reveal), run_time=1)
        self.wait(1)

        # Transform ? to 1
        p0_ans = Tex("5^0 = 1", font_size=38, fill_color=RED)
        p0_ans.move_to(p0_q.get_center())
        self.play(Transform(p0_q, p0_ans), run_time=1)
        self.wait(2)

        # Fade everything
        all_pattern = VGroup(p4, arr1, p3, arr2, p2, arr3, p1, arr4, p0_q, reveal)
        self.play(FadeOut(all_pattern), run_time=1)

        # =================================================================
        # SECTION 3: WORKS FOR ANY NUMBER
        # =================================================================
        any_title = Text("Works for\nany number", font_size=35, fill_color=TEAL)
        any_title.to_edge(UP, buff=2.5)
        self.play(Write(any_title), run_time=1)
        self.wait(1)

        n1 = Tex("2^0 = 1", font_size=45, fill_color=BLUE)
        n1.next_to(any_title, DOWN, buff=0.5)
        self.play(Write(n1), run_time=0.8)
        self.wait(1)

        n2 = Tex("10^0 = 1", font_size=45, fill_color=BLUE)
        n2.next_to(n1, DOWN, buff=0.4)
        self.play(Write(n2), run_time=0.8)
        self.wait(1)

        n3 = Tex("100^0 = 1", font_size=45, fill_color=BLUE)
        n3.next_to(n2, DOWN, buff=0.4)
        self.play(Write(n3), run_time=0.8)
        self.wait(2)

        self.play(FadeOut(any_title), FadeOut(n1), FadeOut(n2), FadeOut(n3), run_time=1)

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("0^0 = \\ ?", font_size=55)
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
