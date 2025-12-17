from manimlib import *

class Episode4(Scene):
    def construct(self):
        # ============================================
        # 0.0-3.0s: HOOK
        # "16% of 50 = ?" with confused emoji
        # ============================================
        
        hook = Tex("16", "\\%", "\\text{ of }", "50", "=", "?", font_size=55)
        hook[0].set_color(TEAL)       # 16
        hook[1].set_color(TEAL)       # %
        hook[3].set_color(GOLD)       # 50
        hook[5].set_color(RED)        # ?
        hook.to_edge(UP, buff=2.0)
        
        # Confused emoji - simple red face
        emoji_face = Circle(radius=0.35, fill_color=RED, fill_opacity=1, stroke_width=0)
        emoji_eye_l = Text("×", font_size=20, fill_color=WHITE)
        emoji_eye_r = Text("×", font_size=20, fill_color=WHITE)
        emoji_mouth = Text("~", font_size=25, fill_color=WHITE)
        emoji_eye_l.move_to(emoji_face.get_center() + UP * 0.08 + LEFT * 0.12)
        emoji_eye_r.move_to(emoji_face.get_center() + UP * 0.08 + RIGHT * 0.12)
        emoji_mouth.move_to(emoji_face.get_center() + DOWN * 0.1)
        confused_emoji = VGroup(emoji_face, emoji_eye_l, emoji_eye_r, emoji_mouth)
        confused_emoji.next_to(hook, DOWN, buff=0.6)
        
        self.play(Write(hook), run_time=1.5)
        self.play(FadeIn(confused_emoji, scale=1.3), run_time=0.5)
        self.wait(1)
        
        # ============================================
        # 3.0-8.0s: REVEAL VISUAL TRICK - SWAP
        # Numbers physically swap places
        # ============================================
        
        self.play(FadeOut(confused_emoji), run_time=0.3)
        
        # Create separate mobjects for the swap animation
        num_16 = Tex("16", font_size=55, fill_color=TEAL)
        num_50 = Tex("50", font_size=55, fill_color=GOLD)
        percent_sign = Tex("\\%", font_size=55, fill_color=WHITE)
        of_text = Tex("\\text{ of }", font_size=55, fill_color=WHITE)
        equals_q = Tex("= ?", font_size=55, fill_color=RED)
        
        # Position them to match the original hook layout
        num_16.move_to(hook[0].get_center())
        percent_sign.move_to(hook[1].get_center())
        of_text.move_to(hook[2].get_center())
        num_50.move_to(hook[3].get_center())
        equals_q.move_to(hook[4:].get_center())
        
        # Swap out the hook for individual pieces
        self.play(
            FadeOut(hook),
            FadeIn(num_16), FadeIn(percent_sign), FadeIn(of_text), FadeIn(num_50), FadeIn(equals_q),
            run_time=0.3
        )
        
        # Store target positions for swap
        pos_16 = num_16.get_center()
        pos_50 = num_50.get_center()
        
        # SWOOSH swap - numbers cross with arc paths
        self.play(
            num_16.animate.move_to(pos_50),
            num_50.animate.move_to(pos_16),
            run_time=0.8,
            rate_func=smooth
        )
        self.wait(0.3)
        
        # Now rearrange to proper "50% of 16 = ?"
        swapped = Tex("50", "\\%", "\\text{ of }", "16", "=", "?", font_size=55)
        swapped[0].set_color(GOLD)      # 50
        swapped[1].set_color(GOLD)      # %
        swapped[3].set_color(TEAL)      # 16
        swapped[5].set_color(RED)       # ?
        swapped.to_edge(UP, buff=2.0)
        
        self.play(
            FadeOut(VGroup(num_16, num_50, percent_sign, of_text, equals_q)),
            FadeIn(swapped),
            run_time=0.4
        )
        self.wait(0.5)
        
        # ============================================
        # 8.0-14.0s: A-HA MOMENT
        # "50% of 16" = half of 16 = 8
        # ============================================
        
        # Show "(half)" hint below 50%
        half_hint = Text("(half)", font_size=30, fill_color=GREEN_C)
        half_hint.next_to(swapped[0:2], DOWN, buff=0.25)
        
        self.play(FadeIn(half_hint, shift=UP * 0.2), run_time=0.5)
        self.wait(0.5)
        
        # Big answer "8"
        answer = Tex("8", font_size=120, fill_color=GREEN_C)
        answer.move_to(ORIGIN)
        
        self.play(
            FadeOut(swapped),
            FadeOut(half_hint),
            run_time=0.3
        )
        self.play(Write(answer), run_time=0.7)
        
        # Green checkmark
        checkmark = Tex("\\checkmark", font_size=80, fill_color=GREEN_C)
        checkmark.next_to(answer, RIGHT, buff=0.25)
        
        self.play(Write(checkmark), run_time=0.4)
        self.wait(1)
        
        # ============================================
        # 14.0-24.0s: EXPOSITION
        # Show formula and reasoning
        # ============================================
        
        # Move answer up
        answer_group = VGroup(answer, checkmark)
        self.play(answer_group.animate.to_edge(UP, buff=1.5), run_time=0.5)
        
        # Formula: a% of b = b% of a
        formula = Tex("a", "\\%", "\\text{ of }", "b", "=", "b", "\\%", "\\text{ of }", "a", font_size=45)
        formula[0].set_color(TEAL)    # a
        formula[1].set_color(TEAL)    # %
        formula[3].set_color(GOLD)    # b
        formula[5].set_color(GOLD)    # b
        formula[6].set_color(GOLD)    # %
        formula[8].set_color(TEAL)    # a
        formula.move_to(ORIGIN).shift(UP * 0.3)
        
        self.play(Write(formula), run_time=1.5)
        self.wait(0.8)
        
        # Why? - Math breakdown
        why_label = Text("Why?", font_size=35, fill_color=WHITE)
        why_label.next_to(formula, DOWN, buff=0.6)
        
        math_proof = Tex(r"\frac{a \times b}{100}", "=", r"\frac{b \times a}{100}", font_size=40)
        math_proof.next_to(why_label, DOWN, buff=0.4)
        
        self.play(Write(why_label), run_time=0.4)
        self.play(Write(math_proof), run_time=1)
        self.wait(1)
        
        # Show actual calculation
        actual_calc = Tex(r"\frac{16 \times 50}{100} = 8", font_size=35, fill_color=GREY_B)
        actual_calc.next_to(math_proof, DOWN, buff=0.5)
        
        self.play(FadeIn(actual_calc), run_time=0.5)
        self.wait(1.5)
        
        # Clear exposition
        self.play(
            FadeOut(VGroup(answer_group, formula, why_label, math_proof, actual_calc)),
            run_time=0.5
        )
        
        # ============================================
        # 24.0-32.0s: CHALLENGE + CTA
        # "44% of 25 = ?" with timer
        # ============================================
        
        # Challenge title
        challenge_title = Text("Your turn!", font_size=40, fill_color=RED)
        challenge_title.to_edge(UP, buff=1.5)
        
        # Challenge question
        challenge_q = Tex("44", "\\%", "\\text{ of }", "25", "=", "?", font_size=55)
        challenge_q[0].set_color(TEAL)
        challenge_q[1].set_color(TEAL)
        challenge_q[3].set_color(GOLD)
        challenge_q[5].set_color(RED)
        challenge_q.next_to(challenge_title, DOWN, buff=0.8)
        
        # Hint
        swap_hint = Text("(Swap it!)", font_size=30, fill_color=GREEN_C)
        swap_hint.next_to(challenge_q, DOWN, buff=0.4)
        
        # Comment CTA
        comment_cta = Text("Comment your answer!", font_size=30, fill_color=WHITE)
        comment_cta.next_to(swap_hint, DOWN, buff=0.6)
        
        self.play(Write(challenge_title), run_time=0.5)
        self.play(Write(challenge_q), run_time=0.8)
        self.play(FadeIn(swap_hint), run_time=0.4)
        self.wait(0.3)
        self.play(Write(comment_cta), run_time=0.5)
        
        # Timer clock
        clock_face = Circle(radius=0.4, stroke_color=TEAL, stroke_width=3)
        clock_hand = Line(ORIGIN, UP * 0.3, color=RED, stroke_width=3)
        clock = VGroup(clock_face, clock_hand)
        clock.next_to(comment_cta, DOWN, buff=0.6)
        
        self.play(FadeIn(clock), run_time=0.3)
        self.play(
            Rotate(clock_hand, angle=-TAU, about_point=clock_face.get_center()),
            run_time=3,
            rate_func=linear
        )
        self.wait(0.3)
        
        # Clear challenge
        self.play(
            FadeOut(VGroup(challenge_title, challenge_q, swap_hint, comment_cta, clock)),
            run_time=0.5
        )
        
        # ============================================
        # STANDARD CTA
        # LIKE, SHARE, SUBSCRIBE
        # ============================================
        
        like_text = Text("LIKE", font="American Captain", font_size=55, fill_color=TEAL)
        share_text = Text("SHARE", font="American Captain", font_size=55, fill_color=WHITE)
        sub_text = Text("SUBSCRIBE", font="American Captain", font_size=55, fill_color=RED)
        
        cta_group = VGroup(like_text, share_text, sub_text).arrange(DOWN, buff=0.4)
        cta_group.move_to(ORIGIN)
        
        self.play(Write(like_text), run_time=0.5)
        self.wait(0.2)
        self.play(TransformFromCopy(like_text, share_text))
        self.wait(0.2)
        self.play(TransformFromCopy(share_text, sub_text))
        self.wait(1.5)
        
        # Zip off screen
        self.play(
            like_text.animate.shift(LEFT * 10),
            share_text.animate.shift(RIGHT * 10),
            sub_text.animate.shift(LEFT * 10),
            run_time=0.7,
            lag_ratio=0.1
        )
        self.wait(0.5)
