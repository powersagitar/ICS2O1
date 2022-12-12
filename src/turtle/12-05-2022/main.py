############################################
# Program: screensaver.py
# Date: 12/05/2022
# Author: Mohan Dong
# Description: Oval screensaver.
############################################

from random import randint
import turtle

def main():
    # initialize
    turtle.title("Group 2");
    turtle.setup(1000, 1000);
    turtle.color("green");
    turtle.begin_fill();
    turtle.shape("circle");
    turtle.shapesize(8, 4, 1);
    turtle.end_fill();
    x = randint(200, 300); y = 240;
    turtle.pu();
    turtle.setpos(x, y);
    xStep = 2; yStep = -3;

    # bouncing
    while True:
        # reverse direction
        if x >= 455 or x <= -455:
            print("line 33")
            xStep = -xStep;
        if y >= 410 or y <= -410:
            print("line 36")
            yStep = -yStep;
        
        # update pen position
        x += xStep; y += yStep;
        turtle.setpos(x, y);

        print("x:", x, "y:", y, "\nxStep:", xStep, "yStep:", yStep); # log

if __name__ == '__main__':
    main();