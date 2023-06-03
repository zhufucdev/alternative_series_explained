from manim import *


class OpeningScene(Scene):
    def construct(self):
        title = Text("Steve Reed Prest")
        subtitle = Text("交错项级数审敛法", font_size=32, color=YELLOW)
        Group(title, subtitle).arrange(DOWN)

        self.play(Write(title))
        self.play(Write(subtitle))
