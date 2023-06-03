from manim import *
import numpy as np

from consts import one_by_n_alt_series_label


class SeriesScene(Scene):
    def construct(self):
        axes = Axes(
            x_range=[1, 10],
            y_range=[-1, 1],
            x_axis_config={
                "numbers_to_include": np.arange(0.1, 10.01, 1)
            },
            tips=False
        )

        positive_func = axes.plot(lambda x: 1 / x, color=BLUE)
        negative_func = axes.plot(lambda x: -1 / x, color=RED)

        positive_label = axes.get_graph_label(positive_func, r"\frac{1}{x}", x_val=1, direction=DOWN * 4 + RIGHT)
        negative_label = axes.get_graph_label(negative_func, r"-\frac{1}{x}", x_val=1, direction=UP * 6 + RIGHT)

        positive_series = [Dot(axes.i2gp(x, positive_func)) for x in range(1, 11, 2)]
        negative_series = [Dot(axes.i2gp(x, negative_func)) for x in range(2, 11, 2)]

        one_by_n_alt_series_label.move_to(positive_series[-1].get_center() + UP + LEFT * 0.2)

        self.play(FadeIn(axes))
        self.play(Create(positive_func), FadeIn(positive_label))
        self.play(Create(negative_func), FadeIn(negative_label))

        self.play(*[GrowFromCenter(dot) for dot in (negative_series + positive_series)])

        self.play(Uncreate(positive_func), Uncreate(negative_func), FadeOut(positive_label), FadeOut(negative_label))
        self.play(Write(one_by_n_alt_series_label))

        self.play(Wait(1))
        self.play(FadeOut(*[o for o in positive_series + negative_series + [axes]]),
                  one_by_n_alt_series_label.animate.to_corner(UP + LEFT))
