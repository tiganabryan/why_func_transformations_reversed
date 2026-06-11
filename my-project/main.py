from manim import *

"""
Most of the time, the code for scripting an animation is entirely contained within the
construct() method of a Scene class. Inside construct(), you can create objects, 
display them on screen, and animate them.

All animations must reside within the construct() method of a class derived from Scene.
Other code, such as auxiliary or mathematical functions, may reside outside the class.
"""


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # "Create" is what displays the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen


class HelloLaTeX(Scene):
    def construct(self):
        tex = Tex(r"f(x)", font_size=144)
        self.add(tex)


class Fading(Scene):
    def construct(self):
        tex_in = Tex("f(x)").move_to(2.5 * UP)
        self.play(Write(tex_in))
        # tex_out = Tex("Fade", "Out").scale(3)
        # self.play(FadeIn(tex_in, shift=DOWN, scale=0.66))
        # self.play(ReplacementTransform(tex_in, tex_out))
        # self.play(
        #     LaggedStart(
        #         *(FadeIn(tex_in, scale=1.5) for char in tex_in),
        #         # shift=2,
        #         lag_ratio=0.1,
        #         run_time=2
        #     )
        # ),
        # self.wait(1)


class LaggingGroup(Scene):
    def construct(self):
        circles = (
            VGroup(*[Circle(radius=1, color=TEAL, fill_opacity=0.5) for j in range(10)])
            .arrange_in_grid(2, 5)
            .scale(0.5)
        )
        tex = Text("lag_ratio=0").move_to(2.5 * UP)
        self.play(Write(tex))
        self.play(AnimationGroup(*[FadeIn(s) for s in circles], lag_ratio=0))
        self.wait(2)
        self.play(AnimationGroup(*[FadeOut(s) for s in circles], lag_ratio=0))
        self.play(FadeOut(tex))

        circles = (
            VGroup(*[Circle(radius=1, color=TEAL, fill_opacity=0.5) for j in range(10)])
            .arrange_in_grid(2, 5)
            .scale(0.5)
        )
        tex = Text("lag_ratio=0.5").move_to(2.5 * UP)
        self.play(Write(tex))
        self.play(AnimationGroup(*[FadeIn(s) for s in circles], lag_ratio=0.5))
        self.wait(2)
        self.play(AnimationGroup(*[FadeOut(s) for s in circles], lag_ratio=0.5))
        self.play(FadeOut(tex))

        circles = (
            VGroup(*[Circle(radius=1, color=TEAL, fill_opacity=0.5) for j in range(10)])
            .arrange_in_grid(2, 5)
            .scale(0.5)
        )
        tex = Text("lag_ratio=1").move_to(2.5 * UP)
        self.play(Write(tex))
        self.play(AnimationGroup(*[FadeIn(s) for s in circles], lag_ratio=1))
        self.wait(2)
        self.play(AnimationGroup(*[FadeOut(s) for s in circles], lag_ratio=1))
        self.play(FadeOut(tex))


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
