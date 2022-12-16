####################################################
# Program: Christmas Greeting Card
# Author: Mohan Dong
# Date: 12/13/2022
# Description: A greeting card for Christmas.
####################################################

# import essential libraries / modules
import turtle
from math import ceil
from random import randint
from time import sleep

# pen instantiation
pen = turtle.Turtle();

# color definition
darkGreen = "#3f9523";
lightGreen = "#e7ffe0";
darkRed = "#bd0000";
mediumRed = "#ff0000";
lightRed = "#ffc4bd";
aqua = "#b8fff7";
yellow = "#fff700";
pink = "#fba2f7";
blue = "#4067fc";
brown = "#a87300";
black = "black";
white = "white";
grey = "grey";

reservedPx = []; # storing reserved positions

# function definition
# utilities
# draw basic shapes
def drawSimple(polygon, length1, length2, pensize, pencolor, fillColor, position):
    # initializing
    pen.setpos(position);
    angle = 360 / int(polygon);
    pen.pencolor(pencolor);
    pen.fillcolor(fillColor);
    pen.pensize(pensize);

    # drawing
    pen.pd();
    pen.begin_fill();
    for i in range(ceil(polygon / 2)):
        pen.forward(length1);
        pen.right(angle);
        pen.forward(length2);
        pen.right(angle);
    pen.end_fill();
    pen.pu();

# draw segments which have specific starting and ending positions
def drawSeg(starting, ending, pensize, pencolor):
    # initializing
    pen.pencolor(pencolor);
    pen.setpos(starting);
    pen.pensize(pensize);

    # drawing
    pen.pd();
    pen.setpos(ending);
    pen.pu();

# draw a pixel 20 * 20
def drawPx(position, color, pensize):
    # initializing
    pen.pencolor(color);
    pen.fillcolor(color);
    pen.setpos(position);
    pen.pensize(pensize);

    # drawing
    pen.pd();
    pen.begin_fill();
    for i in range(4):
        pen.forward(20);
        pen.right(90);
    pen.end_fill();
    pen.pu();

# extending reserved pixels
def extendReservedPx(xInit, yInit, xStep, yStep, limit):
    for i in range(limit):
        if not [xInit, yInit] in reservedPx:
            reservedPx.append([xInit, yInit]);
        xInit += xStep; yInit += yStep;

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

# initializing
def initialize():
    turtle.hideturtle();
    turtle.setup(1000, 1000);
    pen.pu();
    pen.speed("fastest");

    # starting text || title
    for i in range(8, 75, 3):
        pen.write("HAPPY", False, "center", ("Rage", i, "italic"));
        sleep(0.0625);
        pen.clear();
    for i in range(75, 120, 2):
        pen.write("HOLIDAYS", False, "center", ("Rage", i, "italic"));
        sleep(0.0625);
        pen.clear();

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

# basic elements
# cross
def cross(x, y, color):
    drawPx((x, y), color, 1); # center
    drawPx((x, y + 20), color, 1); # upper
    drawPx((x, y - 20), color, 1); # lower
    drawPx((x - 20, y), color, 1); # left
    drawPx((x + 20, y), color, 1); # right

    # making sure no overlapping will occur
    for resX in range(x - 40, x + 41, 20):
        for resY in range(y - 40, y + 41, 20):
            reservedPx.append([(resX, resY)]);

# candyCane
def candyCane():
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

    # extending reserved pixels
    for i in range(-460, -280, 20):
        extendReservedPx(i, -460, 0, 20, 18);

# christmas tree
def christmasTree():
    # leaves
    top = 120;
    for x in range(0, 181, 20):
        for y in range(top, -301, -20):
            drawPx((x, y), darkGreen, 1);
        top -= 60;
    top = 60;
    for x in range(-20, -181, -20):
        for y in range(top, -301, -20):
            drawPx((x, y), darkGreen, 1);
        top -= 60;
    
    # trunk
    for i in range(-320, -421, -20):
        drawPx((0, i), brown, 1);

    # extending reserved pixels
    for i in range(-160, 161, 20):
        extendReservedPx(i, 140, 0, -20, 30);
    
    cross(0, 120, yellow); # adding the star

def gift(x, y, topColor, bottomColor):
    extendReservedPx(x - 20, y - 40, 20, 0, 6); # extend reserved pixels

    # cover
    for i in range(2):
        for i in range(x, x + 101, 20):
            drawPx((i, y), topColor, 1);
        y -= 20;

    # body
    for i in range(2):
        for i in range(x + 20, x + 81, 20):
            drawPx((i, y), bottomColor, 1);
        y -= 20;

    # belt
    y = -340;
    for i in range(2):
        for i in range(x + 40, x + 61, 20):
            drawPx((i, y), yellow, 1);
        y -= 20;

def main():
    print("[program starting]");
    # initializing
    initialize();
    print("[initialized]");

    # elements
    print("[building candy cane]");
    candyCane(); # candyCane
    print("[done]");
    
    # christmas tree
    print("[building christmas tree]");
    christmasTree();
    print("[done]");
    
    # gifts under the christmas tree
    print("[building gifts under christmas tree]");
    gift(-120, -360, darkGreen, mediumRed);
    gift(20, -360, mediumRed, darkGreen);
    print("[done]");

    # snow
    print("[building snowflakes]");
    i = 0
    while i < 20:
        x = randint(-440, 380) // 20 * 20; y = randint(-400, 360) // 20 * 20;
        if not [x, y] in reservedPx:
            cross(x, y, aqua);
            i += 1;
    print("[done]");
    
    # christmas tree lighting
    print("[building lighting for christmas tree]");
    pen.hideturtle();
    color = [yellow, pink, blue, mediumRed, brown, lightGreen, darkRed, lightRed, aqua, white, grey];
    while True:
        userInput = input("Do you want the lighting color be randomly generated? [y/n]");
        if (userInput == 'y'):
            print("[done]");
            while True:
                drawPx((0, 0), color[randint(0, len(color) - 1)], 1);
                drawPx((-20, -60), color[randint(0, len(color) - 1)], 1);
                drawPx((20, -100), color[randint(0, len(color) - 1)], 1);
                drawPx((0, -160), color[randint(0, len(color) - 1)], 1);
                drawPx((-40, -240), color[randint(0, len(color) - 1)], 1);
                drawPx((60, -280), color[randint(0, len(color) - 1)], 1);
        elif (userInput == 'n'):
            print("available color list:", color, "\nenter the index: ");
            drawPx((0, 0), color[int(input())], 1);
            drawPx((-20, -60), color[int(input())], 1);
            drawPx((20, -100), color[int(input())], 1);
            drawPx((0, -160), color[int(input())], 1);
            drawPx((-40, -240), color[int(input())], 1);
            drawPx((60, -280), color[int(input())], 1);
            print("[done]");
        else:
            print("invalid input");
    
if __name__ == '__main__':
    main();