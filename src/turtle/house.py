# importing libraries
import turtle 
import math

# defining functions
def drawSimple(polygon, length1, length2, penColor, fillColor, xStart, yStart):
    turtle.setpos(xStart, yStart);
    angle = 360 / int(polygon);
    turtle.pencolor(penColor);
    turtle.fillcolor(fillColor);

    turtle.pd();
    turtle.begin_fill();
    for i in range(math.ceil(polygon / 2)):
        turtle.forward(length1);
        turtle.right(angle);
        turtle.forward(length2);
        turtle.right(angle);
    turtle.end_fill();
    turtle.pu();

def drawIsosceles(length, angle, rotation, xStart, yStart):
    turtle.setpos(xStart, yStart);
    turtle.pd();

    for i in range(rotation):
        turtle.forward(length);
        turtle.right(angle);
    turtle.pu();

# def main()
turtle.setup(1000, 1000); # setting up canvas
turtle.pu();
turtle.speed("fastest"); # code 0 <int>

drawSimple(4, 1000, 400, "blue", "blue", -500, 500); # drawing a sky

# drawing a sun
turtle.setpos(-450, 350)
turtle.pencolor("yellow");
turtle.fillcolor("yellow");
turtle.begin_fill()
turtle.circle(100); 
turtle.end_fill();

drawSimple(4, 1000, 600, "green", "green", -500, 100); # drawing the gound
drawSimple(4, 600, 500, "black", "black", -300, 200); # drawing rectangular part of the house

turtle.exitonclick();