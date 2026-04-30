from manimlib import *

class Episode17(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK
        # =================================================================
        hook = Tex("a^2 - b^2 = (a+b)(a-b)", font_size=45)
        hook.move_to(ORIGIN + UP * 0.5)
        self.play(Write(hook), run_time=1.5)
        self.wait(1)

        hook_q = Text("Why?", font_size=50, fill_color=RED)
        hook_q.next_to(hook, DOWN, buff=0.4)
        self.play(Write(hook_q), run_time=1)
        self.wait(2)

        self.play(FadeOut(hook), FadeOut(hook_q), run_time=1)

        # =================================================================
        # SECTION 2: THE PROOF
        # =================================================================
        a = 2.3
        b = 1.0

        # --- Step 1: Square with bottom brace "a" ---
        sq = Square(side_length=a)
        sq.set_fill(BLUE, opacity=0.3)
        sq.set_stroke(WHITE, width=2)
        sq.move_to(ORIGIN + LEFT * 0.1 + UP * 0.2)

        title = Tex("a^2", font_size=40, fill_color=BLUE)
        title.to_edge(UP, buff=1.2)

        br_a = Brace(sq, DOWN, buff=0.1)
        lb_a = Tex("a", font_size=30)
        lb_a.next_to(br_a, DOWN, buff=0.1)

        self.play(ShowCreation(sq), Write(title), run_time=1)
        self.play(GrowFromCenter(br_a), Write(lb_a), run_time=1)
        self.wait(2)

        bl = sq.get_corner(DL)
        tl = sq.get_corner(UL)
        tr = sq.get_corner(UR)

        # --- Step 2: b square in top-left with braces ---
        b_sq = Square(side_length=b)
        b_sq.set_fill(RED, opacity=0.5)
        b_sq.set_stroke(WHITE, width=2)
        b_sq.move_to(tl + np.array([b / 2, -b / 2, 0]))

        br_bL = Brace(Line(tl, tl + DOWN * b), LEFT, buff=0.1)
        lb_bL = Tex("b", font_size=30)
        lb_bL.next_to(br_bL, LEFT, buff=0.1)

        br_bT = Brace(Line(tl, tl + RIGHT * b), UP, buff=0.1)
        lb_bT = Tex("b", font_size=30)
        lb_bT.next_to(br_bT, UP, buff=0.1)

        self.play(
            FadeIn(b_sq),
            GrowFromCenter(br_bL), Write(lb_bL),
            GrowFromCenter(br_bT), Write(lb_bT),
            run_time=1.5
        )
        self.wait(2)

        # --- Step 3: (a-b) braces on remaining left and top ---
        br_abL = Brace(Line(bl, bl + UP * (a - b)), LEFT, buff=0.1)
        lb_abL = Tex("a-b", font_size=30)
        lb_abL.next_to(br_abL, LEFT, buff=0.1)

        br_abT = Brace(Line(tl + RIGHT * b, tr), UP, buff=0.1)
        lb_abT = Tex("a-b", font_size=30)
        lb_abT.next_to(br_abT, UP, buff=0.1)

        self.play(
            GrowFromCenter(br_abL), Write(lb_abL),
            GrowFromCenter(br_abT), Write(lb_abT),
            run_time=1.5
        )
        self.wait(2)

        title2 = Tex("a^2 - b^2", font_size=40, fill_color=TEAL)
        title2.to_edge(UP, buff=1.2)
        self.play(Transform(title, title2), run_time=1)
        self.wait(1)

        # --- Step 4: Dashed lines split L-shape ---
        dash_h = DashedLine(
            bl + np.array([0, a - b, 0]), bl + np.array([a, a - b, 0]),
            dash_length=0.1, stroke_color=WHITE, stroke_width=2
        )
        dash_v = DashedLine(
            bl + np.array([b, a - b, 0]), bl + np.array([b, a, 0]),
            dash_length=0.1, stroke_color=WHITE, stroke_width=2
        )
        self.play(ShowCreation(dash_h), ShowCreation(dash_v), run_time=1)
        self.wait(1)

        # Colored rects replace square
        rect_bot = Rectangle(width=a, height=a - b)
        rect_bot.set_fill(BLUE, opacity=0.4)
        rect_bot.set_stroke(WHITE, width=2)
        rect_bot.move_to(bl + np.array([a / 2, (a - b) / 2, 0]))

        rect_top = Rectangle(width=a - b, height=b)
        rect_top.set_fill(BLUE, opacity=0.4)
        rect_top.set_stroke(WHITE, width=2)
        rect_top.move_to(bl + np.array([b + (a - b) / 2, a - b / 2, 0]))

        self.play(
            FadeOut(sq), FadeOut(b_sq), FadeOut(lb_bT), FadeOut(br_bT),
            FadeOut(dash_h), FadeOut(dash_v), FadeOut(lb_bL), FadeOut(br_bL),
            FadeIn(rect_bot), FadeIn(rect_top),
            run_time=1
        )
        self.wait(1)

        br_b_R = Brace(rect_top, RIGHT, buff=0.1)
        lb_b_R = Tex("b", font_size=30)
        lb_b_R.next_to(br_b_R, RIGHT, buff=0.1)

        self.play(
            GrowFromCenter(br_b_R), Write(lb_b_R),
            run_time=1.5
        )
        self.wait(2)

        self.play(FadeOut(lb_abT), FadeOut(br_abT))

        # --- Step 5: Top rect rotates & slides to right of bottom ---
        tgt_x = rect_bot.get_right()[0] + b / 2
        tgt_y = rect_bot.get_center()[1]
        tgt = np.array([tgt_x, tgt_y, 0])

        # Destination brace/label (properly oriented at target)
        rect_dest = Rectangle(width=b, height=a - b)
        rect_dest.set_fill(BLUE, opacity=0.4)
        rect_dest.set_stroke(WHITE, width=2)
        rect_dest.move_to(tgt)

        br_b_dest = Brace(rect_dest, DOWN, buff=0.1)
        lb_b_dest = Tex("b", font_size=30)
        lb_b_dest.next_to(br_b_dest, DOWN, buff=0.1)

        # Rotate the rect physically, brace/label Transform to stay readable
        self.play(
            Rotate(rect_top, -PI / 2, about_point=rect_top.get_center()),
            run_time=1
        )
        self.play(
            rect_top.animate.move_to(tgt),
            Transform(br_b_R, br_b_dest),
            Transform(lb_b_R, lb_b_dest),
            run_time=1.5
        )
        self.wait(2)

        # --- Step 6: Big brace → a+b assembled ---
        combined = VGroup(rect_bot, rect_top)
        br_full = Brace(combined, DOWN, buff=0.7)

        apb = Tex("a", "+", "b", font_size=30)
        apb.next_to(br_full, DOWN, buff=0.1)

        self.play(GrowFromCenter(br_full), run_time=1)
        self.play(
            TransformFromCopy(lb_a[-1], apb[0]),
            Write(apb[1]),
            TransformFromCopy(lb_b_R[-1], apb[2]),
            run_time=1.5
        )
        self.wait(2)

        # --- Step 7: Assemble (a+b)(a-b) below ---
        part_apb = Tex("(a+b)", font_size=35)
        part_amb = Tex("(a-b)", font_size=35)
        part_apb.next_to(apb, DOWN, buff=0.5)
        part_amb.next_to(part_apb, RIGHT, buff=0.05)

        self.play(TransformFromCopy(apb, part_apb), run_time=1)
        self.play(TransformFromCopy(lb_abL, part_amb), run_time=1)
        self.wait(1)

        # title2 (a²-b²) moves down next to the assembled expression
        title_copy = Tex("a^2 - b^2 =", font_size=35)
        title_copy.next_to(part_apb, LEFT, buff=0.15)

        self.play(TransformFromCopy(title, title_copy), run_time=1)
        self.wait(1)

        # --- Step 8: All merge into full formula below, in RED ---
        formula = Tex("a^2 - b^2 = (a+b)(a-b)", font_size=42, fill_color=RED)
        formula.move_to(VGroup(title_copy, part_apb, part_amb).get_center())

        self.play(
            FadeOut(rect_bot), FadeOut(rect_top), FadeOut(lb_abL),
            FadeOut(br_b_R), FadeOut(lb_b_R),
            FadeOut(br_abL), FadeOut(br_a), FadeOut(lb_a),
            FadeOut(br_full), FadeOut(apb), FadeOut(title),
            Transform(title_copy, formula),
            Transform(part_apb, formula),
            Transform(part_amb, formula),
            run_time=2
        )
        self.wait(1)
        self.play(
            title_copy.animate.move_to(ORIGIN),
            part_apb.animate.move_to(ORIGIN),
            part_amb.animate.move_to(ORIGIN),
            run_time=1.5
        )
        self.wait(2)
        self.play(FadeOut(title_copy), FadeOut(part_apb), FadeOut(part_amb), run_time=1)

        # =================================================================
        # SECTION 3: EXAMPLE
        # =================================================================
        ex_title = Text("Example", font_size=40, fill_color=TEAL)
        ex_title.to_edge(UP, buff=2)
        self.play(Write(ex_title), run_time=1)
        self.wait(1)

        e1 = Tex("97 \\times 103", font_size=45)
        e1.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(e1), run_time=1)
        self.wait(1)

        e2 = Tex("= (100-3)(100+3)", font_size=40)
        e2.next_to(e1, DOWN, buff=0.4)
        self.play(Write(e2), run_time=1)
        self.wait(1)

        e3 = Tex("= 100^2 - 3^2", font_size=40)
        e3.next_to(e2, DOWN, buff=0.4)
        self.play(Write(e3), run_time=1)
        self.wait(1)

        e4 = Tex("= 10000 - 9", font_size=40)
        e4.next_to(e3, DOWN, buff=0.4)
        self.play(Write(e4), run_time=1)
        self.wait(1)

        e5 = Tex("= 9991", font_size=45, fill_color=GREEN_C)
        e5.next_to(e4, DOWN, buff=0.4)
        self.play(Write(e5), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(ex_title), FadeOut(e1), FadeOut(e2),
            FadeOut(e3), FadeOut(e4), FadeOut(e5),
            run_time=1
        )

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("48 \\times 52 = \\ ?", font_size=50)
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
