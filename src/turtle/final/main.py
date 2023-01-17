############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle
import tkinter
from random import randint
from os import _exit
from playsound import playsound

class Catcher(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.speed("fastest")
        turtle.register_shape("./catcher.gif")
        self.shape("./catcher.gif")
        self.setpos(randint(-387, 387), -387)

        # catcher movement binding
        turtle.onkeypress(self.movLeft, "a")
        turtle.onkeypress(self.movRight, "d")

    def movLeft(self):
        if not self.xcor() <= -387: # border check
            self.setpos(self.xcor() - 10, self.ycor())
    
    def movRight(self):
        if not self.xcor() >= 387: # border check
            self.setpos(self.xcor() + 10, self.ycor())

class FallingObject(turtle.Turtle):
    fallingSpeed = None

    def __init__(self):
        super().__init__()
        self.pu()
        self.speed("fastest")
        turtle.register_shape("./falling.gif")
        self.shape("./falling.gif")
        self.setpos(randint(-462, 462), randint(0, 465))
        self.fallingSpeed = randint(1, 10)

    def falling(self):
        self.setpos(self.xcor(), self.ycor() - self.fallingSpeed)

    def reset(self):
        self.setpos(randint(-462, 462), randint(535, 635))
        self.fallingSpeed = randint(1, 10)

class Statistics(turtle.Turtle):
    data = None
    name = None

    def __init__(self, dataName, initDataValue, pos):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.speed("fastest")

        # move object to designed position
        self.setpos(pos)

        # set attribute values
        self.data = initDataValue
        self.name = dataName

        # print initial statistics statement for turtle.undo() uses later on
        self.write(self.name + ": " + str(self.data), move=False, align="left", font=("Arial", 17, "normal"))

    def dataUpdate(self, diff):
        self.data += diff
        self.undo() # use undo to erase written statements as it is faster
        self.write(self.name + ": " + str(self.data), move=False, align="left", font=("Arial", 17, "normal"))

class ExitPrompt:
    window = None

    def __init__(self, fallingObjects):
        # hold screen
        for obj in fallingObjects:
            obj.fallingSpeed = 0

        # display exit message
        text = turtle.Turtle()
        text.hideturtle()
        text.pu()
        text.speed("fastest")
        text.setpos(0, 20)
        text.write("Game Over", move=False, align="center", font=("Arial", 30, "normal"))
        text.setpos(text.xcor(), text.ycor() - 40)
        text.write("You have exceeded the maximum missed count (5).", move=False, align="center", font=("Arial", 30, "normal"))

        # exit prompt window
        self.window = tkinter.Tk()
        self.window.title("Exit Prompt - Game Failed")
        tkinter.Label(self.window, text="Exit Prompt - Game Failed").pack()
        tkinter.Button(self.window, text="Retry", command=self.restart).pack()
        tkinter.Button(self.window, text="Exit", command=self.exit).pack()
    
    def restart(self):
        self.window.destroy() # destroy tkinter window (exit prompt)
        restart() # call program restart function

    def exit(self):
        exit(0) # exit program with 0

def restart():
    turtle.clearscreen() # clear screen
    main() # recall main function

def exit(exitCode):
    _exit(exitCode)

def main():
    # screen initialization
    turtle.setup(1000, 1000)
    turtle.hideturtle()
    turtle.bgpic("./background.gif")

    # catcher
    catcher = Catcher()

    # falling objects
    fallingObjectList = []
    for i in range(5):
        locals()[f"falling{i}"] = FallingObject()
        fallingObjectList.append(locals()[f"falling{i}"])

    # statistics
    missedStat = Statistics("Missed", 0, (-430, 400))
    caughtStat = Statistics("Caught", 0, (-430, 365))

    # listen for screen events
    turtle.listen()

    # moving animations
    while True:
        for obj in fallingObjectList:
            obj.falling() # regular falling

            # missed decision
            if obj.ycor() <= -465:
                obj.reset()
                missedStat.dataUpdate(1)
                playsound("missed.wav")

                # check if the user failed the game
                if missedStat.data > 5:
                    exitPrompt = ExitPrompt(fallingObjectList)

            # caught decision
            elif obj.ycor() > catcher.ycor() + 92 and obj.ycor() < catcher.ycor() + 112 and abs(obj.xcor() - catcher.xcor()) < 112:
                obj.reset()
                caughtStat.dataUpdate(1)
                playsound("caught.wav")

if __name__ == "__main__":
    main()