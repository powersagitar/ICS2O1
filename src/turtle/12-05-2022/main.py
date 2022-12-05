from random import randint
import turtle

def initialize(color):
    turtle.title("Group 2");
    turtle.setup(1000, 1000);
    turtle.pu;
    turtle.speed("fastest");
    turtle.clear();
    turtle.color(color);
    turtle.begin_fill();
    turtle.shape("circle");
    turtle.shapesize(8, 4, 1);
    turtle.end_fill();

def oval(position, color):
    turtle.pu();
    turtle.setpos(position);
    

def main():
    initialize();
    x = randint(200, 300); y = 240;
    oval((x, y), "green");
    xReverse = False; yReverse = False;
    xStep = 2; yStep = -3;

    while True:
        if x > -450 and x < 450:
            print("line 29")
            xReverse = False;
        if y > -450 and y < 450:
            print("line 32")
            yReverse = False;

        if (x >= 500 or x <= -500) and xReverse == False:
            print("line 36")
            xStep = -xStep;
            xReverse = True;
        if (y >= 500 or y <= -500) and yReverse == False:
            print("line 40")
            yStep = -yStep;
            yReverse = True;
        
        x += xStep; y += yStep;
        oval((x, y), "green");

        print("x:", x, "y:", y, "\nxStep:", xStep, "yStep:", yStep, "\nreverse status:", "x:", xReverse, "y:", yReverse);


if __name__ == '__main__':
    main();