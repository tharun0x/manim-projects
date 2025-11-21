from manimlib import *

class Episode1(Scene):
    def construct(self):
        # --- 0.0–2.0s Hook ---
        # Big top text: "Multiply 23 × 11 in 5 seconds?"
        title = Text("Multiply 23 x 11\nin 5 seconds?", font_size=40, fill_color=RED)
        title.to_edge(UP, buff=2.0)
        
        problem = Tex("23 \\times 11 = ?", font_size=50)
        problem.next_to(title, DOWN, buff=1.5)

        self.play(Write(title), run_time=3)
        self.play(Write(problem), run_time=3)
        self.wait(0.5)

        # --- 2.0–6.0s Show method with one example ---
        # Visual: write 2 3 with a gap between digits.
        
        self.play(FadeOut(problem))

        # Representation of 23 split
        d1 = Tex("2", font_size=120, color=BLUE)
        d2 = Tex("3", font_size=120, color=BLUE)
        group_23 = VGroup(d1, d2).arrange(RIGHT, buff=0.2)
        group_23.move_to(ORIGIN)
        
        self.play(Write(group_23))
        self.wait(0.5)
        
        # Split them
        self.play(
            d1.animate.shift(LEFT * 1),
            d2.animate.shift(RIGHT * 1),
            run_time=1
        )
        self.wait(1) # Voice: "Write the two digits with a space between them."

        # --- 6.0–14.0s Reveal trick ---
        # Visual step: show the middle digit as sum 2+3 = 5, place it between them to form 2 5 3.
        
        calculation = Tex("2 + 3 = 5", font_size=80, color=YELLOW)
        calculation.next_to(group_23, DOWN, buff=1.0)
        
        self.play(Write(calculation))
        self.wait(1)
        
        middle_digit = calculation[-1].copy() # The '5'
        
        self.play(
            middle_digit.animate.move_to(ORIGIN).scale(1.5), # Move to center gap
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
        full_eq = Tex("23 \\times 11 = 253", font_size=70, color=GREEN)
        full_eq.next_to(final_result, DOWN, buff=1.0)
        self.play(FadeIn(full_eq, shift=UP))
        self.wait(2)

        # Cleanup for next section
        self.play(FadeOut(Group(title, final_result, full_eq)))

        # --- 14.0–20.0s Show edge cases ---
        # Visual: show 58 × 11 -> 5 + 8 = 13, carry the 1 to left: result 638.
        
        edge_title = Text("What about 58 × 11?", font_size=50).to_edge(UP, buff=2.0)
        self.play(Write(edge_title))
        
        e_d1 = Tex("5", font_size=120, color=BLUE)
        e_d2 = Tex("8", font_size=120, color=BLUE)
        group_58 = VGroup(e_d1, e_d2).arrange(RIGHT, buff=2.0) # Already split
        group_58.move_to(ORIGIN)
        
        self.play(FadeIn(group_58, shift=UP))
        
        # Sum
        sum_text = Tex("5 + 8 = 13", font_size=70, color=YELLOW)
        sum_text.next_to(group_58, DOWN, buff=0.5)
        self.play(Write(sum_text))
        self.wait(0.5)
        
        # Move 13 to middle
        mid_13 = sum_text[-2:].copy() # "13"
        mid_13.generate_target()
        mid_13.target.move_to(ORIGIN)
        mid_13.target.scale(1.5)
        
        self.play(MoveToTarget(mid_13), FadeOut(sum_text))
        
        # Animate carry
        # 1 moves to 5 and transforms 5->6
        digit_1 = mid_13[0]
        digit_3 = mid_13[1]
        
        new_d1 = Tex("6", font_size=120, color=GREEN).move_to(e_d1)
        
        self.play(
            digit_1.animate.move_to(e_d1.get_center()).set_opacity(0),
            Transform(e_d1, new_d1),
            digit_3.animate.next_to(new_d1, RIGHT, buff=0.1),
            e_d2.animate.next_to(digit_3, RIGHT, buff=0.1),
            run_time=1.5
        )
        
        # Re-arrange properly
        final_58 = VGroup(e_d1, digit_3, e_d2)
        self.play(final_58.animate.arrange(RIGHT, buff=0.1).move_to(ORIGIN))
        
        check_58 = Tex("638", font_size=90, color=GREEN).next_to(final_58, DOWN)
        self.play(FadeIn(check_58))
        self.wait(1)
        
        self.play(FadeOut(Group(edge_title, final_58, check_58)))

        # --- 20.0–28.0s Quick practice challenge + CTA ---
        # Visual: flash 47 × 11 and 99 × 11 quickly, hold answers for 1.5s each.
        
        q1 = Tex("47 \\times 11 = ?", font_size=80)
        q1.shift(UP * 2)
        self.play(FadeIn(q1))
        self.wait(1)
        
        a1 = Tex("517", font_size=80, color=GREEN)
        a1.next_to(q1, DOWN)
        self.play(Write(a1))
        self.wait(0.5)
        
        q2 = Tex("99 \\times 11 = ?", font_size=80)
        q2.shift(DOWN * 1)
        self.play(FadeIn(q2))
        self.wait(1)
        
        a2 = Tex("1089", font_size=80, color=GREEN)
        a2.next_to(q2, DOWN)
        self.play(Write(a2))
        self.wait(1)
        
        # CTA
        cta = Text("Follow for daily math hacks!", font_size=40, color=YELLOW)
        cta.to_edge(DOWN, buff=2.0)
        self.play(Write(cta))
        self.wait(2)
