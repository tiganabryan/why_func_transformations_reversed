from manim import *
from manim_themes.manim_theme import apply_theme

"""
Most of the time, the code for scripting an animation is entirely contained within the
construct() method of a Scene class. Inside construct(), you can create objects, 
display them on screen, and animate them.

All animations must reside within the construct() method of a class derived from Scene.
Other code, such as auxiliary or mathematical functions, may reside outside the class.
"""


class BaseTransformationScene(Scene):
    """
    Quickly create my function transformation animations
    """

    def __init__(
        self,
        plot_length: int | float = 8,
        function_expression=lambda x: np.sin(x),
        x_axis_length: int | float = None,
        function_length: int | float = None,
        **kwargs,
    ):
        self.plot_length = plot_length
        self.function_expression = function_expression
        self.function_length = function_length
        self.x_axis_length = x_axis_length

        super().__init__(**kwargs)

    @property
    def axes_config(self):
        return {
            "x_range": [0, self.plot_length, 1],  # (x_min, x_max, x_step)
            "y_range": [-3, 3, -2],
            "axis_config": {"include_tip": False},
            "x_length": self.x_axis_length or self.plot_length,
        }

    @property
    def graph_config(self):
        return {
            "function": lambda x: np.sin(x),
            "color": "PURPLE",
            "x_range": [0, self.function_length or self.plot_length],
        }

    def setup(self):
        for setting in self.graph_config:
            print(self.graph_config[f"{setting}"])

        for setting in self.axes_config:
            print(self.axes_config[f"{setting}"])

        self.general_transformation_equation = MathTex(
            "{{y=}} {{a}} {{f}} {{k}} {{(x}} {{-d)}} {{+c}}"
        )
        self.general_transformation_equation.to_edge(RIGHT, 1.7)
        self.a_index = 2
        self.c_index = 12
        self.d_index = 10
        self.k_index = 6

        self.add(self.general_transformation_equation)  # render it on screen

        # create coordinate system obj
        self.axes = Axes(
            **self.axes_config,
        )

        # create function's graph obj
        for val in self.graph_config:
            print(f"{self.graph_config[val]}")

        self.function_object = self.axes.plot(**self.graph_config)

        # dotted line version
        # dotted_sin_func = DashedVMobject(
        #     function_object,
        #     num_dashes=200,
        #     # dash_length=0.001,
        #     # dashed_ratio=0.1,
        #     equal_lengths=True,
        #     color="#9BE1FA",
        # )

        # add colour fill to graph
        self.area_under_curve = self.axes.get_area(
            self.function_object,
            x_range=[0, self.function_length or self.plot_length],
            color=[PURPLE, PINK, BLUE],
            fill_opacity=0.5,
        )

        # link evthng together
        self.sine_graph = VGroup.add(
            self.axes, self.function_object, self.area_under_curve
        )
        self.sine_graph.to_edge(LEFT, 1)
        self.add(self.sine_graph)

        def update_area(
            self,
        ):  # remove repeat here, same logic as original area maker. add area config obj or smthg
            new_area = self.axes.get_area(
                self.function_object,
                x_range=[0, self.function_length or self.plot_length],
                color=[PURPLE, PINK, BLUE],
                fill_opacity=0.5,
            )
            self.area_under_curve.become(new_area)

        self.add_updater(
            lambda dt: update_area(self)
        )  # dt param is passed in by manim. not used but required by manim

    def construct(self):
        return super().construct()


class VerticalTransformationScene(BaseTransformationScene):
    def construct(self):
        self.wait(1)

        self.play(
            self.function_object.animate.stretch(3, dim=1),
            Transform(
                self.general_transformation_equation[self.a_index],
                MathTex("2")
                .set_color(YELLOW)
                .move_to(self.general_transformation_equation[self.a_index])
                .shift(UP * 0.06),
            ),
            run_time=1.5,
        )

        self.wait(2)


class HorizontalTransformationScene(BaseTransformationScene):
    def setup(self):
        self.plot_length = 7
        self.function_length = 4

        super().setup()

    def construct(self):
        self.wait(1)

        self.play(
            # Transform(self.function_object) # replace animation with a real transformation on the graph obj eventually
            self.function_object.animate.shift(RIGHT * 2),
            Transform(
                self.general_transformation_equation[self.d_index],
                MathTex("-2)")
                .set_color(RED)
                .move_to(self.general_transformation_equation[self.d_index]),
            ),
            run_time=1.5,
        )

        self.wait(2)


