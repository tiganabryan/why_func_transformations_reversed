# made with the manim animation library

![animation](/VerticalTransformationScene.gif)

updates:
june 14th
Originally the width of the graph colouring was dependent on the graph's width or the x-axis' length, but that introduced some bugs.

My solution was a state driven approach to maintain sync between graph rendering, area shading, and annotations.

As the project grew, I wanted to be able to link the graph's transformations with other visual elements – area shading, labels. They needed to depend on the underlying function definition.

I implemented this by moving transformation parameters into ValueTracker objects, triggering updates to elements with any change of the graph's state, animating side effects instead of directly writing them in

Here's to more math animations
