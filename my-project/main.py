from manim import *
from manim_themes.manim_theme import apply_theme


class TransformationNotation(MathTex):
    def __init__(self):
        super().__init__()

        self.tex = MathTex(
            "y=",
            "a",
            "f",
            "k",
            "(",
            "x",
            "-d",
            ")",
            "+c",
        )

        self.a = self.tex[1]
        self.k = self.tex[3]
        self.d = self.tex[6]
        self.c = self.tex[8]

        self.add(self.tex)


class BaseTransformationScene(Scene):
    """
    Quickly create function transformation animations.
    """

    def setup(self):
        self.general_transformation_equation = TransformationNotation()

    def construct(self):
        return super().construct()


class VerticalTransformationScene(BaseTransformationScene):
    def construct(self):
        self.wait(1)

        self.play(
            self.function_object.animate.stretch(3, dim=1),
            Transform(
                self.transformation_notation[self.a_index],
                MathTex("2")
                .set_color(YELLOW)
                .move_to(self.transformation_notation[self.a_index])
                .shift(UP * 0.06),
            ),
            run_time=1.5,
        )

        self.wait(2)


class HorizontalTransformationScene(BaseTransformationScene):
    def setup(self):
        default_plot_length = 3
        self.transformation_mathtex = MathTex(self.transformation_notation)
        self.a = self.transformation_mathtex[0]

        graph_config = self.default_graph_config.copy()
        graph_config["x_range"] = [0, default_plot_length]
        print(f"{default_plot_length}")

        super().setup()

    def construct(self):
        self.wait(1)

        self.play(
            # Transform(self.function_object)
            self.function_object.animate.shift(RIGHT * 2),
            Transform(
                self.transformation_notation,
                MathTex("-2)")
                .set_color(RED)
                .move_to(self.transformation_notation[self.d_index]),
            ),
            run_time=1.5,
        )

        self.wait(2)


class TransformationNotation(Scene):
    def construct(self):
        transformation_notation = MathTex("{{y=af}} {{k(x-d)}} {{+c}}")
        isolated_input = transformation_notation[2]

        isolated_input_indices = [0, 1, 3, 4, 5]
        output_param_indices = []

        self.play(Write(transformation_notation))

        self.play(
            FadeToColor(transformation_notation[0][2], color="#D79BFA"),
            FadeToColor(transformation_notation[4], color="#D79BFA"),
        )

        # self.play(
        #     FadeToColor(transformation_notation[2][i], color="#CE78FF")
        #     for i in isolated_input_indices
        # )
        # self.wait(duration=1)
        # self.play(
        #     Transform(
        #         transformation_notation,
        #         isolated_input,
        #         run_time=1,
        #     )
        # )

        self.wait(duration=0.3)
        self.play(ScaleInPlace(transformation_notation, 2))
        self.wait(duration=2)

        # self.play(Transform(transformation_notation))

        # self.play()

        # self.wait(duration=3)

        # transformation_notation.set_color_by_tex("k(x-d)", BLUE)
        # self.add(isolated_input)

        # isolated_input = MathTex("y=af\color{blue}{k(x-d)}+c")
        # isolated_output = Tex("")
        # self.add(transformation_notation)
        # self.wait(duration=3)
        # self.play(Transform(transformation_notation, isolated_input))


if __name__ == "main":
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "DashedGraphScene"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")
