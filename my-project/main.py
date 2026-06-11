from manim import *

"""
Most of the time, the code for scripting an animation is entirely contained within the
construct() method of a Scene class. Inside construct(), you can create objects, 
display them on screen, and animate them.
"""

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen



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
