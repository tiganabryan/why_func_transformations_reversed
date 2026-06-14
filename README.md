# WIP. explainer video on the connection between reference frames in physics and transformations of functions
Math has a reputation for being a collection of (bad) recipes to be memorized, when that **could not** be further from the truth!

The idea that certain math operations done to functions appear "reversed" isn't just an off-hand fact to memorize; updating and nesting coordinate systems inside each other is at the core of how we describe physical phenomena.

I want to share how the reasoning behind this extends into linear algebra, visual arts, and the physical sciences. So, here I am... Programming math animations. Such is life

![animation](/VerticalTransformationScene.gif)

## updates:

### june 14th
  #### completed:
  - equation and graph animations
  #### to-do:
  - animate nested coordinate systems, corresponding diagrams, and a real world example

  #### design choices
  - Originally the width of the graph colouring was dependent on the graph's width or the x-axis' length, but that introduced some bugs.
  
  - As the project grew, I wanted to be able to link the graph's transformations with other visual elements – area shading, labels. They needed to depend on the underlying function definition.
  
  - My solution was a state driven approach to maintain sync between graph rendering, area shading, and annotations.
  
  - I implemented this by moving transformation parameters into ValueTracker objects, triggering updates to elements with any change of the graph's state, and animating side effects instead of directly writing them in
  
  Hopefully more additions coming soon if I have time!
