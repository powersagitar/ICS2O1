import turtle
import math
from pathlib import Path
from random import randint

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
grey = "grey";

# function definition
# utilities
# initializing
def initialize():
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

    grid(grey); # grid
    

# draw the grid
def grid(color):
# horizontal
    vertical = -500; horizontal = 500;
    for i in range(50):
        drawSeg((-500, horizontal), (500, horizontal), 1, color);
        horizontal -= 20;

    # vertical
    for i in range(50):
        drawSeg((vertical, 500), (vertical, -500), 1, color);
        vertical += 20;

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

# draw a pixel 20 * 20
def drawPx(position, color, pensize):
    # initializing
    turtle.pencolor(color);
    turtle.fillcolor(color);
    turtle.setpos(position);
    prevPensize = turtle.pensize();
    turtle.pensize(pensize);

    # drawing
    turtle.pd();
    turtle.begin_fill();
    for i in range(4):
        turtle.forward(20);
        turtle.right(90);
    turtle.end_fill();
    turtle.pu();
    turtle.pensize(prevPensize);

# basic elements
# snow
def snow(x, y):
    drawPx((x, y), aqua, 1); # center
    drawPx((x, y + 20), aqua, 1); # upper
    drawPx((x, y - 20), aqua, 1); # lower
    drawPx((x - 20, y), aqua, 1); # left
    drawPx((x + 20, y), aqua, 1); # right

# candy
def candy():
    # blocks on lefter left
    y = -400;
    for i in range(7):
        drawPx((-420, y), mediumRed, 1);
        y += 40;
    
    # blocks on righter left
    y = -380;
    for i in range(7):
        drawPx((-400, y), mediumRed, 1);
        y += 40;
    
    # blocks on top
    x = -360;
    for i in range(2):
        drawPx((x, -140), mediumRed, 1);
        x += 40;
    
    # blocks on right
    drawPx((-320, -180), mediumRed, 1);

    # border
    drawSeg((-420, -420), (-420, -160), 3, black); # lefter left
    drawSeg((-380, -400), (-380, -160), 3, black); # righter left
    drawSeg((-420, -420), (-400, -420), 3, black); # bottom
    drawSeg((-400, -420), (-380, -400), 3, black); # bottom slope
    drawSeg((-420, -160), (-400, -140), 3, black); # top slope
    drawSeg((-400, -140), (-300, -140), 3, black); # upper top
    drawSeg((-380, -160), (-320, -160), 3, black); # lower top
    drawSeg((-320, -160), (-320, -200), 3, black); # lefter right
    drawSeg((-320, -200), (-300, -200), 3, black); # lower right
    drawSeg((-300, -140), (-300, -200), 3, black); # righter right

def main():
    initialize(); # initializing
    
    # snow
    for i in range(10):
        snow((randint(-440, 380) * 20) // 20, (randint(-440, 360) * 20) // 20); # snow is not on grid

    candy(); # candy

    turtle.exitonclick();

if __name__ == '__main__':
    main();