from manim import *

from consts import leibnitz_label, alternating_series_label


class LeibnitzResolutionScene(Scene):
    def construct(self):
        leibnitz_label.to_corner(LEFT + DOWN)
        alternating_series_label.to_corner(LEFT + UP)
        self.add(leibnitz_label, alternating_series_label)

        step_one = Group(Text("①"), MathTex(r"u_{n}"), Text("递减")).arrange()
        step_two = Group(Text("②"), MathTex(r"\lim_{n \to \infty}", r"u_{n}", r"= 0")).arrange()
        Group(step_one, step_two).arrange(DOWN)
        step_one.next_to(step_two, UP, aligned_edge=LEFT)
        self.add(step_one, step_two)

        self.play(FadeOut(alternating_series_label), step_one.animate.to_corner(LEFT + UP), FadeOut(step_two))

        subtraction_res = MathTex(r"u_{n+1}", r"-", r"u_n", r"\leqslant 0")
        division_res = MathTex(r"\frac{u_{n+1}}{u_n} \leqslant 1")
        func_res = MathTex(r"let \mspace{3mu} f(n) =", r"u_n", r"\to", r"\frac{df}{dn} < 0")
        Group(subtraction_res, division_res).arrange(DOWN)
        division_res.align_to(subtraction_res, RIGHT)
        u_n = step_one[1].copy(), step_one[1].copy()
        self.play(Transform(u_n[0], subtraction_res[0]),
                  u_n[1].animate.move_to(subtraction_res[2]),
                  FadeIn(subtraction_res[1]))
        subtraction_res.submobjects[0], subtraction_res.submobjects[2] = u_n
        self.play(Write(subtraction_res[-1]))
        self.play(Write(division_res))

        self.wait()
        division_res.align_to(subtraction_res, RIGHT)
        self.play(Group(subtraction_res, division_res).animate.move_to(UP))
        func_res.next_to(division_res, DOWN)
        self.play(Write(func_res[0]))
        u_n_ = step_one[1].copy()
        self.play(u_n_.animate.move_to(func_res[1]))
        func_res.submobjects[1] = u_n_
        self.play(Write(func_res[2]), Write(func_res[3]))

        self.wait()
        step_two.to_corner(UP + LEFT)
        lobeta_assumptions = MathTex(r"u_n = \frac{a_n}{b_n}")
        lobeta_label = Text("使用洛必达法则")
        lim_res = MathTex(r"let \mspace{3mu} f(n) = a_n, g(n) = b_n",
                          r"= \lim_{n \to \infty} \frac{f^{'}(n)}{g^{'}(n)}")
        title_group = Group(lobeta_assumptions, lobeta_label).arrange(DOWN)
        self.play(FadeOut(step_one, shift=LEFT), FadeIn(step_two, shift=LEFT),
                  FadeOut(subtraction_res, division_res, func_res, shift=LEFT),
                  FadeIn(title_group, shift=LEFT))

        self.wait()

        lim_res_lim_label = Group(step_two[1][0], step_two[1][1]).copy()
        rearranged = Group(lobeta_label.copy(), lim_res[0].copy(),
                           Group(lim_res_lim_label, lim_res[1]).copy().arrange(RIGHT)).arrange(DOWN)
        lim_res[0].move_to(rearranged[1])
        lim_res[1].move_to(rearranged[2][1])
        self.play(FadeOut(lobeta_assumptions, shift=UP),
                  lobeta_label.animate.move_to(rearranged[0]))
        self.play(Write(lim_res[0]))
        self.play(lim_res_lim_label.animate.move_to(rearranged[2][0]))
        lim_res[1].move_to(rearranged[2][1])
        self.play(Write(lim_res[1]))
