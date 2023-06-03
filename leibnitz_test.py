from manim import *
from consts import one_by_n_alt_series_label, leibnitz_label, alternating_series_label


class LeibnitzTestScene(Scene):
    def construct(self):
        one_by_n_alt_series_label.to_corner(LEFT + UP)
        leibnitz_label.to_corner(LEFT + DOWN)
        self.add(one_by_n_alt_series_label)
        self.play(Write(leibnitz_label))
        self.play(Circumscribe(one_by_n_alt_series_label[1], fade_out=True, run_time=2))

        un = one_by_n_alt_series_label[1].copy()
        self.add(un)
        self.play(un.animate.move_to(ORIGIN))

        arrow_up = Arrow(start=un.get_corner(RIGHT + DOWN) + DOWN * 0.1 + RIGHT * 0.1,
                         end=un.get_corner(RIGHT + DOWN) + RIGHT * 0.1 + UP * 0.3)
        arrow_down = Arrow(start=un.get_corner(RIGHT + UP) + UP * 0.2 + RIGHT * 0.5,
                           end=un.get_corner(RIGHT + DOWN) + RIGHT * 0.5 + DOWN * 0.3)
        self.play(GrowArrow(arrow_up))
        self.play(GrowArrow(arrow_down))

        decrease_label = Text("} 递减")
        mark_one = Text("① {")
        _un = un.copy()
        group1 = Group(mark_one, _un, decrease_label)
        group1.arrange(direction=RIGHT, buff=0.2)
        self.play(un.animate.move_to(_un.get_center()), FadeOut(arrow_up, arrow_down))
        self.play(Write(mark_one), Write(decrease_label))
        self.play(Group(mark_one, un, decrease_label)
                  .animate.next_to(one_by_n_alt_series_label, DOWN + RIGHT, aligned_edge=LEFT, buff=1))

        mark_two = Text("②")
        mark_two_lim = MathTex(r"\lim_{n \to \infty}", r"\frac{1}{n}", r"= 0")
        group2 = Group(mark_two, mark_two_lim)
        group2.arrange(direction=RIGHT, buff=0.2)
        self.play(Write(mark_two))
        self.play(Write(mark_two_lim))
        self.play(Wait())
        self.play(group2.animate.next_to(mark_one, DOWN, aligned_edge=LEFT))

        implies_label = MathTex(r"\implies")
        summation = MathTex(r"\sum_{n=1}^{\infty} (-1)^{n-1}\frac{1}{n}")
        implication = Text("收敛")
        implication_group = Group(summation, implication)
        implication_group.arrange(RIGHT, buff=0.2)
        align_group = Group(implies_label, implication_group).arrange(RIGHT, buff=0.5)
        align_group.move_to((group1.get_corner(RIGHT + DOWN) + group2.get_corner(RIGHT + UP)) / 2 + UP * 0.3, aligned_edge=LEFT)

        self.play(Write(implies_label))
        self.play(Write(summation))
        self.play(Write(implication))

        self.play(Circumscribe(leibnitz_label))
        self.play(Wait())

        self.play(Unwrite(one_by_n_alt_series_label))
        alternating_series_label.to_corner(LEFT + UP)
        self.play(Write(alternating_series_label))
        self.play(alternating_series_label[2].copy().animate.move_to(un.get_center() + DOWN * 0.05), FadeOut(un))
        self.play(alternating_series_label[2].copy().animate.move_to(mark_two_lim[1].get_center() + DOWN * 0.05),
                  FadeOut(mark_two_lim[1]))
        self.play(alternating_series_label.copy().animate.move_to(summation), FadeOut(summation))

