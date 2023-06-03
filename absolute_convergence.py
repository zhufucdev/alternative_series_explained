from manim import *

from consts import leibnitz_label
from consts import abs_convergence_label


class AbsoluteConvergenceScene(Scene):
    def construct(self):
        abs_convergence_label.to_corner(LEFT + DOWN)
        self.play(Write(abs_convergence_label))

        series = MathTex(r"\sum_{n=1}^{\infty} ", r"(-1)^{n-1}", r"\frac{1}{n^2}")
        self.play(Write(series))

        inserted = series.copy()
        inserted.insert(1, MathTex(r"\vert"))
        inserted.insert(3, MathTex(r"\vert"))
        arranged = inserted.copy().arrange()
        self.play(series[0].animate.move_to(arranged[0]), series[1].animate.move_to(arranged[2]),
                  series[2].animate.move_to(arranged[4]))
        self.remove(series)
        series = arranged
        self.add(series)
        self.play(FadeIn(series[1], series[3], shift=DOWN))

        alt_c = [series[2], series[1], series[3]]
        series.remove(*alt_c)
        self.play(FadeOut(*alt_c), series.animate.arrange())

        convergence_label = Text("收敛").next_to(series)
        self.play(Write(convergence_label))

        self.play(FadeOut(convergence_label, series))
        self.play(abs_convergence_label.animate.move_to(ORIGIN))
        self.wait()

        cross = (
            Line(abs_convergence_label.get_corner(LEFT + UP), abs_convergence_label.get_corner(RIGHT + DOWN),
                 color=RED),
            Line(abs_convergence_label.get_corner(RIGHT + UP), abs_convergence_label.get_corner(LEFT + DOWN),
                 color=RED))
        self.play(Create(cross[0]), Create(cross[1]))

        arrow = MathTex(r"\to").move_to(RIGHT * 2)
        leibnitz_label.move_to(RIGHT * 5)
        self.play(Group(Group(abs_convergence_label, cross[0], cross[1]), arrow, leibnitz_label).animate.arrange(RIGHT))

        self.wait()
        self.play(FadeOut(abs_convergence_label, cross[0], cross[1], arrow), leibnitz_label.animate.to_corner(LEFT + DOWN))
