from manimlib import *

class Episode9(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK (light)
        # =================================================================
        problem = Tex("\\sqrt{1764} \\ = \\ ?", font_size=50)
        problem.move_to(ORIGIN)
        self.play(Write(problem), run_time=2)
        self.wait(2)

        hard_text = Text("Without a\ncalculator", font_size=35, fill_color=RED)
        hard_text.next_to(problem, DOWN, buff=0.6)
        self.play(Write(hard_text), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(problem), FadeOut(hard_text), run_time=1.5)

        # =================================================================
        # SECTION 2: STEP 1 — Last digit mapping table (elaborate)
        # =================================================================
        s1_title = Text("Step 1: Last Digit Rule", font_size=35, fill_color=TEAL)
        s1_title.to_edge(UP, buff=2.5)
        self.play(Write(s1_title), run_time=1.5)
        self.wait(2)

        # Table dimensions
        col_w = 2.2       # width of each column
        row_h = 0.5       # height of each row
        table_w = col_w * 2
        n_rows = 7         # 1 header + 6 data
        table_h = row_h * n_rows
        table_top = s1_title.get_bottom()[1] - 0.4
        table_left = -table_w / 2

        # Table grid lines
        grid = VGroup()
        # Horizontal lines
        for i in range(n_rows + 1):
            y = table_top - i * row_h
            weight = 3 if i <= 1 else 1.5
            h_line = Line(
                np.array([table_left, y, 0]),
                np.array([table_left + table_w, y, 0]),
                stroke_width=weight, stroke_color=WHITE
            )
            grid.add(h_line)
        # Vertical lines (left, center, right)
        for x in [table_left, table_left + col_w, table_left + table_w]:
            v_line = Line(
                np.array([x, table_top, 0]),
                np.array([x, table_top - table_h, 0]),
                stroke_width=1.5, stroke_color=WHITE
            )
            grid.add(v_line)

        self.play(ShowCreation(grid), run_time=1.5)

        # Header text
        hdr_left = Text("Last Digit", font_size=24, fill_color=GREY_A)
        hdr_right = Text("Answer ends in", font_size=24, fill_color=GREY_A)
        hdr_left.move_to(np.array([table_left + col_w / 2, table_top - row_h / 2, 0]))
        hdr_right.move_to(np.array([table_left + col_w * 1.5, table_top - row_h / 2, 0]))
        self.play(Write(hdr_left), Write(hdr_right), run_time=1)

        # Data rows with color
        mappings = [
            ("0", "0", BLUE),
            ("1", "1 or 9", RED),
            ("4", "2 or 8", GREEN),
            ("5", "5", ORANGE),
            ("6", "4 or 6", PINK),
            ("9", "3 or 7", TEAL),
        ]

        cell_texts = VGroup()
        for i, (left, right, color) in enumerate(mappings):
            y = table_top - (i + 1.5) * row_h
            left_text = Text(left, font_size=24)
            right_text = Text(right, font_size=24, fill_color=color)
            left_text.move_to(np.array([table_left + col_w / 2, y, 0]))
            right_text.move_to(np.array([table_left + col_w * 1.5, y, 0]))
            cell_row = VGroup(left_text, right_text)
            cell_texts.add(cell_row)
            self.play(Write(cell_row), run_time=0.4)

        self.wait(2)

        self.play(
            FadeOut(s1_title), FadeOut(grid), FadeOut(hdr_left),
            FadeOut(hdr_right), FadeOut(cell_texts),
            run_time=1.5
        )

        # =================================================================
        # SECTION 3: Apply Step 1 to 1764 (new clean screen)
        # =================================================================
        apply_title = Text("Apply to 1764", font_size=35, fill_color=TEAL)
        apply_title.to_edge(UP, buff=3)
        self.play(Write(apply_title), run_time=1.5)
        self.wait(2)

        app1 = Text("1764 ends in 4", font_size=35)
        app1.next_to(apply_title, DOWN, buff=0.5)
        self.play(Write(app1), run_time=1.5)
        self.wait(2)

        app2 = Text("Unit digit = 2 or 8", font_size=35, fill_color=GREEN_C)
        app2.next_to(app1, DOWN, buff=0.5)
        self.play(Write(app2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(apply_title), FadeOut(app1), FadeOut(app2), run_time=1.5)

        # =================================================================
        # SECTION 4: STEP 2 — Tens digit (dense)
        # =================================================================
        s2_title = Text("Step 2: Ignore\nlast 2 digits", font_size=35, fill_color=TEAL)
        s2_title.to_edge(UP, buff=1.5)
        self.play(Write(s2_title), run_time=1.5)
        self.wait(2)

        s2a = Tex("1764 \\to 17", font_size=45)
        s2a.next_to(s2_title, DOWN, buff=0.5)
        self.play(Write(s2a), run_time=1.5)
        self.wait(2)

        s2b = Text("Nearest perfect\nsquare below 17", font_size=35)
        s2b.next_to(s2a, DOWN, buff=0.5)
        self.play(Write(s2b), run_time=1.5)
        self.wait(2)

        s2c = Tex("4^2 \\ = \\ 16 < 17", font_size=45)
        s2c.next_to(s2b, DOWN, buff=0.5)
        self.play(Write(s2c), run_time=1.5)
        self.wait(2)

        s2d = Text("Tens digit = 4", font_size=35, fill_color=TEAL)
        s2d.next_to(s2c, DOWN, buff=0.5)
        self.play(Write(s2d), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(s2_title), FadeOut(s2a), FadeOut(s2b), FadeOut(s2c), FadeOut(s2d),
            run_time=1.5
        )

        # =================================================================
        # SECTION 5: COMBINE — Answer (light)
        # =================================================================
        combine = Text("Answer is\n42 or 48?", font_size=40, fill_color=TEAL)
        combine.to_edge(UP, buff=2.5)
        self.play(Write(combine), run_time=1.5)
        self.wait(2)

        verify = Tex("42^2 \\ = \\ 1764", font_size=45)
        verify.next_to(combine, DOWN, buff=0.5)
        self.play(Write(verify), run_time=1.5)
        self.wait(2)

        final = Tex("\\sqrt{1764} \\ = \\ 42", font_size=50, fill_color=GREEN_C)
        final.next_to(verify, DOWN, buff=0.5)
        self.play(Write(final), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(combine), FadeOut(verify), FadeOut(final), run_time=1.5)

        # =================================================================
        # SECTION 6: MORE EXAMPLES — expanded step-by-step
        # =================================================================
        more = Text("More\nExamples", font_size=40, fill_color=TEAL)
        more.to_edge(UP, buff=1)
        self.play(Write(more), run_time=1.5)
        self.wait(2)

        # Example 1: sqrt(2025) — step by step
        ex1_title = Tex("\\sqrt{2025}", font_size=45)
        ex1_title.next_to(more, DOWN, buff=0.5)
        self.play(Write(ex1_title), run_time=1.5)
        self.wait(2)

        ex1_s1 = Text("Ends in 5, so\nunit digit = 5", font_size=30, fill_color=GREEN_C)
        ex1_s1.next_to(ex1_title, DOWN, buff=0.4)
        self.play(Write(ex1_s1), run_time=1.5)
        self.wait(2)

        ex1_s2 = Text("Ignore last 2 digits: 20", font_size=30)
        ex1_s2.next_to(ex1_s1, DOWN, buff=0.4)
        self.play(Write(ex1_s2), run_time=1.5)
        self.wait(2)

        ex1_s3 = Tex("4^2 = 16 < 20", font_size=35)
        ex1_s3.next_to(ex1_s2, DOWN, buff=0.4)
        self.play(Write(ex1_s3), run_time=1)
        self.wait(2)

        ex1_s4 = Text("Tens = 4", font_size=30, fill_color=TEAL)
        ex1_s4.next_to(ex1_s3, DOWN, buff=0.4)
        self.play(Write(ex1_s4), run_time=1)
        self.wait(2)

        # Answer assembled via TransformFromCopy — separate objects to avoid index issues
        ex1_eq = Tex("\\sqrt{2025} \\ = \\ ", font_size=45)
        ex1_d1 = Tex("4", font_size=45, fill_color=GREEN_C)
        ex1_d2 = Tex("5", font_size=45, fill_color=GREEN_C)
        ex1_eq.next_to(ex1_s4, DOWN, buff=0.4).shift(LEFT * 0.5)
        ex1_d1.next_to(ex1_eq, RIGHT, buff=0.2)
        ex1_d2.next_to(ex1_d1, RIGHT, buff=0.05)
        self.play(Write(ex1_eq), run_time=0.5)
        self.play(TransformFromCopy(ex1_s4[-1], ex1_d1), run_time=1)
        self.play(TransformFromCopy(ex1_s1[-1], ex1_d2), run_time=1)
        self.wait(2)
        self.play(
            FadeOut(ex1_title), FadeOut(ex1_s1), FadeOut(ex1_s2),
            FadeOut(ex1_s3), FadeOut(ex1_s4),
            FadeOut(ex1_eq), FadeOut(ex1_d1), FadeOut(ex1_d2),
            run_time=1.5
        )

        # Example 2: sqrt(3969) — step by step
        ex2_title = Tex("\\sqrt{3969}", font_size=45)
        ex2_title.next_to(more, DOWN, buff=0.5)
        self.play(Write(ex2_title), run_time=1.5)
        self.wait(2)

        ex2_s1 = Text("Ends in 9, so\nunit digit = 3 or 7", font_size=30, fill_color=GREEN_C)
        ex2_s1.next_to(ex2_title, DOWN, buff=0.4)
        self.play(Write(ex2_s1), run_time=1.5)
        self.wait(2)

        ex2_s2 = Text("Ignore last 2 digits: 39", font_size=30)
        ex2_s2.next_to(ex2_s1, DOWN, buff=0.4)
        self.play(Write(ex2_s2), run_time=1.5)
        self.wait(2)

        ex2_s3 = Tex("6^2 = 36 < 39", font_size=35)
        ex2_s3.next_to(ex2_s2, DOWN, buff=0.4)
        self.play(Write(ex2_s3), run_time=1)
        self.wait(2)

        ex2_s4 = Text("Tens = 6, so 63 or 67?", font_size=30, fill_color=TEAL)
        ex2_s4.next_to(ex2_s3, DOWN, buff=0.4)
        self.play(Write(ex2_s4), run_time=1)
        self.wait(2)

        ex2_verify = Tex("63^2 = 3969", font_size=35)
        ex2_verify.next_to(ex2_s4, DOWN, buff=0.4)
        self.play(Write(ex2_verify), run_time=1)
        self.wait(2)

        ex2_ans = Tex("\\sqrt{3969} \\ = \\ 63", font_size=45, fill_color=GREEN_C)
        ex2_ans.next_to(ex2_verify, DOWN, buff=0.4)
        self.play(Write(ex2_ans), run_time=1.5)
        self.wait(2)
        self.play(
            FadeOut(ex2_title), FadeOut(ex2_s1), FadeOut(ex2_s2),
            FadeOut(ex2_s3), FadeOut(ex2_s4), FadeOut(ex2_verify),
            FadeOut(ex2_ans), FadeOut(more),
            run_time=1.5
        )

        # =================================================================
        # CAVEAT
        # =================================================================
        caveat_title = Text("One caveat", font_size=40, fill_color=RED)
        caveat_title.to_edge(UP, buff=2.5)
        self.play(Write(caveat_title), run_time=1.5)
        self.wait(2)

        caveat1 = Text("Works only for\nperfect squares", font_size=35)
        caveat1.next_to(caveat_title, DOWN, buff=0.5)
        self.play(Write(caveat1), run_time=1.5)
        self.wait(2)

        caveat2 = Text("Competitive\nexams always give\nperfect squares", font_size=30, fill_color=TEAL)
        caveat2.next_to(caveat1, DOWN, buff=0.5)
        self.play(Write(caveat2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(caveat_title), FadeOut(caveat1), FadeOut(caveat2), run_time=1.5)

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("\\sqrt{5184} \\ = \\ ?", font_size=50)
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
