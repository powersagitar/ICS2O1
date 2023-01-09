############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle

#todo adjust image size

def main():
    # initialization
    # turtle
    turtle.setup(1000, 1000) # canvas setup
    turtle.bgpic("./assets/images/background.gif") # background img
    turtle.register_shape("./assets/images/catcher.gif") # catcher img
    turtle.register_shape("./assets/images/falling.gif") # falling obj img

    # instantiation
    catcher = turtle.Turtle()
    for i in range(5):
        locals()[f"falling{i}"] = turtle.Turtle()

    # initialize instances
    catcher.shape("./assets/images/catcher.gif")
    catcher.setpos(0, 0)
    for i in range(5):
        print(i)
        locals()[f"falling{i}"].shape("./assets/images/falling.gif")
        locals()[f"falling{i}"].setpos(0, 0)


if __name__ == '__main__':
    main()