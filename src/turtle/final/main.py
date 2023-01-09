############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle
from pathlib import Path

def main():
    catcher = turtle.Turtle()

    turtle.setup(1000, 1000)
    turtle.bgpic(Path("./assets/images/background.gif"))

if __name__ == '__main__':
    main()