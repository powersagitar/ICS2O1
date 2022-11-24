# `turtle/house`
Table of Contents
- [`turtle/house`](#turtlehouse)
  - [Functions](#functions)
    - [drawSimple](#drawsimple)
    - [draw](#draw)
    - [drawSeg](#drawseg)
    - [drawCircle](#drawcircle)


## Functions
### drawSimple
`drawSimple(<int> polygon, <float> length1, <float2> length2, <string> pencolor, <string> fillcolor, <float> position)`  
A function for drawing basic shapes.
* `<int> polygon`: The amount of sides of a basic shape. Eg. If wanted to draw a square, enter `4`.
* `<float> length1`: The length of top and bottom sides.
* `<float> length2`: The length of left and right sides.
* `<string> pencolor`: The initial pen color.
* `<string> fillcolor`: The initial fill color.
* `<float> position`: The initial pen position.

### draw
`draw(<float> length, <float> heading, <string> pencolor, <float> position)`  
A function for regular (non-preset) drawing.
* `<float> length`: The length of the segment which you wanted to draw.
* `<float> heading`: The initial heading of turtle.
* `<string> pencolor`: The initial pen color.
* `<float> position`: The initial pen position.

### drawSeg
`drawSeg(<float> starting, <float> ending, <string> pencolor)`  
Draw segments which have specific starting and ending positions.
* `<float> starting`: The starting position of the segment.
* `<float> ending`: The ending position of the segment.
* `<string> pencolor`: The initial pen color.

### drawCircle
`drawCircle(<string> color, <float> radius, <float> position)`  
Draw circles by using Turtle built-in functions.
* `<string> color`: The initial pen color and the initial fill color.
* `<float> radius`: The radius of the circle you wanted to draw.
* `<float> position`: The position of the circle you wanted to draw.