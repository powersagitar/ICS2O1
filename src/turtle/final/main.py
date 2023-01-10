############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle
from random import randint

# struct for catcher movement control
class CatcherMovement:
    def left():
        if not catcher.xcor() <= -387: # border check
            catcher.setpos(catcher.xcor() - 10, catcher.ycor())
    
    def right():
        if not catcher.xcor() >= 387: # border check
            catcher.setpos(catcher.xcor() + 10, catcher.ycor())

def initialize(fallingObjectsCount):
    # turtle
    turtle.setup(1000, 1000) # canvas setup
    turtle.bgpic("./background.gif") # background img
    turtle.register_shape("./catcher.gif") # catcher img
    turtle.register_shape("./falling.gif") # falling object img

    # instantiation and initialization
    # catcher
    globals()["catcher"] = turtle.Turtle()
    catcher.pu()
    catcher.speed("fastest")
    catcher.shape("./catcher.gif")
    catcher.setpos(randint(-387, 387), -387)

    # catcher movement binding ! do NOT put parentheses after the function, otherwise it will stop working
    turtle.onkeypress(CatcherMovement.left, "a")
    turtle.onkeypress(CatcherMovement.right, "d")

    # falling object || snowflakes
    globals()["fallingObjNum"] = fallingObjectsCount
    for i in range(fallingObjNum):
        globals()[f"falling{i}"] = turtle.Turtle()
        globals()[f"falling{i}"].pu()
        globals()[f"falling{i}"].speed("fastest")
        globals()[f"falling{i}"].shape("./falling.gif")
        globals()[f"falling{i}"].setpos(randint(-462, 462), randint(0, 465))
    
def main():
    # initialization
    print("please wait until the game is initialized")
    initialize(5)
    input("game initialized. press enter to continue")

    # listen for screen events
    turtle.listen() 

    # moving animations
    while True:
        # this for loop is used to make the control switch between all the objects
        for i in range(fallingObjNum):
            # falling objects
            globals()[f"falling{i}"].setpos(globals()[f"falling{i}"].xcor(), globals()[f"falling{i}"].ycor() - 5) # regular falling

            # reset falling object position if touches bottom border || caught by catcher [implementation: using distance2 = (x1 - x2)2 + (y1 - y2)2 to calculate the distance between the falling object and the catcher. the distance is 112, therefore distance2 becomes 12544]
            if (globals()[f"falling{i}"].ycor() <= -465) or (((globals()[f"falling{i}"].xcor() - catcher.xcor()) ** 2 + (globals()[f"falling{i}"].ycor() - catcher.ycor()) ** 2) <= 12544):
                globals()[f"falling{i}"].setpos(randint(-462, 462), 465)
            
if __name__ == '__main__':
    main()