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

pen = turtle.Turtle(); # pen instantiation

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
    pen.setpos(position); # set starting position
    angle = 360 / int(polygon); # angle value for each corner
    pen.pencolor(pencolor); # set pen color
    pen.fillcolor(fillColor); # set fill color
    pen.pensize(pensize); # set pen size

    # drawing
    pen.pd(); # drop the pen
    pen.begin_fill(); # start filling

    # body part || print the shape
    for i in range(ceil(polygon / 2)):
        pen.forward(length1);
        pen.right(angle);
        pen.forward(length2);
        pen.right(angle);

    pen.end_fill(); # stop filling
    pen.pu(); # lift the pen

# draw segments which have specific starting and ending positions
def drawSeg(starting, ending, pensize, pencolor):
    # initializing
    pen.pencolor(pencolor); # set pen color
    pen.setpos(starting); # set first end point
    pen.pensize(pensize); # set pen size

    # drawing
    pen.pd(); # drop the pen
    pen.setpos(ending); # set second end point
    pen.pu(); # lift the pen

# draw a pixel 20 * 20
def drawPx(position, color, pensize):
    # initializing
    pen.pencolor(color); # set pen color
    pen.fillcolor(color); # set fill color
    pen.setpos(position); # set starting position
    pen.pensize(pensize); # set pensize

    # drawing
    pen.pd(); # drop the pen
    pen.begin_fill(); # start filling

    # body part || draw a pixel
    for i in range(4):
        pen.forward(20);
        pen.right(90);

    pen.end_fill(); # stop filling
    pen.pu(); # life the pen

# extending reserved pixels
def extendReservedPx(xInit, yInit, xStep, yStep, limit):
    for i in range(limit): # set iteration counter
        if not [xInit, yInit] in reservedPx: # data duplication check
            reservedPx.append([xInit, yInit]); # append new data
        xInit += xStep; yInit += yStep; # move to next target pixel

# draw the grid
def grid(color):
    vertical = -500; horizontal = 500; # set initial value

    for i in range(50): # set iteration counter
        drawSeg((-500, horizontal), (500, horizontal), 1, color); # draw a horizontal line
        drawSeg((vertical, 500), (vertical, -500), 1, color); # draw a vertical line
        horizontal -= 20; vertical += 20; # move to next target lines

# initializing
def initialize():
    turtle.hideturtle(); # hide turtle
    turtle.setup(1000, 1000); # set up canvas
    pen.pu(); # lift the pen
    pen.speed("fastest"); # set pen speed to fastest

    # starting text || title
    # happy
    for i in range(8, 75, 3):
        pen.write("HAPPY", False, "center", ("Rage", i, "italic")); # print text
        sleep(0.0625); # delay for vision persistence
        pen.undo(); # clear screen for next output

    # holidays
    for i in range(75, 120, 2):
        pen.write("HOLIDAYS", False, "center", ("Rage", i, "italic")); # print text
        sleep(0.0625); # delay for vision persistence
        pen.undo(); # clear screen for next output

    # background
    # var definition
    start = -500; end = 500;
    pencolor = [mediumRed, darkGreen, mediumRed, white];

    # red, green, white stripes
    for i in range(100):
        drawSeg((start, 500), (-500, end), 20, pencolor[i % 4]); # draw colored stripes
        start += 20; end -= 20; # navigate to next target line

    drawSimple(4, 920, 920, 5, black, white, (-462.5, 462.5)); # white square || white background

    grid(grey); # grid

# basic elements
# cross
def cross(x, y, color):
    drawPx((x, y), color, 1); # center
    drawPx((x, y + 20), color, 1); # top
    drawPx((x, y - 20), color, 1); # bottom
    drawPx((x - 20, y), color, 1); # left
    drawPx((x + 20, y), color, 1); # right

    # making sure no overlapping will occur || traverse through all pixels in a 5px by 5px space
    for resX in range(x - 40, x + 41, 20):
        for resY in range(y - 40, y + 41, 20):
            reservedPx.append([(resX, resY)]);

# candy cane
def candyCane():
    # blocks on lefter left
    y = -400; # var definition
    for i in range(7):
        drawPx((-420, y), mediumRed, 1); # draw and color the pixel
        y += 40; # navigate to next target pixel
    
    # blocks on righter left
    y = -380; # var definition
    for i in range(7):
        drawPx((-400, y), mediumRed, 1); # draw and color the pixel
        y += 40; # navigate to next target pixel
    
    # blocks on top
    x = -360; # var definition
    for i in range(2):
        drawPx((x, -140), mediumRed, 1); # draw and color the pixel
        x += 40; # navigate to next target pixel
    
    # blocks on right
    drawPx((-320, -180), mediumRed, 1); # draw and color the pixels

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

    # extending reserved pixels || traverse through the rectangular area where the candy cane is
    for i in range(-460, -280, 20):
        extendReservedPx(i, -460, 0, 20, 18);

