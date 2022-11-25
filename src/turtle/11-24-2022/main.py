import turtle
from pathlib import Path


# def main():
turtle.setup(1000, 1000);
turtle.bgpic(Path("./include/bg.png"));
turtle.addshape("./include/pen.gif");
turtle.shape("./include/pen.gif");
turtle.update();

turtle.exitonclick();