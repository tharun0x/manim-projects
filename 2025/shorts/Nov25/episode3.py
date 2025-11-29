from manimlib import *

class Episode3(Scene):
    def construct(self):
        # Hook: Big question
        title = Text("Why area of any triangle\n is ", font_size=30, fill_color=RED)
        formula = Tex(r"\frac{1}{2} \times b \times h\ ?", font_size=30, fill_color=BLUE)
        title.to_edge(UP, buff=1.5)
        formula.next_to(title, DOWN, buff=0.2)
        self.play(Write(title), run_time=1.5)
        self.play(Write(formula), run_time=1.5)
        self.wait(0.5)

        # Quick pop of triangle with "Area = ?"
        triangle = Polygon(
            LEFT * 0.75 + DOWN * 1,
            RIGHT * 0.75 + DOWN * 1,
            UP * 0.5 + RIGHT * 0.5,
            color=TEAL,
            fill_opacity=0.3
        )
        triangle.move_to(ORIGIN).shift(DOWN * 0.2 + LEFT * 0.7)

        self.play(DrawBorderThenFill(triangle), run_time=1)
        self.wait(0.5)

        # Show the core idea: label base "b" and height "h"
        # Get actual triangle vertices
        vertices = triangle.get_vertices()
        apex_pos = vertices[2]
        base_y = vertices[0][1]  # Y-coordinate of base
        
        # Drop perpendicular from apex straight down to base level
        foot = np.array([apex_pos[0], base_y, 0])

        # Base brace and label
        base_left = vertices[0]
        base_right = vertices[1]
        base_brace = Brace(Line(base_left, base_right), DOWN, buff=0.1)
        base_label = Tex("b", font_size=40, fill_color=TEAL)
        base_label.next_to(base_brace, DOWN, buff=0.1)

        # Perpendicular from apex to base (height)
        height_line = DashedLine(apex_pos, foot, color=WHITE, stroke_width=3)
        height_label = Tex("h", font_size=40, fill_color=WHITE)
        height_label.next_to(height_line, LEFT, buff=0.15)

        # Right angle marker
        right_angle = Square(side_length=0.15, color=WHITE, stroke_width=2)
        right_angle.move_to(foot + UP * 0.075 + LEFT * 0.075)

        self.play(ShowCreation(base_brace), Write(base_label), run_time=0.5)
        self.play(ShowCreation(height_line), run_time=1)
        self.play(Write(height_label), FadeIn(right_angle), run_time=0.5)
        self.wait(1)

        # Create duplicate triangle
        triangle_copy = triangle.copy()
        triangle_copy.set_color(TEAL_C)
        triangle_copy.set_style(stroke_opacity=0.7)
        
        # Get vertices for rotation point calculation
        verts = triangle.get_vertices()
        v1, v2, v3 = verts[0], verts[1], verts[2]  # bottom-left, bottom-right, apex
        
        # Midpoint of the slanted edge (bottom-right to apex)
        midpoint_edge = np.array([(v2[0] + v3[0]) / 2, (v2[1] + v3[1]) / 2, 0])
        
        # Show duplication
        self.play(TransformFromCopy(triangle, triangle_copy), run_time=1)
        self.wait(0.3)
        
        # Rotate copy 180° around the edge midpoint to form parallelogram
        self.play(
            Rotate(triangle_copy, PI, about_point=midpoint_edge),
            run_time=1.5
        )
        self.wait(0.5)

        # fadeout title and formula
        self.play(FadeOut(title), FadeOut(formula), run_time=0.5)

        # Group as parallelogram and center
        parallelogram_group = VGroup(triangle, triangle_copy, height_line, height_label, right_angle, base_brace, base_label)
        parallelogram_group.generate_target()
        parallelogram_group.target.move_to(ORIGIN).shift(UP * 1.5)

        self.play(MoveToTarget(parallelogram_group), run_time=1)
        self.wait(0.5)

        # Show "Area = b × h" with small parallelogram symbol
        para_symbol = Polygon(
            ORIGIN, RIGHT * 0.3, RIGHT * 0.3 + UP * 0.2 + RIGHT * 0.1, UP * 0.2 + RIGHT * 0.1,
            color=WHITE, stroke_width=2
        )
        para_symbol.set_height(0.25)
        para_area_text = Tex(r"\ Area = b \times h", font_size=30, fill_color=WHITE)
        para_symbol.next_to(para_area_text, LEFT, buff=0.15)
        para_area = VGroup(para_symbol, para_area_text)
        para_area.next_to(parallelogram_group, DOWN, buff=0.4)
        self.play(ShowCreation(para_symbol), Write(para_area_text), run_time=1)
        self.wait(1)

        # show Parallelogram Area = 2 × Triangle Area
        # Duplicate para_symbol and move it down
        para_symbol2 = para_symbol.copy()
        
        # Position where the second line will be
        target_pos = para_area.get_center() + DOWN * 0.6
        para_symbol2.move_to(target_pos + LEFT * 1.4)
        
        # Animate: copy moves from original to new position below
        self.play(TransformFromCopy(para_symbol, para_symbol2), run_time=0.8)
        
        # Now write the text next to it
        para_area_text2 = Tex(r"Area = 2 \times \triangle \ Area", font_size=30, fill_color=WHITE)
        para_area_text2.next_to(para_symbol2, RIGHT, buff=0.15)
        self.play(Write(para_area_text2), run_time=0.8)
        
        para_area2 = VGroup(para_symbol2, para_area_text2)
        self.wait(1)

        # Show "b × h = 2 × triangle Area" by duplicating parts from above
        # Extract "b × h" from para_area_text and "2 × △ Area" from para_area_text2
        
        # Position for the combined equation
        eq_pos = para_area2.get_center() + DOWN * 0.6
        
        # Duplicate "b × h" part (create new tex that looks like the relevant part)
        bxh_copy = Tex(r"b \times h", font_size=30, fill_color=WHITE)
        bxh_copy.move_to(eq_pos + LEFT * 1)
        
        # Animate from para_area_text down
        self.play(TransformFromCopy(para_area_text, bxh_copy), run_time=0.8)
        
        # Equals sign
        equals_sign = Tex(r"=", font_size=30, fill_color=WHITE)
        equals_sign.next_to(bxh_copy, RIGHT, buff=0.15)
        self.play(Write(equals_sign), run_time=0.3)
        
        # Duplicate "2 × △ Area" part
        tri_area_copy = Tex(r"2 \times \triangle \ Area", font_size=30, fill_color=WHITE)
        tri_area_copy.next_to(equals_sign, RIGHT, buff=0.15)
        
        # Animate from para_area_text2 down
        self.play(TransformFromCopy(para_area_text2, tri_area_copy), run_time=0.8)
        
        two_tri_eq = VGroup(bxh_copy, equals_sign, tri_area_copy)
        self.wait(1)

        # Algebra manipulation: b×h = 2×△Area → △Area = (b×h)/2
        # Position for the final derived equation
        final_eq_pos = two_tri_eq.get_center() + DOWN * 0.8
        
        # Triangle Area on the left
        tri_area_final = Tex(r"\triangle \ Area", font_size=30, fill_color=WHITE)
        tri_area_final.move_to(final_eq_pos + LEFT * 0.7)
        
        # Equals sign
        equals_final = Tex(r"=", font_size=30, fill_color=WHITE)
        equals_final.next_to(tri_area_final, RIGHT, buff=0.15)
        
        # Duplicate b×h and move down for numerator
        bxh_num = Tex(r"b \times h", font_size=30, fill_color=WHITE)
        bxh_num.next_to(equals_final, RIGHT, buff=0.3)
        
        # Fraction line
        frac_line = Line(LEFT * 0.4, RIGHT * 0.4, stroke_width=2)
        frac_line.next_to(equals_final, RIGHT, buff=0.15)
        
        # Position numerator above fraction line
        bxh_num.next_to(frac_line, UP, buff=0.1)
        
        # The "2" moves down to become denominator
        two_denom = Tex(r"2", font_size=30, fill_color=WHITE)
        two_denom.next_to(frac_line, DOWN, buff=0.1)
        
        # Animate: △Area appears, equals sign writes
        self.play(
            TransformFromCopy(tri_area_copy, tri_area_final),
            run_time=0.8
        )
        self.play(Write(equals_final), run_time=0.3)
        
        # Animate: b×h duplicates down as numerator
        self.play(
            TransformFromCopy(bxh_copy, bxh_num),
            run_time=0.8
        )
        
        # Animate: fraction line appears, "2" moves from tri_area_copy down to denominator
        # Extract the "2" visually from tri_area_copy
        two_source = tri_area_copy[0]  # First character is "2"
        self.play(
            ShowCreation(frac_line),
            TransformFromCopy(two_source, two_denom),
            run_time=0.8
        )
        
        derived_formula = VGroup(tri_area_final, equals_final, frac_line, bxh_num, two_denom)
        self.wait(1)

        # Final formula: transform to large formula
        self.play(
            FadeOut(parallelogram_group),
            FadeOut(para_area),
            FadeOut(para_area2),
            FadeOut(two_tri_eq),
            run_time=0.5
        )

        # Transform derived_formula to final formula
        final_formula = Tex("\\triangle \ Area = \\frac{1}{2} \\times b \\times h", font_size=30, fill_color=RED)
        final_formula.move_to(ORIGIN)

        self.play(ReplacementTransform(derived_formula, final_formula), run_time=1.5)
        self.wait(1)

        # Faint triangle sketch behind
        faint_triangle = Polygon(
            LEFT * 0.6 + DOWN * 0.8,
            RIGHT * 0.6 + DOWN * 0.8,
            UP * 0.4 + RIGHT * 0.1,
            color=TEAL,
            fill_opacity=0.5,
            stroke_opacity=0.3
        )
        faint_triangle.move_to(ORIGIN).shift(UP * 1.5)
        self.play(FadeIn(faint_triangle), run_time=0.5)
        self.wait(1)

        self.play(FadeOut(final_formula), FadeOut(faint_triangle), run_time=0.5)

        # Quick practice example
        # Example triangle: base 8 cm, height 5 cm
        example_tri = Polygon(
            LEFT * 0.8 + DOWN * 0.6,
            RIGHT * 0.8 + DOWN * 0.6,
            UP * 0.6 + LEFT * 0.2,
            color=TEAL,
            fill_opacity=0.3
        )
        example_tri.move_to(ORIGIN).shift(UP * 0.5)

        # Base brace and label for example triangle
        ex_verts = example_tri.get_vertices()
        ex_base_left = ex_verts[0]
        ex_base_right = ex_verts[1]
        ex_base_brace = Brace(Line(ex_base_left, ex_base_right), DOWN, buff=0.1)
        ex_base = Tex("8", font_size=30, fill_color=WHITE)
        ex_base.next_to(ex_base_brace, DOWN, buff=0.1)

        # Height with dashed line for example triangle
        ex_apex = ex_verts[2]
        ex_base_y = ex_verts[0][1]
        ex_foot = np.array([ex_apex[0], ex_base_y, 0])
        ex_height_line = DashedLine(ex_apex, ex_foot, color=WHITE, stroke_width=3)
        ex_height = Tex("5", font_size=30, fill_color=WHITE)
        ex_height.next_to(ex_height_line, RIGHT, buff=0.1)

        example_text = Text("What's the area?", font_size=35, fill_color=RED)
        example_text.to_edge(UP, buff=2)

        self.play(
            Write(example_text),
            DrawBorderThenFill(example_tri),
            run_time=1
        )
        self.play(ShowCreation(ex_base_brace), Write(ex_base), ShowCreation(ex_height_line), Write(ex_height), run_time=0.5)
        self.wait(1)

        # Show solving steps
        # Step 1: Write the area formula
        solve_formula = Tex("\\triangle \ Area = \\frac{1}{2} \\times b \\times h", font_size=30, fill_color=WHITE)
        solve_formula.next_to(example_tri, DOWN, buff=0.9)
        self.play(Write(solve_formula), run_time=1)
        self.wait(0.5)

        # Step 2: Plugin values - build equation piece by piece
        # First copy "= 1/2 ×" from formula and translate down
        eq_half_times = Tex("= \\frac{1}{2} \\times", font_size=30, fill_color=WHITE)
        eq_half_times.next_to(solve_formula, DOWN, buff=0.3, aligned_edge=LEFT).shift(RIGHT * 0.8)
        
        self.play(TransformFromCopy(solve_formula, eq_half_times), run_time=0.6)
        
        # Copy 8 from triangle base and place it
        eight_copy = Tex("8", font_size=30, fill_color=WHITE)
        eight_copy.next_to(eq_half_times, RIGHT, buff=0.15)
        
        self.play(TransformFromCopy(ex_base, eight_copy), run_time=0.6)
        
        # Add "×" between 8 and 5
        times_sign = Tex("\\times", font_size=30, fill_color=WHITE)
        times_sign.next_to(eight_copy, RIGHT, buff=0.15)
        
        self.play(Write(times_sign), run_time=0.3)
        
        # Copy 5 from triangle height and place it
        five_copy = Tex("5", font_size=30, fill_color=WHITE)
        five_copy.next_to(times_sign, RIGHT, buff=0.15)
        
        self.play(TransformFromCopy(ex_height, five_copy), run_time=0.6)
        
        solve_step2 = VGroup(eq_half_times, eight_copy, times_sign, five_copy)
        self.wait(0.5)

        # Step 3: Calculate intermediate
        solve_step3 = Tex("= \\frac{40}{2}", font_size=30, fill_color=WHITE)
        solve_step3.next_to(solve_step2, DOWN, buff=0.3)
        solve_step3.shift(LEFT * 1)
        self.play(Write(solve_step3), run_time=0.5)
        self.wait(0.3)

        # Step 4: Final answer
        answer = Tex("= 20\ units^2", font_size=30, fill_color=RED)
        answer.next_to(solve_step3, buff=0.3)
        self.play(Write(answer), run_time=0.8)
        self.wait(1)

        # Group all solve steps for fadeout
        solve_group = VGroup(solve_formula, solve_step2, solve_step3, answer)

        # CTA
        self.play(
            FadeOut(example_text),
            FadeOut(example_tri),
            FadeOut(ex_base_brace),
            FadeOut(ex_base),
            FadeOut(ex_height_line),
            FadeOut(ex_height),
            FadeOut(solve_group),
            run_time=0.5
        )

        #challenge for audience
        # Triangle with base 12 and height 7 (scaled proportionally)
        challenge_tri = Polygon(
            LEFT * 1.0 + DOWN * 0.6,
            RIGHT * 1.0 + DOWN * 0.6,
            UP * 0.7 + LEFT * 0.1,
            color=TEAL,
            fill_opacity=0.3
        )
        challenge_tri.move_to(ORIGIN).shift(UP * 0.5)

        # Base brace and label for challenge triangle
        ch_verts = challenge_tri.get_vertices()
        ch_base_left = ch_verts[0]
        ch_base_right = ch_verts[1]
        ch_base_brace = Brace(Line(ch_base_left, ch_base_right), DOWN, buff=0.1)
        ch_base = Tex("12", font_size=30, fill_color=WHITE)
        ch_base.next_to(ch_base_brace, DOWN, buff=0.1)

        # Height with dashed line for challenge triangle
        ch_verts = challenge_tri.get_vertices()
        ch_apex = ch_verts[2]
        ch_base_y = ch_verts[0][1]
        ch_foot = np.array([ch_apex[0], ch_base_y, 0])
        ch_height_line = DashedLine(ch_apex, ch_foot, color=WHITE, stroke_width=3)
        ch_height = Tex("7", font_size=30, fill_color=WHITE)
        ch_height.next_to(ch_height_line, RIGHT, buff=0.1)

        challenge_text = Text("TRY THIS!", font_size=35, fill_color=RED)
        challenge_text.to_edge(UP, buff=2)

        self.play(
            Write(challenge_text),
            DrawBorderThenFill(challenge_tri),
            run_time=1
        )
        self.play(ShowCreation(ch_base_brace), Write(ch_base), ShowCreation(ch_height_line), Write(ch_height), run_time=0.5)
        self.wait(1)

        # Analog Clock Timer
        clock = VGroup()
        face = Circle(radius=0.5, stroke_color=TEAL)
        ticks = VGroup()
        for i in range(4):
            tick = Line(UP * 0.4, UP * 0.5).rotate(i * PI / 2, about_point=ORIGIN)
            ticks.add(tick)
        hand = Line(ORIGIN, UP * 0.4, stroke_width=4)
        clock.add(face, ticks, hand)
        clock.next_to(challenge_tri, DOWN, buff=1.2)
        
        self.play(Write(clock))
        self.play(
            Rotate(hand, angle=-TAU, about_point=face.get_center()),
            run_time=5,
            rate_func=linear
        )
        self.wait(2)
        self.play(FadeOut(Group(challenge_tri, ch_height_line, ch_height, challenge_text, ch_base_brace, ch_base, clock)))

        # Standard CTA: LIKE, SHARE, SUBSCRIBE
        like_text = Text("LIKE", font_size=40, fill_color=TEAL)
        like_text.move_to(ORIGIN).shift(UP * 1)

        self.play(Write(like_text), run_time=0.5)

        share_text = Text("SHARE", font_size=40, fill_color=WHITE)
        share_text.next_to(like_text, DOWN, buff=0.5)

        self.play(TransformFromCopy(like_text, share_text), run_time=0.5)

        subscribe_text = Text("SUBSCRIBE", font_size=40, fill_color=RED)
        subscribe_text.next_to(share_text, DOWN, buff=0.5)

        self.play(TransformFromCopy(share_text, subscribe_text), run_time=0.5)
        self.wait(1)

        # Zip off screen
        cta_group = VGroup(like_text, share_text, subscribe_text)
        self.play(
            like_text.animate.shift(LEFT * 10),
            share_text.animate.shift(RIGHT * 10),
            subscribe_text.animate.shift(LEFT * 10),
            run_time=0.5,
            lag_ratio=0.1
        )
        self.wait(1)
