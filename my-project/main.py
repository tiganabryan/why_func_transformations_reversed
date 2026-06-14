from manim import *
from manim_themes.manim_theme import apply_theme
from numpy import typing
from typing import Callable, Any

# "Most of the time, the code for scripting an animation is entirely contained within the
# construct() method of a Scene class. Inside construct(), you can create objects,
# display them on screen, and animate them.

# All animations must reside within the construct() method of a class derived from Scene.
# Other code, such as auxiliary or mathematical functions, may reside outside the class."
# – manim docs


class BaseTransformationScene(Scene):
    """
    Quickly create my function transformation animations
    """

    def __init__(
        self,
        plot_length: int | float = 8,
        # parent_function=lambda x: np.sin(x),
        parent_function: Callable = np.sin,  # e.g. np.log, np.sqrt, etc.
        vert_stretch: int | float = 1,
        vert_shift: int | float = 0,
        horz_stretch: int | float = 1,
        horz_shift: int | float = 0,
        x_axis_length: int | float = None,
        function_length: int | float = None,
        **kwargs,
    ):
        self.plot_length = plot_length
        self.x_axis_length = x_axis_length

        self.parent_function = parent_function
        self.function_length = function_length
        self.vert_stretch = vert_stretch
        self.vert_shift = vert_shift
        self.horz_stretch = horz_stretch
        self.horz_shift = horz_shift

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
    def transformed_function_callable(self):
        return lambda x: (
            # fmt: off
            self.vert_stretch.get_value() * self.parent_function(self.horz_stretch.get_value() * (x - self.horz_shift.get_value())) + self.vert_shift.get_value()
            # fmt: on
            # python version of y=afk(x-d)+c
        )

    @property
    def graph_config(self):
        return {
            "function": self.transformed_function_callable,
            "color": "PURPLE",
            "x_range": [0, self.function_length or self.plot_length],
        }

    def apply_vert_stretch(self, value: int | float = 1):
        self.vert_stretch = value
        self.rerender_graph()

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

        self.vert_stretch = ValueTracker(1)
        self.vert_shift = ValueTracker(0)
        self.horz_stretch = ValueTracker(1)
        self.horz_shift = ValueTracker(0)

        # create coordinate system obj
        self.axes = Axes(
            **self.axes_config,
        )

        # create function's graph obj
        for val in self.graph_config:
            print(self.graph_config[val], type(self.graph_config[val]))

        self.function_object = self.axes.plot(
            function=self.graph_config["function"],
            color=self.graph_config["color"],
            x_range=self.graph_config["x_range"],
        )

        # dotted line version
        # dotted_sin_func = DashedVMobject(
        #     function_object,
        #     num_dashes=200,
        #     # dash_length=0.001,
        #     # dashed_ratio=0.1,
        #     equal_lengths=True,
        #     color="#9BE1FA",
        # )

        # add colour fill to graph test
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

        def rerender_graph(self):
            new_graph = self.axes.plot(**self.graph_config)
            self.function_object.become(new_graph)

        self.function_object.add_updater(
            lambda m: m.become(
                self.axes.plot(
                    self.transformed_function_callable,
                    color=PURPLE,
                    x_range=[0, self.plot_length],
                )
            )
        )

    def construct(self):
        return super().construct()


class VerticalTransformationScene(BaseTransformationScene):
    def setup(self):
        self.plot_length = 6
        # self.function_length = 4

        super().setup()

    def construct(self):
        self.wait(1)

        self.play(
            self.vert_stretch.animate.set_value(3),
            # self.function_object.animate.stretch(3, dim=1),
            Transform(
                mobject=self.general_transformation_equation[self.a_index],
                target_mobject=MathTex("2")
                .set_color(YELLOW)
                .move_to(self.general_transformation_equation[self.a_index])
                .shift(UP * 0.06),
            ),
            run_time=1.5,
        )
        self.wait(1)

        self.play(
            self.vert_stretch.animate.set_value(0.5),
            Transform(
                mobject=self.general_transformation_equation[self.a_index],
                target_mobject=MathTex(r"\tfrac{1}{2}")
                .set_color(YELLOW)
                .move_to(self.general_transformation_equation[self.a_index]),
            ),
            run_time=1,
        )
        self.wait(1)

        self.play(
            self.vert_shift.animate.set_value(-2),
            # self.function_object.animate.shift(DOWN * 2),
            Transform(
                mobject=self.general_transformation_equation[self.c_index],
                target_mobject=MathTex("-2")
                .set_color(ORANGE)
                .move_to(self.general_transformation_equation[self.c_index])
                .shift(LEFT * 0.1)
                .shift(UP * 0.02),
            ),
            run_time=1,
        )
        self.wait(1)

        self.play(
            self.vert_shift.animate.set_value(2),
            Transform(
                mobject=self.general_transformation_equation[self.c_index],
                target_mobject=MathTex("+2")
                .set_color(ORANGE)
                .move_to(self.general_transformation_equation[self.c_index]),
                # .shift(LEFT * 0.1),
            ),
            run_time=2,
        )
        self.wait(2)


class HorizontalTransformationScene(BaseTransformationScene):
    def setup(self):
        self.plot_length = 7
        # self.function_length = 4

        super().setup()

    def construct(self):
        self.wait(1)

        self.play(
            # Transform(self.function_object) # replace animation with a real transformation on the graph obj eventually
            # self.function_object.animate.shift(RIGHT * 2),
            self.horz_shift.animate.set_value(2),
            run_time=1,
        )

        self.play(
            Transform(
                mobject=self.general_transformation_equation[self.d_index],
                target_mobject=MathTex("-2)")
                .set_color("#FF4848")
                .move_to(self.general_transformation_equation[self.d_index]),
            )
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
