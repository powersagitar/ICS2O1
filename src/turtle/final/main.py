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

# struct for basic shapes
class BasicShapes:
    @staticmethod
    def roundedRectangle(obj, fillcolor, center_x, center_y, width, height, cornersize):
        obj.up()
        obj.goto(center_x-width / 2 + cornersize, center_y - height / 2)
        obj.fillcolor(fillcolor)
        obj.down()
        obj.begin_fill()
        for i in range(2):
            obj.fd(width - 2 * cornersize)
            obj.circle(cornersize, 90)
            obj.fd(height - 2 * cornersize)
            obj.circle(cornersize, 90)
        obj.end_fill()
        obj.up()

# struct for catcher movement control
class CatcherMovement:
    @staticmethod
    def left():
        if not catcher.xcor() <= -387: # border check
            catcher.setpos(catcher.xcor() - 10, catcher.ycor())
    
    @staticmethod
    def right():
        if not catcher.xcor() >= 387: # border check
            catcher.setpos(catcher.xcor() + 10, catcher.ycor())

# struct for falling object control
class FallingObjectControl:
    @staticmethod
    def reset(i):
        globals()[f"falling{i}"].setpos(randint(-462, 462), randint(535, 635)) # reset falling object position to ABOVE the top, using ycor to control the delay before falling starts
        fallingSpeed[i] = randint(1, 10)

# class for statistics control
class StatControl:
    # private attributes to store statistics
    missedCount = None
    caughtCount = None

    # private attributes to control missed stat and caught stat separately
    missedStat = turtle.Turtle()
    caughtStat = turtle.Turtle()

    def __init__(self, initMissedCount, initCaughtCount):
        # initialize the missed count && caught count
        self.missedCount = initMissedCount
        self.caughtCount = initCaughtCount

        # initialize the objects: missedStat && caughtStat
        for obj in [self.missedStat, self.caughtStat]:
            obj.hideturtle()
            obj.pu()
            obj.speed("fastest")

        # move the two objects to designed position
        #* this section has to be put before the initial stat printing since removal is done using turtle.undo()
        self.missedStat.setpos(-430, 400)
        self.caughtStat.setpos(-430, 365)

        # print the initial statistics statement for turtle.undo() uses later on
        self.missedStat.write("Missed: " + str(self.missedCount), move=False, align='left', font=('Arial', 17, 'normal'))
        self.caughtStat.write("Caught: " + str(self.caughtCount), move=False, align='left', font=('Arial', 17, 'normal'))

    def updateMissedCount(self, diff):
        self.missedCount += diff
        self.missedStat.undo() # use undo to erase written statements as it is faster
        self.missedStat.write("Missed: " + str(self.missedCount), move=False, align='left', font=('Arial', 17, 'normal'))

    def updateCaughtCount(self, diff):
        self.caughtCount += diff
        self.caughtStat.undo() # use undo to erase written statements as it is faster
        self.caughtStat.write("Caught: " + str(self.caughtCount), move=False, align='left', font=('Arial', 17, 'normal'))

# a struct for controlling the general program status
class ProgramStatusControl:
    @staticmethod
    def initialize(fallingObjectsCount):
        # turtle
        turtle.setup(1000, 1000) # canvas setup
        turtle.hideturtle()
        turtle.pu()
        turtle.bgpic("./background.gif") # background img
        turtle.register_shape("./catcher.gif") # catcher img
        turtle.register_shape("./falling.gif") # falling object img

        # object instantiation and initialization
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
        globals()["fallingSpeed"] = []
        globals()["fallingObjNum"] = fallingObjectsCount
        for i in range(fallingObjNum):
            globals()[f"falling{i}"] = turtle.Turtle()
            globals()[f"falling{i}"].pu()
            globals()[f"falling{i}"].speed("fastest")
            globals()[f"falling{i}"].shape("./falling.gif")
            globals()[f"falling{i}"].setpos(randint(-462, 462), randint(0, 465))
            fallingSpeed.append(randint(1, 10))
        
        # statistics
        globals()["stat"] = StatControl(0, 0)

    @staticmethod
    def exit():
        del globals()["exitPrompt"] # reset exit prompt availability
        _exit(0) # exit program with 0

    @staticmethod
    def restart():
        # reset screen
        turtle.clearscreen()
        exitPrompt.destroy()

        # reset exit prompt availability
        del globals()["exitPrompt"] 

        # recall main function
        main()

    @staticmethod
    def exitPrompt():
        # hold screen
        for i in range(5):
            fallingSpeed[i] = 0

        # display exit message
        turtle.setpos(0, 20)
        turtle.write("Game Over", move=False, align='center', font=('Arial', 30, 'normal'))
        turtle.setpos(turtle.xcor(), turtle.ycor() - 40)
        turtle.write("You have exceeded the maximum missed count (5).", move=False, align='center', font=('Arial', 30, 'normal'))
        
        # exit prompt window
        globals()["exitPrompt"] = tkinter.Tk()
        exitPrompt.title("Exit Prompt - Game Failed")
        tkinter.Label(exitPrompt, text="Exit Prompt - Game Failed").pack()
        tkinter.Button(exitPrompt, text="Retry", command=ProgramStatusControl.restart).pack()
        tkinter.Button(exitPrompt, text="Exit", command=ProgramStatusControl.exit).pack()

def main():
    # initialization
    # print("please wait until the game is initialized")
    ProgramStatusControl.initialize(5)
    # input("game initialized. press enter to continue")

    # listen for screen events
    turtle.listen() 

    # moving animations
    while True:
        # this for loop is used to make the control switch between all the objects
        for i in range(fallingObjNum):
            # falling objects
            globals()[f"falling{i}"].setpos(globals()[f"falling{i}"].xcor(), globals()[f"falling{i}"].ycor() - fallingSpeed[i]) # regular falling

            if not "exitPrompt" in globals():
                # missed decision
                if globals()[f"falling{i}"].ycor() <= -465:
                    FallingObjectControl.reset(i)
                    stat.updateMissedCount(1)
                    
                    # check if the user failed the game
                    if stat.missedCount > 5:
                        ProgramStatusControl.exitPrompt()

                # caught decision
                elif globals()[f"falling{i}"].ycor() > catcher.ycor() + 92 and globals()[f"falling{i}"].ycor() < catcher.ycor() + 112 and abs(globals()[f"falling{i}"].xcor() - catcher.xcor()) < 112:
                    FallingObjectControl.reset(i)
                    stat.updateCaughtCount(1)
            
if __name__ == '__main__':
    main()