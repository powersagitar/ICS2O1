############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle
from pathlib import Path

def main():
    # instantiation
    catcher = turtle.Turtle()

    # initialization
    turtle.setup(1000, 1000)
    turtle.bgpic(Path("./assets/images/background.gif"))
    turtle.register_shape("catcher", Path("./assets/images/catcher.gif"))
    catcher.shape(catcher)
    catcher.setpos(0, 0)

if __name__ == '__main__':
    main()