import math

from manim import *

one_by_n_alt_series_label = MathTex("(-1)^{n-1}", r"\frac{1}{n}")
alternating_series_label = MathTex(r"\sum_{n=1}^{\infty}", "(-1)^{n-1}", r"u_{n}")
abs_convergence_label = Text("绝对收敛")
leibnitz_label = Text("莱布尼兹判别法")


def get_clock(radius: float = 2.0) -> (Group, Line, Callable[float, None]):
    circle = Circle(color=WHITE, fill_opacity=0.8, stroke_color=ORANGE, stroke_width=10, radius=radius)

    def get_n(d: float):
        raw = int(d / math.pi * 6)
        if raw == 0:
            return 11
        else:
            return raw - 1

    ticks = [Text(f"{get_n(d) + 1}", font_size=32, color=BLACK)
             .move_to(((radius - 0.3) * math.sin(d), (radius - 0.3) * math.cos(d), 0))
             .rotate(math.pi - d)
             for d in ((n - 1) / 6 * math.pi for n in range(1, 13))]
    hand = Line(ORIGIN, (0, radius - 0.1, 0), color=BLACK)

    def rotate(degree: float):
        r = radius - 0.1
        hand.set_points_by_ends(circle.get_center(),
                                np.array([r * math.sin(degree), r * math.cos(degree), 0]) + circle.get_center())

    clock = Group(*([circle, hand] + ticks))
    return clock, hand, rotate
