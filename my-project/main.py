from manim import *
from manim_themes.manim_theme import apply_theme

"""
Most of the time, the code for scripting an animation is entirely contained within the
construct() method of a Scene class. Inside construct(), you can create objects, 
display them on screen, and animate them.

All animations must reside within the construct() method of a class derived from Scene.
Other code, such as auxiliary or mathematical functions, may reside outside the class.
"""


# class ThemeExample(Scene):
#     # def setup(self):
#     #     theme = "tokyonight"
#     #     apply_theme(manim_scene=self, theme_name=theme, light_theme=True)

#     def construct(self):
#         my_text = Tex("af(x-d)+c")
#         # maroon_text = Tex("af(x-d)+c", color=PINK)
#         # maroon_text.next_to(my_text, DOWN)

#         text_group = VGroup(my_text).move_to(ORIGIN)

#         self.play(FadeIn(text_group), run_time=3)


# from manim import *


class DashedGraphScene(Scene):
    def construct(self):
        # 1. Create the coordinate axes
        axes = Axes(
            x_range=[0, 12, 1],
            y_range=[-2, 2, -2],
            axis_config={"include_tip": False},
        )

        # 2. Generate a standard continuous graph (e.g., f(x) = sqrt(x))
        # Note: DottedVMobject is best for functions.
        # For discrete data, use axes.plot_line_graph() with add_vertex_dots=False
        continuous_graph = axes.plot(lambda x: np.sin(x), color=BLUE)

        # 3. Convert the graph to a dashed/dotted line
        dashed_graph = DashedVMobject(
            continuous_graph,
            num_dashes=200,
            # dash_length=0.001,
            dashed_ratio=0.1,
            equal_lengths=True,
        )
        # graph,

        # 4. Add to the scene and animate
        self.play(Create(axes), run_time=0.4)
        self.play(Create(dashed_graph), run_time=5)
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

        self.play(Write(transformation_notation))

        self.play(FadeToColor(transformation_notation[2], color=PURPLE, run_time=1))
        # self.wait(duration=2)
        self.play(Transform(transformation_notation, isolated_input, run_time=1))
        self.wait(duration=3)

        # self.play()

        # self.wait(duration=3)

        # transformation_notation.set_color_by_tex("k(x-d)", BLUE)
        # self.add(isolated_input)

        # isolated_input = MathTex("y=af\color{blue}{k(x-d)}+c")
        # isolated_output = Tex("")
        # self.add(transformation_notation)
        # self.wait(duration=3)
        # self.play(Transform(transformation_notation, isolated_input))


# class CreateCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
#         self.play(Create(circle))  # "Create" is what displays the circle on screen


# class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

#         square = Square()  # create a square
#         square.rotate(PI / 4)  # rotate a certain amount

#         self.play(Create(square))  # animate the creation of the square
#         self.play(Transform(square, circle))  # interpolate the square into the circle
#         self.play(FadeOut(square))  # fade out animation


# class SquareAndCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

#         square = Square()  # create a square
#         square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

#         square.next_to(circle, RIGHT, buff=0.5)  # set the position
#         self.play(Create(circle), Create(square))  # show the shapes on screen


# class AnimatedSquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         square = Square()  # create a square

#         self.play(Create(square))  # show the square on screen
#         self.play(square.animate.rotate(PI / 4))  # rotate the square
#         self.play(Transform(square, circle))  # transform the square into a circle
#         self.play(
#             square.animate.set_fill(PINK, opacity=0.5)
#         )  # color the circle on screen


# class HelloLaTeX(Scene):
#     def construct(self):
#         tex = Tex(r"f(x)", font_size=144)
#         self.add(tex)


# class Fading(Scene):
#     def construct(self):
#         tex_in = Tex("f(x)").move_to(2.5 * UP)
#         self.play(Write(tex_in))
#         # tex_out = Tex("Fade", "Out").scale(3)
#         # self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
#         # self.play(ReplacementTransform(tex_in, tex_out))
#         # self.play(
#         #     LaggedStart(
#         #         *(FadeIn(tex_in, scale=1.5) for char in tex_in),
#         #         # shift=2,
#         #         lag_ratio=0.1,
#         #         run_time=2
#         #     )
#         # ),
#         # self.wait(1)


# class LaggingGroup(Scene):
#     def construct(self):
#         circles = (
#             VGroup(*[Circle(radius=1, color=TEAL, fill_opacity=0.5) for j in range(10)])
#             .arrange_in_grid(2, 5)
#             .scale(0.5)
#         )
#         tex = Text("lag_ratio=0").move_to(2.5 * UP)
#         self.play(Write(tex))
#         self.play(AnimationGroup(*[FadeIn(s) for s in circles], lag_ratio=0))
#         self.wait(2)
#         self.play(AnimationGroup(*[FadeOut(s) for s in circles], lag_ratio=0))
#         self.play(FadeOut(tex))

#         circles = (
#             VGroup(*[Circle(radius=1, color=TEAL, fill_opacity=0.5) for j in range(10)])
#             .arrange_in_grid(2, 5)
#             .scale(0.5)
#         )
#         tex = Text("lag_ratio=0.5").move_to(2.5 * UP)
#         self.play(Write(tex))
#         self.play(AnimationGroup(*[FadeIn(s) for s in circles], lag_ratio=0.5))
#         self.wait(2)
#         self.play(AnimationGroup(*[FadeOut(s) for s in circles], lag_ratio=0.5))
#         self.play(FadeOut(tex))

#         circles = (
#             VGroup(*[Circle(radius=1, color=TEAL, fill_opacity=0.5) for j in range(10)])
#             .arrange_in_grid(2, 5)
#             .scale(0.5)
#         )
#         tex = Text("lag_ratio=1").move_to(2.5 * UP)
#         self.play(Write(tex))
#         self.play(AnimationGroup(*[FadeIn(s) for s in circles], lag_ratio=1))
#         self.wait(2)
#         self.play(AnimationGroup(*[FadeOut(s) for s in circles], lag_ratio=1))
#         self.play(FadeOut(tex))


if __name__ == "main":
    import os
    from pathlib import Path

    FLAGS = "-pqm"
    SCENE = "ThemeExample"

    file_path = Path(__file__).resolve()
    os.system(f"manim {Path(__file__).resolve()} {SCENE} {FLAGS}")


# from manim import *
# class DefaultTemplate(Scene):
#     def construct(self):
#         circle = Circle()  # create a circle
#         circle.set_fill(PINK, opacity=0.5)  # set color and transparency

#         square = Square()  # create a square
#         square.flip(RIGHT)  # flip horizontally
#         square.rotate(-3 * TAU / 8)  # rotate a certain amount

#         self.play(Create(square))  # animate the creation of the square
#         self.play(Transform(square, circle))  # interpolate the square into the circle
#         self.play(FadeOut(square))  # fade out animation
