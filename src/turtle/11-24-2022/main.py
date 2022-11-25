# importing libraries
import turtle
from pathlib import Path


# def main():
turtle.setup(1000, 1000); # setting up the canvas
turtle.bgpic(Path("./include/bg.png")); # setting background image
turtle.addshape("./include/pen.gif"); # registering pen shape
turtle.shape("./include/pen.gif"); # updating pen shape
turtle.update(); # update canvas

turtle.exitonclick();