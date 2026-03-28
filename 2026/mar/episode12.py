from manimlib import *

class Episode12(Scene):
    def construct(self):
        # =================================================================
        # SECTION 1: HOOK (light)
        # =================================================================
        problem = Tex("\\sqrt[3]{17576} \\ = \\ ?", font_size=50)
        problem.move_to(ORIGIN)
        self.play(Write(problem), run_time=2)
        self.wait(2)

        hard_text = Text("Without a\ncalculator", font_size=35, fill_color=RED)
        hard_text.next_to(problem, DOWN, buff=0.6)
        self.play(Write(hard_text), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(problem), FadeOut(hard_text), run_time=1)

        # =================================================================
        # SECTION 2: STEP 1 — Last Digit mapping table
        # =================================================================
        s1_title = Text("Step 1: Last Digit Rule", font_size=35, fill_color=TEAL)
        s1_title.to_edge(UP, buff=1.5)
        self.play(Write(s1_title), run_time=1.5)
        self.wait(2)

        # Table dimensions
        col_w = 2.2
        row_h = 0.38
        table_w = col_w * 2
        n_rows = 11  # 1 header + 10 data rows
        table_h = row_h * n_rows
        table_top = s1_title.get_bottom()[1] - 0.3
        table_left = -table_w / 2

        # Table grid lines
        grid = VGroup()
        for i in range(n_rows + 1):
            y = table_top - i * row_h
            weight = 3 if i <= 1 else 1.5
            h_line = Line(
                np.array([table_left, y, 0]),
                np.array([table_left + table_w, y, 0]),
                stroke_width=weight, stroke_color=WHITE
            )
            grid.add(h_line)
        for x in [table_left, table_left + col_w, table_left + table_w]:
            v_line = Line(
                np.array([x, table_top, 0]),
                np.array([x, table_top - table_h, 0]),
                stroke_width=1.5, stroke_color=WHITE
            )
            grid.add(v_line)

        self.play(ShowCreation(grid), run_time=1.5)

        # Header text
        hdr_left = Text("Ends in", font_size=18, fill_color=GREY_A)
        hdr_right = Text("Cube root ends in", font_size=18, fill_color=GREY_A)
        hdr_left.move_to(np.array([table_left + col_w / 2, table_top - row_h / 2, 0]))
        hdr_right.move_to(np.array([table_left + col_w * 1.5, table_top - row_h / 2, 0]))
        self.play(Write(hdr_left), Write(hdr_right), run_time=1)

        # Data rows — all 10 individual pairs
        mappings = [
            ("0", "0", BLUE),
            ("1", "1", BLUE),
            ("2", "8", GREEN),
            ("3", "7", RED),
            ("4", "4", ORANGE),
            ("5", "5", ORANGE),
            ("6", "6", TEAL),
            ("7", "3", RED),
            ("8", "2", GREEN),
            ("9", "9", TEAL),
        ]

        cell_texts = VGroup()
        for i, (left, right, color) in enumerate(mappings):
            y = table_top - (i + 1.5) * row_h
            left_text = Text(left, font_size=18)
            right_text = Text(right, font_size=18, fill_color=color)
            left_text.move_to(np.array([table_left + col_w / 2, y, 0]))
            right_text.move_to(np.array([table_left + col_w * 1.5, y, 0]))
            cell_row = VGroup(left_text, right_text)
            cell_texts.add(cell_row)
            self.play(Write(cell_row), run_time=0.25)

        self.wait(2)

        # Highlight mirrored pairs: 2→8 & 8→2, then 3→7 & 7→3
        # cell_texts indices: 0=0, 1=1, 2=2→8, 3=3→7, 4=4, 5=5, 6=6, 7=7→3, 8=8→2, 9=9
        self.play(
            Indicate(cell_texts[2], color=YELLOW, scale_factor=1.2),
            Indicate(cell_texts[8], color=YELLOW, scale_factor=1.2),
            run_time=2
        )
        self.wait(0.5)
        self.play(
            Indicate(cell_texts[3], color=YELLOW, scale_factor=1.2),
            Indicate(cell_texts[7], color=YELLOW, scale_factor=1.2),
            run_time=2
        )
        self.wait(0.5)

        # Apply to problem
        apply1 = Text("17576 ends in 6", font_size=30)
        apply1.next_to(grid, DOWN, buff=0.4)
        self.play(Write(apply1), run_time=1)
        self.wait(2)

        apply2 = Text("Unit digit = 6", font_size=30, fill_color=GREEN_C)
        apply2.next_to(apply1, DOWN, buff=0.3)
        self.play(Write(apply2), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(s1_title), FadeOut(grid), FadeOut(hdr_left),
            FadeOut(hdr_right), FadeOut(cell_texts),
            FadeOut(apply1), FadeOut(apply2),
            run_time=1
        )

        # =================================================================
        # SECTION 3: STEP 2 — Tens digit
        # =================================================================
        s2_title = Text("Step 2: Ignore\nlast 3 digits", font_size=35, fill_color=TEAL)
        s2_title.to_edge(UP, buff=2)
        self.play(Write(s2_title), run_time=1.5)
        self.wait(2)

        s2a = Tex("17576 \\to 17", font_size=45)
        s2a.next_to(s2_title, DOWN, buff=0.5)
        self.play(Write(s2a), run_time=1.5)
        self.wait(2)

        s2b = Text("Nearest perfect\ncube below 17", font_size=30)
        s2b.next_to(s2a, DOWN, buff=0.4)
        self.play(Write(s2b), run_time=1)
        self.wait(2)

        s2c = Tex("2^3 = 8 < 17 < 27 = 3^3", font_size=40)
        s2c.next_to(s2b, DOWN, buff=0.4)
        self.play(Write(s2c), run_time=1.5)
        self.wait(2)

        s2d = Text("Tens digit = 2", font_size=30, fill_color=TEAL)
        s2d.next_to(s2c, DOWN, buff=0.4)
        self.play(Write(s2d), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(s2_title), FadeOut(s2a), FadeOut(s2b), FadeOut(s2c), FadeOut(s2d),
            run_time=1
        )

        # =================================================================
        # SECTION 4: COMBINE — Answer
        # =================================================================
        combine_title = Text("Put them together", font_size=35, fill_color=TEAL)
        combine_title.to_edge(UP, buff=2.5)
        self.play(Write(combine_title), run_time=1)
        self.wait(2)

        tens_text = Text("Tens = 2", font_size=35)
        tens_text.next_to(combine_title, DOWN, buff=0.5)
        self.play(Write(tens_text), run_time=1)

        units_text = Text("Units = 6", font_size=35)
        units_text.next_to(tens_text, DOWN, buff=0.3)
        self.play(Write(units_text), run_time=1)
        self.wait(2)

        final = Tex("\\sqrt[3]{17576} \\ = \\ 26", font_size=50, fill_color=GREEN_C)
        final.next_to(units_text, DOWN, buff=0.5)
        self.play(Write(final), run_time=1.5)
        self.wait(2)

        self.play(
            FadeOut(combine_title), FadeOut(tens_text), FadeOut(units_text), FadeOut(final),
            run_time=1
        )

        # =================================================================
        # SECTION 5: EXAMPLE (1 only)
        # =================================================================
        ex_title = Text("Example", font_size=40, fill_color=TEAL)
        ex_title.to_edge(UP, buff=1.5)
        self.play(Write(ex_title), run_time=1)
        self.wait(2)

        ex1 = Tex("\\sqrt[3]{42875}", font_size=45)
        ex1.next_to(ex_title, DOWN, buff=0.5)
        self.play(Write(ex1), run_time=1.5)
        self.wait(2)

        ex_s1 = Text("Ends in 5, so\nunit digit = 5", font_size=28, fill_color=GREEN_C)
        ex_s1.next_to(ex1, DOWN, buff=0.4)
        self.play(Write(ex_s1), run_time=1)
        self.wait(2)

        ex_s2 = Text("Ignore last 3 digits: 42", font_size=28)
        ex_s2.next_to(ex_s1, DOWN, buff=0.3)
        self.play(Write(ex_s2), run_time=1)
        self.wait(2)

        ex_s3 = Tex("3^3 = 27 < 42 < 64 = 4^3", font_size=35)
        ex_s3.next_to(ex_s2, DOWN, buff=0.3)
        self.play(Write(ex_s3), run_time=1)
        self.wait(2)

        ex_s4 = Text("Tens = 3", font_size=28, fill_color=TEAL)
        ex_s4.next_to(ex_s3, DOWN, buff=0.3)
        self.play(Write(ex_s4), run_time=1)
        self.wait(2)

        # Answer assembled via TransformFromCopy
        ex_eq = Tex("\\sqrt[3]{42875} \\ = \\ ", font_size=45)
        ex_d1 = Tex("3", font_size=45, fill_color=GREEN_C)
        ex_d2 = Tex("5", font_size=45, fill_color=GREEN_C)
        ex_eq.next_to(ex_s4, DOWN, buff=0.4)
        ex_d1.next_to(ex_eq, RIGHT, buff=0.2)
        ex_d2.next_to(ex_d1, RIGHT, buff=0.05)
        self.play(Write(ex_eq), run_time=0.5)
        self.play(TransformFromCopy(ex_s4[-1], ex_d1), run_time=1)
        self.play(TransformFromCopy(ex_s1[-1], ex_d2), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(ex_title), FadeOut(ex1), FadeOut(ex_s1),
            FadeOut(ex_s2), FadeOut(ex_s3), FadeOut(ex_s4),
            FadeOut(ex_eq), FadeOut(ex_d1), FadeOut(ex_d2),
            run_time=1
        )

        # =================================================================
        # CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("\\sqrt[3]{39304} \\ = \\ ?", font_size=50)
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
