############################################
# Program: screensaver.py
# Date: 12/05/2022
# Author: Mohan Dong
# Description: Oval screensaver.
############################################

from random import randint
import turtle

def initialize(color):
    turtle.title("Group 2");
    turtle.setup(1000, 1000);
    turtle.speed("fastest");
    turtle.clear();
    turtle.color(color);
    turtle.begin_fill();
    turtle.shape("circle");
    turtle.shapesize(8, 4, 1);
    turtle.end_fill();

def main():
    # initialize
    initialize("green");
    x = randint(200, 300); y = 240;
    turtle.pu();
    turtle.setpos(x, y);
    xReverse = False; yReverse = False;
    xStep = 2; yStep = -3;

    # bouncing
    while True:
        # boucing eligibility check
        if x > -5 and x < 5:
            print("line 35")
            xReverse = False;
        if y > -5 and y < 5:
            print("line 38")
            yReverse = False;

        # reverse direction
        if (x >= 455 or x <= -455) and xReverse == False:
            print("line 43")
            xStep = -xStep;
            xReverse = True;
        if (y >= 410 or y <= -410) and yReverse == False:
            print("line 47")
            yStep = -yStep;
            yReverse = True;
        
        # update pen position
        x += xStep; y += yStep;
        turtle.setpos(x, y);

        print("x:", x, "y:", y, "\nxStep:", xStep, "yStep:", yStep, "\nreverse status:", "x:", xReverse, "y:", yReverse); # log


if __name__ == '__main__':
    main();