class VerticalTransformationScene(Scene):
    def construct(self):
        transformation_notation = MathTex("{{y=}} {{a}} {{fk(x-d)}} {{+c}}")
        transformation_notation.to_edge(RIGHT, 1.7)
        a_index = 2
        c_index = 6
        self.add(transformation_notation)

        # 1. Create the coordinate axes
        axes = Axes(
            x_range=[0, 12, 1],
            y_range=[-3, 3, -2],
            axis_config={"include_tip": False},
            x_length=6,
        )

        # 2. Generate a standard continuous graph (e.g., f(x) = sqrt(x))
        # Note: DottedVMobject is best for functions.
        # For discrete data, use axes.plot_line_graph() with add_vertex_dots=False
        continuous_graph = axes.plot(lambda x: np.sin(x), color=PURPLE)

        # 3. Convert the graph to a dashed/dotted line
        dotted_sin_func = DashedVMobject(
            continuous_graph,
            num_dashes=200,
            # dash_length=0.001,
            # dashed_ratio=0.1,
            equal_lengths=True,
            color="#9BE1FA",
        )

        area_under_curve = axes.get_area(
            continuous_graph,
            x_range=[0, 12],
            color=[PURPLE, PINK, BLUE],
            fill_opacity=0.5,
        )

        # def update_area(area):
        #     # .become() swaps the internal polygon meshes smoothly frame-by-frame
        #     new_area = axes.get_area(
        #         continuous_graph,
        #         x_range=[0, 12],
        #         color=[PURPLE, PINK, BLUE],
        #         fill_opacity=0.5,
        #     ).to_edge(LEFT, 1)
        #     MaintainPositionRelativeTo(new_area, dotted_sin_func)
        #     area.become(new_area)

        # graph,

        # 4. Add to the scene and animate
        # self.play(Create(axes), run_time=0.4)
        # self.play(Create(dotted_sin_func), run_time=1)
        sine_graph = VGroup.add(axes, continuous_graph, area_under_curve)
        sine_graph.to_edge(LEFT, 1)
        self.add(sine_graph)

        # area_under_curve.add_updater(update_area)

        def update_area(area):
            new_area = axes.get_area(
                continuous_graph,
                x_range=[0, 12],
                color=[PURPLE, PINK, BLUE],
                fill_opacity=0.5,
            )
            area.become(new_area)

        area_under_curve.add_updater(update_area)
        self.wait(2)

        str_replacement_col = YELLOW
        shift_replacement_col = PURPLE

        replacement_number = {
            "vertical_str_by_2": MathTex("2"),
            "vertical_str_by_1": MathTex("1"),
            "vertical_shift_down": MathTex("-2"),
            "vertical_shift_up": MathTex("+2"),
        }

        self.play(
            continuous_graph.animate.stretch(3, dim=1),
            Transform(
                transformation_notation[a_index],
                replacement_number["vertical_str_by_2"]
                .set_color(str_replacement_col)
                .move_to(transformation_notation[a_index])
                .shift(UP * 0.06),
            ),
            run_time=1.5,
        )
        self.wait(1)

        self.play(
            continuous_graph.animate.stretch(0.5, dim=1),
            Transform(
                transformation_notation[a_index],
                replacement_number["vertical_str_by_1"]
                .set_color(str_replacement_col)
                .move_to(transformation_notation[a_index]),
            ),
            run_time=1,
        )
        self.wait(1)

        self.play(
            continuous_graph.animate.shift(DOWN * 2),
            Transform(
                transformation_notation[c_index],
                replacement_number["vertical_shift_down"]
                .set_color(shift_replacement_col)
                .move_to(transformation_notation[c_index]),
            ),
            run_time=1,
        )
        self.wait(1)

        self.play(
            continuous_graph.animate.shift(UP * 4),
            Transform(
                transformation_notation[c_index],
                replacement_number["vertical_shift_up"]
                .set_color(shift_replacement_col)
                .move_to(transformation_notation[c_index]),
            ),
            run_time=2,
        )
        self.wait(2)


class TransformationNotation(Scene):
    def construct(self):
        # equation = MathTex(
        #     r"e^{x} = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
        #     substrings_to_isolate="x",
        # )
        # equation.set_color_by_tex("x", YELLOW)
        # self.play(Write(equation))

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
