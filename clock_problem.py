import math

from manim import *

from consts import get_clock


def get_u(n):
    u = math.pi * 2 * 1 / n
    if n % 2 == 0:
        u *= -1
    return u


class ClockScene(Scene):
    def construct(self):
        clock, hand, rotate_hand = get_clock()
        hand_tracker = ValueTracker(0)
        label = Text("Hand = 0", font_size=32).move_to(RIGHT * 3)
        self.play(FadeIn(clock))

        hand.add_updater(lambda x: rotate_hand(hand_tracker.get_value()))

        for n in range(1, 5):
            self.play(hand_tracker.animate.increment_value(get_u(n)))
            self.wait()

        self.play(clock.animate.move_to(LEFT), FadeIn(label))
        label.add_updater(lambda x:
                          label.become(
                              Text("Hand = {:.3f}".format(hand_tracker.get_value() / math.pi / 2), font_size=32)
                              .move_to(RIGHT * 3)))
        for n in range(5, 50):
            self.play(hand_tracker.animate(run_time=0.1 + 2 / n).increment_value(get_u(n)))
