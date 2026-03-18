from manimlib import *

class Episode8(Scene):
    def construct(self):
        # Watermark (commented out for YouTube)
        # watermark = Text("@tharun0x", font="Arial", font_size=15, fill_color=WHITE)
        # watermark.set_opacity(0.2)
        # watermark.to_edge(DOWN, buff=1).to_edge(RIGHT, buff=0.5)
        # self.add(watermark)

        # =================================================================
        # SECTION 1: HOOK (light — 2 items)
        # =================================================================
        problem = Tex("1000 - 746 \\ = \\ ?", font_size=50)
        problem.move_to(ORIGIN)
        self.play(Write(problem), run_time=2)
        self.wait(2)

        hard_text = Text("No pen, no paper", font_size=35, fill_color=RED)
        hard_text.next_to(problem, DOWN, buff=0.6)
        self.play(Write(hard_text), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(problem), FadeOut(hard_text), run_time=1.5)

        # =================================================================
        # SECTION 2: THE TRICK (dense — 6+ items)
        # =================================================================
        trick_title = Text("The Trick", font_size=40, fill_color=TEAL)
        trick_title.to_edge(UP, buff=2.5)
        self.play(Write(trick_title), run_time=1.5)
        self.wait(2)

        rule1 = Text("Subtract each digit\nfrom 9", font_size=35)
        rule1.next_to(trick_title, DOWN, buff=0.5)
        self.play(Write(rule1), run_time=1.5)
        self.wait(2)

        rule2 = Text("Except the last\ndigit from 10", font_size=35, fill_color=TEAL)
        rule2.next_to(rule1, DOWN, buff=0.5)
        self.play(Write(rule2), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(trick_title), FadeOut(rule1), FadeOut(rule2), run_time=1.5)

        # Demo: 1000 - 746
        demo_title = Text("1000 - 746", font_size=40, fill_color=TEAL)
        demo_title.to_edge(UP, buff=2.5)
        self.play(Write(demo_title), run_time=1.5)
        self.wait(2)

        d1 = Tex("9 - 7", " \\ = \\ ", "2", font_size=45)
        d1.next_to(demo_title, DOWN, buff=0.5)
        self.play(Write(d1), run_time=1.5)
        self.wait(2)

        d2 = Tex("9 - 4", " \\ = \\ ", "5", font_size=45)
        d2.next_to(d1, DOWN, buff=0.5)
        self.play(Write(d2), run_time=1.5)
        self.wait(2)

        d3 = Tex("10 - 6", " \\ = \\ ", "4", font_size=45)
        d3.next_to(d2, DOWN, buff=0.5)
        self.play(Write(d3), run_time=1.5)
        self.wait(2)

        # Final answer — copy individual result digits one by one
        ans = Tex("= \\ ", "2", "5", "4", font_size=50)
        ans[1].set_color(GREEN_C)
        ans[2].set_color(GREEN_C)
        ans[3].set_color(GREEN_C)
        ans.next_to(d3, DOWN, buff=0.5)
        self.play(Write(ans[0]), run_time=0.5)  # write the "="
        self.play(TransformFromCopy(d1[4], ans[1]), run_time=1)
        self.play(TransformFromCopy(d2[4], ans[2]), run_time=1)
        self.play(TransformFromCopy(d3[5], ans[3]), run_time=1)
        self.wait(2)

        self.play(
            FadeOut(demo_title), FadeOut(d1), FadeOut(d2), FadeOut(d3), FadeOut(ans),
            run_time=1.5
        )

        # =================================================================
        # SECTION 3: MORE EXAMPLES (light — cycling)
        # =================================================================
        more = Text("More\nExamples", font_size=40, fill_color=TEAL)
        more.to_edge(UP, buff=2.5)
        self.play(Write(more), run_time=1.5)
        self.wait(2)

        # Example 1: 1000 - 387
        e1a = Tex("1000 - 387", font_size=45)
        e1a.next_to(more, DOWN, buff=0.5)
        self.play(Write(e1a), run_time=1.5)
        self.wait(2)

        e1b = Tex("3 \\to ", "\ 6", ", \quad 8 \\to ", "\ 1", ", \quad 7 \\to ", "\ 3", font_size=35)
        e1b.next_to(e1a, DOWN, buff=0.5)
        self.play(Write(e1b), run_time=1.5)
        self.wait(2)

        e1c = Tex("= \\ ", "6", "1", "3", font_size=50)
        e1c[1].set_color(GREEN_C)
        e1c[2].set_color(GREEN_C)
        e1c[3].set_color(GREEN_C)
        e1c.next_to(e1b, DOWN, buff=0.5)
        self.play(Write(e1c[0]), run_time=0.5)
        self.play(TransformFromCopy(e1b[2], e1c[1]), run_time=1)
        self.play(TransformFromCopy(e1b[6], e1c[2]), run_time=1)
        self.play(TransformFromCopy(e1b[10], e1c[3]), run_time=1)
        self.wait(2)
        self.play(FadeOut(e1a), FadeOut(e1b), FadeOut(e1c), run_time=1.5)

        # Example 2: 1000 - 47 (2-digit — show leading zero trick)
        e2a = Tex("1000 - 47", font_size=45)
        e2a.next_to(more, DOWN, buff=0.5)
        self.play(Write(e2a), run_time=1.5)
        self.wait(2)

        e2note = Text("47 is same as 047", font_size=30, fill_color=TEAL)
        e2note.next_to(e2a, DOWN, buff=0.5)
        self.play(Write(e2note), run_time=1.5)
        self.wait(2)

        e2b = Tex("0 \\to ","\ 9", ", \quad 4 \\to ", "\ 5", ", \quad 7 \\to ", "\ 3", font_size=35)
        e2b.next_to(e2note, DOWN, buff=0.5)
        self.play(Write(e2b), run_time=1.5)
        self.wait(2)

        e2c = Tex("= \\ ", "9", "5", "3", font_size=50)
        e2c[1].set_color(GREEN_C)
        e2c[2].set_color(GREEN_C)
        e2c[3].set_color(GREEN_C)
        e2c.next_to(e2b, DOWN, buff=0.5)
        self.play(Write(e2c[0]), run_time=0.5)
        self.play(TransformFromCopy(e2b[2], e2c[1]), run_time=1)
        self.play(TransformFromCopy(e2b[6], e2c[2]), run_time=1)
        self.play(TransformFromCopy(e2b[10], e2c[3]), run_time=1)
        self.wait(2)
        self.play(
            FadeOut(e2a), FadeOut(e2note), FadeOut(e2b), FadeOut(e2c), FadeOut(more),
            run_time=1.5
        )

        # =================================================================
        # SECTION 4: WHY IT WORKS (dense — 4 items)
        # =================================================================
        why = Text("Why does this\nwork?", font_size=40, fill_color=TEAL)
        why.to_edge(UP, buff=2.5)
        self.play(Write(why), run_time=1.5)
        self.wait(2)

        w1 = Tex("1000 \\ = \\ 999 + 1", font_size=45)
        w1.next_to(why, DOWN, buff=0.5)
        self.play(Write(w1), run_time=1.5)
        self.wait(2)

        w2a = Tex("1000 - N \\ = \\ (999 + 1) - N", font_size=38)
        w2a.next_to(w1, DOWN, buff=0.5)
        self.play(Write(w2a), run_time=1.5)
        self.wait(2)

        w2b = Tex("= \\ (999 - N) + 1", font_size=38, fill_color=TEAL)
        w2b.next_to(w2a, DOWN, buff=0.5)
        self.play(Write(w2b), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(why), FadeOut(w1), FadeOut(w2a), FadeOut(w2b), run_time=1.5)

        # Explanation of what 999 - N means
        meaning = Text("Subtract each digit from 9\nand add 1 to the result", font_size=30, fill_color=TEAL)
        meaning.to_edge(UP, buff=2.5)
        self.play(Write(meaning), run_time=1.5)
        self.wait(2)

        w3 = Text("which is equal to", font_size=35)
        w3.next_to(meaning, DOWN, buff=0.5)
        self.play(Write(w3), run_time=1.5)
        self.wait(2)

        w4 = Text("Subtracting each initial\n digits from 9 and\n subtracting the last\n digit alone from 10", font_size=30, fill_color=RED)
        w4.next_to(w3, DOWN, buff=0.5)
        self.play(Write(w4), run_time=1.5)
        self.wait(2)

        self.play(FadeOut(meaning), FadeOut(w3), FadeOut(w4), run_time=1.5)

        # =================================================================
        # SECTION 5: CHALLENGE
        # =================================================================
        c_title = Text("Challenge", font_size=45, fill_color=RED)
        c_eq = Tex("1000 - 683 \\ = \\ ?", font_size=50)
        challenge_group = VGroup(c_title, c_eq).arrange(DOWN, buff=0.3)
        challenge_group.to_edge(UP, buff=2.5)

        self.play(Write(challenge_group), run_time=2)
        self.wait(2)

        # Standard analog clock timer
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
        # SECTION 6: CTA (standard)
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
