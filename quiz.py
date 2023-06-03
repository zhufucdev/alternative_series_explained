from manim import *

Text.set_default(font_size=32)
MathTex.set_default(font_size=32)


class QuizScene(Scene):
    def construct(self):
        def write_all(*groups: Group):
            for g in groups:
                for ele in g:
                    self.play(Write(ele))

        quiz = Group(Text("判别级数"),
                     MathTex(r"\sum_{n=2}^{\infty} (-1)^{n} \frac{1}{\ln n}"),
                     Text("的敛散性，若收敛，是条件收敛还是绝对收敛？")).arrange()
        quiz.to_edge(UP)
        write_all(quiz)

        solve_label = Text("解：")
        abs_res_1 = MathTex(r"\vert (-1)^{n} \vert \frac{1}{\ln n} = \frac{1}{\ln n}",
                            r">", r"\frac{1}{n}")
        abs_res_2 = Group(Text("而"), MathTex(r"\sum_{n=2}^{\infty} \frac{1}{n}"), Text("发散")).arrange()
        abs_res_3 = Group(MathTex(r"\therefore \sum_{n=2}^{\infty} \frac{1}{\ln n}"), Text("发散")).arrange()

        solve_label.next_to(quiz, DOWN, aligned_edge=LEFT)
        abs_res_1.next_to(solve_label, RIGHT, aligned_edge=LEFT, buff=0.5)
        abs_res_2.next_to(abs_res_1, DOWN, aligned_edge=LEFT)
        abs_res_3.next_to(abs_res_2, DOWN, aligned_edge=LEFT)

        self.play(Write(solve_label))
        self.play(Write(abs_res_1))
        write_all(abs_res_2, abs_res_3)

        divide_res_1 = MathTex(r"\because \frac{1}{\ln (n+1)} - {\frac{1}{\ln n} "
                               r"= \frac{\ln (1 - \frac{1}{n+1})}{\ln (n+1) \ln n}"
                               r"< 0")
        divide_res_2 = Group(MathTex(r"\therefore \{\frac{1}{\ln n}\}"), Text("递减")).arrange()
        divide_res_3 = Group(Text("而"), MathTex(r"\lim_{n \to \infty} \frac{1}{\ln n} = 0")).arrange()
        divide_res_4 = Group(MathTex(r"\therefore \sum_{n=2}^{\infty} (-1)^{n} \frac{1}{\ln n}"),
                             Text("条件收敛")).arrange()
        divide_res_1.next_to(abs_res_3, DOWN, aligned_edge=LEFT, buff=0.5)
        divide_res_2.next_to(divide_res_1, DOWN, aligned_edge=LEFT)
        divide_res_3.next_to(abs_res_1, RIGHT, aligned_edge=LEFT, buff=5)
        divide_res_4.next_to(divide_res_3, DOWN, aligned_edge=LEFT)
        self.play(Write(divide_res_1))
        write_all(divide_res_2, divide_res_3, divide_res_4)
