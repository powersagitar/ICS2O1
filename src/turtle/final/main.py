############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle
from random import randint
from math import sqrt

class CatcherMovement:
    @staticmethod
    def left():
        if not catcher.xcor() <= -387:
            catcher.setpos(catcher.xcor() - 10, catcher.ycor())
    
    @staticmethod
    def right():
        if not catcher.xcor() >= 387:
            catcher.setpos(catcher.xcor() + 10, catcher.ycor())

    @staticmethod
    def up():
        if not catcher.ycor() >= 387:
            catcher.setpos(catcher.xcor(), catcher.ycor() + 10)

    @staticmethod
    def down():
        if not catcher.ycor() <= -387:
            catcher.setpos(catcher.xcor(), catcher.ycor() - 10)

def initialize(fallingObjectsCount):
    # turtle
    turtle.setup(1000, 1000) # canvas setup
    turtle.bgpic("./assets/images/background.gif") # background img
    turtle.register_shape("./assets/images/catcher.gif") # catcher img
    turtle.register_shape("./assets/images/falling.gif") # falling obj img

    # instantiation and initialization
    # catcher
    globals()["catcher"] = turtle.Turtle()
    catcher.pu()
    catcher.speed("fastest")
    catcher.shape("./assets/images/catcher.gif")
    catcher.setpos(randint(-387, 387), -387)

    #! catcher movement binding, not sure if needed to be moved to line 73
    turtle.onkeypress(CatcherMovement.left(), "a")
    turtle.onkeypress(CatcherMovement.right(), "d")
    # turtle.onkeypress(CatcherMovement.up(), "w")
    # turtle.onkeypress(CatcherMovement.down(), "s")

    # falling obj || snowflakes
    globals()["fallingObjNum"] = fallingObjectsCount
    for i in range(fallingObjNum):
        globals()[f"falling{i}"] = turtle.Turtle()
        globals()[f"falling{i}"].pu()
        globals()[f"falling{i}"].speed("fastest")
        globals()[f"falling{i}"].shape("./assets/images/falling.gif")
        globals()[f"falling{i}"].setpos(randint(-462, 462), randint(0, 465))
    
def main():
    print("please wait until the game is initialized")
    initialize(5)
    input("game initialized. press enter to continue")

    # main loop
    while True:
        for i in range(fallingObjNum):
            # falling obj
            globals()[f"falling{i}"].setpos(globals()[f"falling{i}"].xcor(), globals()[f"falling{i}"].ycor() - 3) # update falling obj position

            # reset falling obj position if touches bottom border || caught by catcher [implementation: using distance2 = (x1 - x2)2 + (y1 - y2)2 to calculate the distance between the falling object and the catcher]
            if (globals()[f"falling{i}"].ycor() <= -465) or (sqrt((globals()[f"falling{i}"].xcor() - catcher.xcor()) ** 2 + (globals()[f"falling{i}"].ycor() - catcher.ycor()) ** 2) <= 112):
                globals()[f"falling{i}"].setpos(randint(-462, 462), 465)

            turtle.listen() # listen for keyboard events
            
            
if __name__ == '__main__':
    main()