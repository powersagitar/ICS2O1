##########################################################################
# Program: turtle/house.py
# Author: Mohan Dong
# Date: 11/23/2022
# Description: A program to draw a house by using Python Turtle.
##########################################################################

# importing libraries
import turtle 
import math

# defining functions
# draw basic shapes
def drawSimple(polygon, length1, length2, pencolor, fillColor, position):
    # initializing
    turtle.setpos(position);
    angle = 360 / int(polygon);
    turtle.pencolor(pencolor);
    turtle.fillcolor(fillColor);

    # drawing
    turtle.pd();
    turtle.begin_fill();
    for i in range(math.ceil(polygon / 2)):
        turtle.forward(length1);
        turtle.right(angle);
        turtle.forward(length2);
        turtle.right(angle);
    turtle.end_fill();
    turtle.pu();

# regular (non-preset) drawing
def draw(length, heading, pencolor, position):
    turtle.setpos(position); # initializing
    
    # drawing
    turtle.seth(heading);
    turtle.pencolor(pencolor);
    turtle.pd();
    turtle.forward(length);
    turtle.pu();

# draw segments which have specific starting and ending positions
def drawSeg(starting, ending, pencolor):
    # initializing
    turtle.pencolor(pencolor);
    turtle.setpos(starting);

    # drawing
    turtle.pd();
    turtle.setpos(ending);
    turtle.pu();

# draw circles
def drawCircle(color, radius, position):
    turtle.pencolor(color);
    turtle.fillcolor(color);
    turtle.setpos(position);
    turtle.begin_fill();
    turtle.circle(radius);
    turtle.end_fill();

# def main():
# initializing
turtle.setup(1000, 1000); # setting up canvas
turtle.pu();
turtle.speed("fastest"); # code 0 <int>

drawSimple(4, 1000, 400, "blue", "blue", (-500, 500)); # drawing a sky
drawCircle("yellow", 100, (-450, 350)); # drawing a sun
drawSimple(4, 1000, 600, "green", "green", (-500, 100)); # drawing the ground
drawSimple(4, 600, 500, "grey", "grey", (-350, 200)); # drawing bottom rectangle

# drawing the roof
turtle.fillcolor("red");
turtle.begin_fill();
draw(250, 55, "red", (-350, 200));
draw(600, 0, "red", turtle.pos());
posTmp0 = turtle.pos();
draw(250, 235, "red", turtle.pos());
turtle.end_fill();

# drawing top-right triangle
turtle.fillcolor("yellow");
turtle.begin_fill();
draw(200, 10, "yellow", turtle.pos());
posTmp1 = turtle.pos();
drawSeg(posTmp1, posTmp0, "yellow"); 
turtle.end_fill();

# drawing right parallelogram
turtle.fillcolor("brown");
turtle.begin_fill();
drawSeg(posTmp1, (446.96, -265.27), "brown");
drawSeg(turtle.pos(), (250, -300), "brown");
drawSeg(turtle.pos(), (250, 200), "brown");
drawSeg(turtle.pos(), posTmp1, "brown");
turtle.end_fill();

# drawing windows
turtle.seth(0);
drawSimple(4, 150, 100, "blue", "blue", (-250, 100));
turtle.width(5);
draw(100, 270, "grey", (-175, 100));
turtle.width(2.5);
draw(150, 0, "grey", (-250, 50));

# drawing doors
drawSimple(4, 100, 250, "white", "white", (100, -50)); # door
drawCircle("grey", 7, (170, -150)); # handle

turtle.exitonclick();
