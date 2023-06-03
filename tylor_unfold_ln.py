import math

from manim import *

from consts import get_clock


class TylorUnfoldSeries(Scene):
    def construct(self):
        unfolding = MathTex(r"\ln (", r"x + 1", r") &= 1 - \frac{1}{2}", r"x^2", r" + \frac{1}{3}", r"x^3", r"+ \cdots")
        self.play(Write(unfolding))
        plug_in = MathTex("2")
        plug_in.move_to(unfolding[1])
        self.play(Transform(unfolding[1], plug_in))
        unfolding.remove(unfolding[1], unfolding[3], unfolding[5])
        unfolding.insert(1, plug_in)
        self.play(unfolding.animate.arrange())

        result = MathTex(r"\approx 0.693147")
        starting = sum(1 / n if n % 2 == 1 else - 1 / n for n in range(1, 1000))
        clock, hand, rotate_hand = get_clock(1.3)
        clock.move_to(RIGHT * 3 + UP * 0.5)
        rotate_hand(starting * math.pi * 2)
        self.play(unfolding.animate.move_to(LEFT * 1.2 + UP * 0.5))
        result.next_to(unfolding[1], DOWN * 2, aligned_edge=LEFT)
        label = Text("Hand = {:.5f}".format(starting), font_size=32).next_to(clock, DOWN)
        self.play(Write(result), FadeIn(clock, label))

        hand_tracker = ValueTracker(starting * math.pi * 2)
        hand.add_updater(
            lambda x: rotate_hand(hand_tracker.get_value())
        )
        label.add_updater(
            lambda x: label.become(Text("Hand = {:.5f}".format(hand_tracker.get_value() / math.pi / 2), font_size=32)
                                   .next_to(clock, DOWN))
        )
        for n in range(1000, 1020):
            self.play(
                hand_tracker.animate(run_time=0.1).increment_value(math.pi * 2 * (1 / n if n % 2 == 1 else -1 / n)))