# christmas tree
def christmasTree():
    # leaves
    # middle and right half
    top = 120;
    # traverse all the pixels where the christmas tree will be
    for x in range(0, 181, 20):
        for y in range(top, -301, -20):
            drawPx((x, y), darkGreen, 1); # draw and color the pixel
        top -= 60; # nevigate to the next target pixel
    
    # left half
    top = 60;
    # traverse all the pixels where the christmas tree will be
    for x in range(-20, -181, -20):
        for y in range(top, -301, -20):
            drawPx((x, y), darkGreen, 1); # draw and color the pixel
        top -= 60; # nevigate to the next target pixel
    
    # trunk
    # traverse all the pixels where the trunk will be
    for i in range(-320, -421, -20):
        drawPx((0, i), brown, 1); # draw and color the trunk

    # extending reserved pixels || traverse a rectangular area where the christmas tree is
    for i in range(-160, 161, 20):
        extendReservedPx(i, 140, 0, -20, 30);
    
    cross(0, 120, yellow); # adding the yellow star on top

def gift(x, y, topColor, bottomColor):
    extendReservedPx(x - 20, y - 40, 20, 0, 6); # extend reserved pixels || traverse through a rectangular area where the gifts are

    # cover
    for i in range(2):
        for i in range(x, x + 101, 20):
            drawPx((i, y), topColor, 1);
        y -= 20; # navigate to next target pixel

    # body
    for i in range(2):
        for i in range(x + 20, x + 81, 20):
            drawPx((i, y), bottomColor, 1);
        y -= 20; # navigate to next target pixel

    # belt
    y = -340;
    for i in range(2):
        for i in range(x + 40, x + 61, 20):
            drawPx((i, y), yellow, 1);
        y -= 20; # navigate to next target pixel

def main():
    print("[program starting]");
    initialize(); # initialize canvas
    print("[initialized]");

    # elements
    print("[building candy cane]");
    candyCane(); # candy cane
    print("[done]");
    
    print("[building christmas tree]");
    christmasTree(); # christmas tree
    print("[done]");
    
    # gifts under the christmas tree
    print("[building gifts under christmas tree]");
    gift(-120, -360, darkGreen, mediumRed); # left side
    gift(20, -360, mediumRed, darkGreen); # right side
    print("[done]");

    # snow
    print("[building snowflakes]");
    i = 0 # define iteration var
    while i < 20:
        x = randint(-440, 380) // 20 * 20; y = randint(-400, 360) // 20 * 20; # make sure generated pixels are on the grid
        if not [x, y] in reservedPx: # overlapping check
            cross(x, y, aqua); # draw a snowflake
            i += 1; # update iteration var
    print("[done]");
    
    # christmas tree lighting
    print("[building lighting for christmas tree]");
    pen.hideturtle(); # hide pen
    color = [yellow, pink, blue, mediumRed, brown, lightGreen, darkRed, lightRed, aqua, white, grey]; # define available lighting colors
    while True:
        userInput = input("Do you want the lighting color be randomly generated? [y/n]"); # mode selector
        # random snow
        if (userInput == 'y'):
            print("[done]");
            while True:
                drawPx((0, 0), color[randint(0, len(color) - 1)], 1);
                drawPx((-20, -60), color[randint(0, len(color) - 1)], 1);
                drawPx((20, -100), color[randint(0, len(color) - 1)], 1);
                drawPx((0, -160), color[randint(0, len(color) - 1)], 1);
                drawPx((-40, -240), color[randint(0, len(color) - 1)], 1);
                drawPx((60, -280), color[randint(0, len(color) - 1)], 1);
        
        # manual snow
        elif (userInput == 'n'):
            print("available color list:", color, "\nenter the index: ");
            drawPx((0, 0), color[int(input())], 1);
            drawPx((-20, -60), color[int(input())], 1);
            drawPx((20, -100), color[int(input())], 1);
            drawPx((0, -160), color[int(input())], 1);
            drawPx((-40, -240), color[int(input())], 1);
            drawPx((60, -280), color[int(input())], 1);
            print("[done]");

        # undefined input
        else:
            print("invalid input");
    
if __name__ == '__main__':
    main();