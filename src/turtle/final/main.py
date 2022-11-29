import turtle
import math
from pathlib import Path

# color definition
darkGreen = "#3f9523";
lightGreen = "##e7ffe0";
darkRed = "#bd0000";
mediumRed = "#ff0000";
lightRed = "#ffc4bd";
aqua = "#b8fff7";
yellow = "#fff700";
pink = "#fba2f7";
blue = "#4067fc";
black = "black";
white = "white";

# function definition
# draw basic shapes
def drawSimple(polygon, length1, length2, pensize, pencolor, fillColor, position):
    # initializing
    turtle.setpos(position);
    angle = 360 / int(polygon);
    turtle.pencolor(pencolor);
    turtle.fillcolor(fillColor);
    prevPensize = turtle.pensize();
    turtle.pensize(pensize);

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
    turtle.pensize(prevPensize);

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
def drawSeg(starting, ending, pensize, pencolor):
    # initializing
    turtle.pencolor(pencolor);
    turtle.setpos(starting);
    prevPensize = turtle.pensize();
    turtle.pensize(pensize);

    # drawing
    turtle.pd();
    turtle.setpos(ending);
    turtle.pu();
    
    turtle.pensize(prevPensize);

def main():
    # initializing
    turtle.setup(1000, 1000);
    turtle.pu();
    turtle.speed("fastest");

    # background
    # var
    start = -500; end = 500;
    pencolor = [mediumRed, darkGreen, mediumRed, white];

    # red, green, white stripes
    for i in range(100):
        drawSeg((start, 500), (-500, end), 20, pencolor[i % 4]);
        start += 20; end -= 20;

    drawSimple(4, 920, 920, 5, black, white, (-462.5, 462.5)); # white square

    # grid
    # horizontal
    vertical = -500; horizontal = 500;
    for i in range(50):
        drawSeg((-500, horizontal), (500, horizontal), 1, "grey");
        horizontal -= 20;

    # vertical
    for i in range(50):
        drawSeg((vertical, 500), (vertical, -500), 1, "grey");
        vertical += 20;


    turtle.exitonclick();

if __name__ == '__main__':
    main();