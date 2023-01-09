############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle

def main():
    # instantiation
    catcher = turtle.Turtle()
    falling = turtle.Turtle()

    # initialization
    turtle.setup(1000, 1000)
    turtle.bgpic("./assets/images/background.gif")
    turtle.register_shape("./assets/images/catcher.gif")
    turtle.register_shape("./assets/images/falling.gif")
    catcher.shape("./assets/images/catcher.gif")
    catcher.setpos(0, 0)
    falling.shape("./assets/images/falling.gif")
    falling.setpos(0, 0)


if __name__ == '__main__':
    main()