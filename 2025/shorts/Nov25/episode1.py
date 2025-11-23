from manimlib import *

class Episode1(Scene):
    def construct(self):
        # Big top text: "Multiply 23 × 11 in 5 seconds?"
        title = Text("Multiply any 2 digit\n number by 11 in\n 5 seconds?", font_size=35, fill_color=RED)
        title.to_edge(UP, buff=1.5)
        
        problem = Tex("23 \\times 11 =\ ?", font_size=50)
        problem.next_to(title, DOWN, buff=1.5)

        self.play(Write(title), run_time=3)
        self.play(Write(problem), run_time=3)
        self.wait(0.5)        
        self.play(FadeOut(problem))

        # Representation of 23
        d1 = Tex("2", font_size=120, fill_color=BLUE)
        d2 = Tex("3", font_size=120, fill_color=BLUE)
        group_23 = VGroup(d1, d2).arrange(RIGHT, buff=0.2)
        group_23.move_to(ORIGIN)
        
        self.play(Write(group_23))
        self.wait(0.5)
        
        # Split them
        self.play(
            d1.animate.shift(LEFT * 0.75),
            d2.animate.shift(RIGHT * 0.75),
            run_time=1
        )
        self.wait(1)

        # show the middle digit as sum 2+3 = 5, place it between them to form 2 5 3.        
        calculation = Tex("2 + 3 = 5", font_size=80)
        calculation.next_to(group_23, DOWN, buff=1.0)

        self.play(Write(calculation))
        self.wait(1)
        
        middle_digit = calculation[-1].copy() # The '5'
        
        self.play(
            middle_digit.animate.move_to(ORIGIN).scale(1.5).set_color(BLUE), # Move to center gap
            FadeOut(calculation),
            run_time=1.5
        )
        
        # Form final number
        final_result = VGroup(d1, middle_digit, d2)
        self.play(
            final_result.animate.arrange(RIGHT, buff=0.1).move_to(ORIGIN),
            run_time=1
        )
        
        # Show full equation check
        full_eq = Tex("23 \\times 11 = 253", font_size=55)
        full_eq.next_to(final_result, DOWN, buff=1.0)
        self.play(FadeIn(full_eq, shift=UP))
        self.wait(2)

        # Cleanup for next section
        self.play(FadeOut(Group(title, final_result, full_eq)))

        # show 58 × 11 -> 5 + 8 = 13, carry the 1 to left: result 638.        
        edge_cases = Text("Edge Cases", font_size=50, fill_color=RED).to_edge(UP, buff=2.0)
        edge_title = Text("What about 58 x 11?", font_size=37).to_edge(UP, buff=2.0)
        edge_title.next_to(edge_cases, DOWN, buff=0.5)
        self.play(Write(edge_cases)) 
        self.play(Write(edge_title))
        
        e_d1 = Tex("5", font_size=120, fill_color=BLUE)
        e_d2 = Tex("8", font_size=120, fill_color=BLUE)
        group_58 = VGroup(e_d1, e_d2).arrange(RIGHT, buff=0.2) # Already split
        group_58.next_to(edge_title, DOWN, buff=0.7)
        
        self.play(Write(group_58))
        self.wait(0.5)

        self.play(
            e_d1.animate.shift(LEFT * 0.75),
            e_d2.animate.shift(RIGHT * 0.75),
            run_time=1
        )
        self.wait(1)
        
        # Sum
        sum_text = Tex("5 + 8 = 13", font_size=60)
        sum_text.next_to(group_58, DOWN, buff=0.5)
        self.play(Write(sum_text))
        self.wait(0.5)
        
        # Move 13 to middle
        mid_13 = sum_text[-2:].copy() # "13"
        mid_13.generate_target()
        mid_13.target.next_to(e_d1, RIGHT, buff=0.6)
        mid_13.target.scale(2.0).set_color(BLUE)
        
        self.play(MoveToTarget(mid_13), FadeOut(sum_text))
        
        # Animate carry
        # 1 moves to 5 and transforms 5->6
        digit_1 = mid_13[0]
        digit_3 = mid_13[1]
        
        # Show addition brace
        brace = Brace(VGroup(e_d1, digit_1), DOWN, buff=0.1)
        plus_sign = Tex("+", font_size=40, color=YELLOW).next_to(brace, DOWN, buff=0.1)
        self.play(GrowFromCenter(brace), Write(plus_sign))
        self.wait(0.5)

        new_d1 = Tex("6", font_size=120, fill_color=BLUE).move_to(e_d1)
        
        self.play(
            FadeOut(brace), FadeOut(plus_sign),
            digit_1.animate.move_to(e_d1.get_center()).set_opacity(0),
            Transform(e_d1, new_d1),
            digit_3.animate.next_to(new_d1, RIGHT, buff=0.1),
            e_d2.animate.next_to(digit_3, RIGHT, buff=0.1),
            run_time=1.5
        )
        
        # Re-arrange properly
        final_58 = VGroup(e_d1, digit_3, e_d2)
        self.play(final_58.animate.arrange(RIGHT, buff=0.1).next_to(edge_title, DOWN, buff=0.5))
        check_58 = Tex("58 \\times 11 =\ 638", font_size=45).next_to(final_58, DOWN, buff=0.5)
        self.play(Write(check_58))
        self.wait(1)
        
        self.play(FadeOut(Group(edge_cases, edge_title, final_58, check_58)))

        # show 43 × 11 = ?
        challenge = Text("Your turn!\nTry this", font_size=45, fill_color=RED)
        challenge.to_edge(UP, buff=2)
        self.play(Write(challenge))
        
        q1 = Tex("43 \\times 11 =\ ?", font_size=50)
        self.play(Write(q1))
        self.wait(1)

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
        self.play(FadeOut(Group(clock, q1, challenge)))
        
        # CTA
        cta = Text("Like\nShare\nSubscribe", font_size=40, fill_color=RED)
        cta.to_edge(UP, buff=1.8)
        
        cta2 = Text("and", font_size=40)
        cta2.next_to(cta, DOWN, buff=1.2)
        
        cta3 = Text("Turn on the bell icon\nfor more STEM content!", font_size=30, fill_color=YELLOW)
        cta3.next_to(cta2, DOWN, buff=1.2)
        
        self.play(Write(VGroup(cta, cta2, cta3)))
        self.wait(0.5)
        
        # Shapes
        triangle = Triangle()
        triangle.replace(cta, stretch=True).scale(1.8).shift(UP * 0.2)
        
        circle = Circle(color=RED)
        circle.move_to(cta2)
        circle.set_width(cta2.get_width() * 1.5)
        
        rect = SurroundingRectangle(cta3, color=WHITE)
        
        self.play(
            ShowCreation(triangle),
            ShowCreation(circle),
            ShowCreation(rect)
        )
        self.wait(2)

        # Closing transition
        final_group = Group(cta, cta2, cta3, triangle, circle, rect)
        self.play(
            ShrinkToCenter(final_group),
            run_time=1.5
        )
        self.play(FadeOut(final_group))
        self.wait(1)
