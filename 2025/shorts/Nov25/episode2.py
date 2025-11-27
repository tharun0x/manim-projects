from manimlib import *

class Episode2(Scene):
    def construct(self):
        # Big top text: "Square 35 in 5 seconds?"
        title = Text("Square any number\nending in 5 quickly", font_size=35, fill_color=RED)
        title.to_edge(UP, buff=1.5)

        problem = Tex("35^2 =\ ?", font_size=50)
        problem.next_to(title, DOWN, buff=1.5)

        self.play(Write(title), run_time=2)
        self.play(Write(problem), run_time=1)
        self.wait(0.5)

        # Show pattern ---
        self.play(FadeOut(problem))

        # Split 35
        d1 = Tex("3", font_size=80, fill_color=TEAL)
        d2 = Tex("5", font_size=80, fill_color=WHITE) # Highlight 5
        group_35 = VGroup(d1, d2).arrange(RIGHT, buff=0.2)
        group_35.move_to(ORIGIN)

        self.play(Write(group_35))
        self.wait(0.5)

        # Emphasize ending in 5
        self.play(Indicate(d2, color=RED))
        self.wait(1)

        # Move 3 to the left slightly
        self.play(
            d1.animate.shift(LEFT * 1),
            d2.animate.set_opacity(0.3) # Dim the 5
        )

        # Show 3 x 4 calculation
        next_num_text = Tex("3 \\times (3+1)", font_size=60)
        next_num_text.next_to(group_35, DOWN, buff=0.5)
        
        calc_text = Tex("3 \\times 4 = 12", font_size=60, color=GREEN_C)
        calc_text.move_to(next_num_text)

        self.play(Write(next_num_text))
        self.wait(0.5)
        self.play(Transform(next_num_text, calc_text))
        self.wait(1)

        # Transform d1 -> 12, d2 -> 25
        target_12 = Tex("12", font_size=120, color=GREEN_C)
        target_25 = Tex("25", font_size=120, color=GOLD)
        c12 = calc_text[-2:].copy()
        
        # Arrange targets at center
        VGroup(target_12, target_25).arrange(RIGHT, buff=0.1).move_to(ORIGIN)
        
        self.play(
            # d1 transforms into 12
            Transform(d1, target_12),
            # Transform d1 into 12
            Transform(c12, target_12),
            FadeOut(calc_text),
            FadeOut(next_num_text),
            run_time=1.5
        )

        self.wait(2)

        self.play(Transform(d2, target_25))
        
        final_ans = VGroup(d1, d2)
        
        full_eq = Tex("35^2 = 1225", font_size=55)
        full_eq.next_to(final_ans, DOWN, buff=1.0)
        self.play(Write(full_eq))
        self.wait(2)
        self.play(FadeOut(VGroup(c12, final_ans, full_eq)))
        self.wait(3)

        # Second Example 65^2 ---
        c1 = Tex("6", font_size=80, fill_color=TEAL)
        c2 = Tex("5", font_size=80, fill_color=WHITE) # Highlight 5
        group_65 = VGroup(c1, c2).arrange(RIGHT, buff=0.2)
        group_65.move_to(ORIGIN)

        self.play(Write(group_65))
        self.wait(0.5)

        # Emphasize ending in 5
        self.play(Indicate(c2, color=RED))
        self.wait(1)

        # Move 3 to the left slightly
        self.play(
            c1.animate.shift(LEFT * 1),
            c2.animate.set_opacity(0.3) # Dim the 5
        )

        # Show 3 x 4 calculation
        next_num_text2 = Tex("6 \\times (6+1)", font_size=60)
        next_num_text2.next_to(group_65, DOWN, buff=0.5)
        
        calc_text2 = Tex("6 \\times 7 = 42", font_size=60, color=GREEN_C)
        calc_text2.move_to(next_num_text)

        self.play(Write(next_num_text2))
        self.wait(0.5)
        self.play(Transform(next_num_text2, calc_text2))
        self.wait(1)

        # Transform d1 -> 12, d2 -> 25
        target_42 = Tex("42", font_size=120, color=GREEN_C)
        target_25 = Tex("25", font_size=120, color=GOLD)
        c42 = calc_text2[-2:].copy()
        
        # Arrange targets at center
        VGroup(target_42, target_25).arrange(RIGHT, buff=0.1).move_to(ORIGIN)
        
        self.play(
            # d1 transforms into 12
            Transform(c1, target_42),
            # Transform d1 into 12
            Transform(c42, target_42),
            FadeOut(calc_text2),
            FadeOut(next_num_text2),
            run_time=1.5
        )

        self.wait(2)

        self.play(Transform(c2, target_25))
        
        final_ans2 = VGroup(c1, c2)
        
        full_eq2 = Tex("65^2 = 4225", font_size=55)
        full_eq2.next_to(final_ans2, DOWN, buff=1.0)
        self.play(Write(full_eq2))
        self.wait(2)
        self.play(FadeOut(VGroup(c42,final_ans2, full_eq2, title)))
        self.wait(3)

        # Challenge
        challenge = Text("Your turn!\nTry this", font_size=45, fill_color=RED)
        challenge.to_edge(UP, buff=2)
        self.play(Write(challenge))

        # Q1: 85^2
        q1 = Tex("85^2 =\ ?", font_size=60)
        q1.next_to(challenge, DOWN, buff=1.0)
        self.play(Write(q1))
        self.wait(1.5)

        # Analog Clock Timer
        clock = VGroup()
        face = Circle(radius=0.5)
        ticks = VGroup()
        for i in range(4):
            tick = Line(UP * 0.4, UP * 0.5).rotate(i * PI / 2, about_point=ORIGIN)
            ticks.add(tick)
        hand = Line(ORIGIN, UP * 0.4, color=RED, stroke_width=4)
        clock.add(face, ticks, hand)
        clock.next_to(q1, DOWN, buff=1)
        
        self.play(Write(clock))
        self.play(
            Rotate(hand, angle=-TAU, about_point=face.get_center()),
            run_time=5,
            rate_func=linear
        )
        self.wait(2)
        self.play(FadeOut(Group(challenge, q1, clock)))

        # --- CTA ---
        like_text = Text("LIKE", font="American Captain", font_size=60, fill_color=TEAL)
        share_text = Text("SHARE", font="American Captain", font_size=60, fill_color=WHITE)
        sub_text = Text("SUBSCRIBE", font="American Captain", font_size=60, fill_color=RED)
        
        cta_group = VGroup(like_text, share_text, sub_text).arrange(DOWN, buff=0.5)
        cta_group.move_to(ORIGIN)
        
        self.play(Write(like_text))
        self.wait(0.5)
        
        self.play(TransformFromCopy(like_text, share_text))
        self.wait(0.5)
        
        self.play(TransformFromCopy(share_text, sub_text))
        self.wait(2)
        
        # Closing transition
        self.play(
            like_text.animate.shift(LEFT * 10),
            share_text.animate.shift(RIGHT * 10),
            sub_text.animate.shift(LEFT * 10),
            run_time=0.8,
            lag_ratio=0.1
        )
        self.wait(2)
