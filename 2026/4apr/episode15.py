from manimlib import *

class Episode15(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK — show the almost-full square
        # =================================================================
        hook_q = Text("Does it EVER\nreach 1?", font_size=40, fill_color=RED)
        hook_q.to_edge(UP, buff=3)
        self.play(Write(hook_q), run_time=1.5)
        self.wait(2)
        self.play(FadeOut(hook_q), run_time=1)

        # =================================================================
        # SECTION 2: THE VISUAL PROOF — filling a unit square
        # =================================================================
        sq_size = 4.0

        # Main square outline
        outline = Square(side_length=sq_size, stroke_color=WHITE, stroke_width=2)
        outline.move_to(ORIGIN + UP * 0.8)  # <-- change this to move everything
        self.play(ShowCreation(outline), run_time=1)
        self.wait(1)

        # Bottom-left corner of the outline — all pieces reference this
        bl = outline.get_corner(DL)

        colors = [BLUE, GREEN, ORANGE, RED, TEAL, PINK, YELLOW]

        # Piece 1: left half — 1/2
        p1 = Rectangle(width=sq_size / 2, height=sq_size)
        p1.set_fill(colors[0], opacity=0.7)
        p1.set_stroke(WHITE, width=1)
        p1.move_to(bl + np.array([sq_size / 4, sq_size / 2, 0]))
        lbl1 = Tex("\\frac{1}{2}", font_size=30, fill_color=WHITE)
        lbl1.move_to(p1.get_center())
        self.play(FadeIn(p1), Write(lbl1), run_time=1)
        self.wait(1.5)

        # Piece 2: top-right quarter — 1/4
        p2 = Rectangle(width=sq_size / 2, height=sq_size / 2)
        p2.set_fill(colors[1], opacity=0.7)
        p2.set_stroke(WHITE, width=1)
        p2.move_to(bl + np.array([sq_size * 3 / 4, sq_size * 3 / 4, 0]))
        lbl2 = Tex("\\frac{1}{4}", font_size=25, fill_color=WHITE)
        lbl2.move_to(p2.get_center())
        self.play(FadeIn(p2), Write(lbl2), run_time=1)
        self.wait(1.5)

        # Piece 3: bottom-right-left eighth — 1/8
        p3 = Rectangle(width=sq_size / 4, height=sq_size / 2)
        p3.set_fill(colors[2], opacity=0.7)
        p3.set_stroke(WHITE, width=1)
        p3.move_to(bl + np.array([sq_size * 5 / 8, sq_size / 4, 0]))
        lbl3 = Tex("\\frac{1}{8}", font_size=20, fill_color=WHITE)
        lbl3.move_to(p3.get_center())
        self.play(FadeIn(p3), Write(lbl3), run_time=0.8)
        self.wait(1)

        # Piece 4: 1/16
        p4 = Rectangle(width=sq_size / 4, height=sq_size / 4)
        p4.set_fill(colors[3], opacity=0.7)
        p4.set_stroke(WHITE, width=1)
        p4.move_to(bl + np.array([sq_size * 7 / 8, sq_size * 3 / 8, 0]))
        lbl4 = Tex("\\frac{1}{16}", font_size=16, fill_color=WHITE)
        lbl4.move_to(p4.get_center())
        self.play(FadeIn(p4), Write(lbl4), run_time=0.6)
        self.wait(1)

        # Piece 5: 1/32
        p5 = Rectangle(width=sq_size / 8, height=sq_size / 4)
        p5.set_fill(colors[4], opacity=0.7)
        p5.set_stroke(WHITE, width=1)
        p5.move_to(bl + np.array([sq_size * 13 / 16, sq_size / 8, 0]))
        lbl5 = Tex("\\frac{1}{32}", font_size=16, fill_color=WHITE)
        lbl5.move_to(p5.get_center())
        self.play(FadeIn(p5), Write(lbl5), run_time=0.4)

        # Piece 6: 1/64
        p6 = Rectangle(width=sq_size / 8, height=sq_size / 8)
        p6.set_fill(colors[5], opacity=0.7)
        p6.set_stroke(WHITE, width=1)
        p6.move_to(bl + np.array([sq_size * 15 / 16, sq_size * 3 / 16, 0]))
        lbl6 = Tex("\\frac{1}{64}", font_size=16, fill_color=WHITE)
        lbl6.move_to(p6.get_center())
        self.play(FadeIn(p6), Write(lbl6), run_time=0.3)

        self.wait(2)

        # The formula
        formula = Tex("\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} + \\frac{1}{16} + \\cdots = 1",
                       font_size=30, fill_color=BLUE)
        formula.to_edge(DOWN, buff=2)
        self.play(Write(formula), run_time=2)
        self.wait(2)

        all_pieces = VGroup(outline, p1, p2, p3, p4, p5, p6,
                            lbl1, lbl2, lbl3, lbl4, lbl5, lbl6, formula)
        self.play(FadeOut(all_pieces), run_time=1)

        # =================================================================
        # SECTION 3: EXAMPLE — running decimal sum
        # =================================================================
        ex_title = Text("See it in\nnumbers", font_size=35, fill_color=TEAL)
        ex_title.to_edge(UP, buff=2)
        self.play(Write(ex_title), run_time=1)
        self.wait(1)

        sums = [
            "\\frac{1}{2} = 0.5",
            "\\frac{1}{2} + \\frac{1}{4} = 0.75",
            "\\frac{1}{2} + \\frac{1}{4} + \\frac{1}{8} = 0.875",
        ]
        prev = ex_title
        sum_objs = []
        for s in sums:
            t = Tex(s, font_size=32)
            t.next_to(prev, DOWN, buff=0.4)
            self.play(Write(t), run_time=1)
            self.wait(1)
            sum_objs.append(t)
            prev = t

        approach = Text("Approaching 1.0", font_size=30, fill_color=RED)
        approach.next_to(prev, DOWN, buff=0.4)
        self.play(Write(approach), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(ex_title), FadeOut(approach),
            *[FadeOut(s) for s in sum_objs],
            run_time=1
        )

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("\\frac{1}{3} + \\frac{1}{9} + \\frac{1}{27} + \\cdots = \\ ?", font_size=42)
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
