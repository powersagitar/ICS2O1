############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle
from random import randint

def initialize():
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

    # falling obj || snowflakes
    for i in range(5):
        globals()[f"falling{i}"] = turtle.Turtle()
        globals()[f"falling{i}"].pu()
        globals()[f"falling{i}"].speed("fastest")
        globals()[f"falling{i}"].shape("./assets/images/falling.gif")
        globals()[f"falling{i}"].setpos(randint(-462, 462), randint(0, 465))

def main():
    print("please wait until the game is initialized")
    initialize()
    input("game initialized. press enter to continue")

if __name__ == '__main__':
    main()