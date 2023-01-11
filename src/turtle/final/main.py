############################################
# Program: final/main.py
# Date: 01/09/2023
# Author: Mohan Dong
# Description: The final project.
############################################

import turtle
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
        globals()[f"falling{i}"].setpos(randint(-462, 462), 535) # reset falling object position to ABOVE the top
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

        # initalize the objects: missedStat && caughtStat
        # make both object invisible
        self.missedStat.hideturtle()
        self.caughtStat.hideturtle()

        # lift the pens of the two objects
        self.missedStat.pu()
        self.caughtStat.pu()

        # set both object speed to fastest
        self.missedStat.speed("fastest")
        self.caughtStat.speed("fastest")

        # move the two objects to designed position
        #! this section has to be put before the initial stat printing since removal is done using turtle.undo()
        self.missedStat.setpos(-430, 400)
        self.caughtStat.setpos(-430, 365)

        # print the initial statistics statement for turtle.undo() uses later on
        self.missedStat.write("Missed: " + str(self.missedCount), move=False, align='left', font=('Arial', 17, 'normal'))
        self.caughtStat.write("Caught: " + str(self.caughtCount), move=False, align='left', font=('Arial', 17, 'normal'))

    def updateMissedCount(self, diff):
        self.missedCount += diff
        self.missedStat.undo() # use undo to erase written statements as it is faster
        self.missedStat.write("Missed: " + str(self.missedCount), move=False, align='left', font=('Arial', 17, 'normal'))

        # check if the user failed the game
        if self.missedCount > 10:
            ProgramStatusControl.exit()

    def updateCaughtCount(self, diff):
        self.caughtCount += diff
        self.caughtStat.undo() # use undo to erase written statements as it is faster
        self.caughtStat.write("Caught: " + str(self.caughtCount), move=False, align='left', font=('Arial', 17, 'normal'))

# a struct for controlling the general program status
class ProgramStatusControl:
    @staticmethod
    def initialize(fallingObjectsCount):
        # turtle
        turtle.clearscreen()
        turtle.setup(1000, 1000) # canvas setup
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
        globals()["stat"] = StatControl(10, 0)

    @staticmethod
    def exit():
        # display exit message
        turtle.write("Game is over since you have reached the maximum missed count (10).", move=False, align='left', font=('Arial', 30, 'normal'))

        # make on screen buttons
        btnExit = turtle.Turtle()
        btnRetry = turtle.Turtle()

        # initialize button objects
        # hide objects
        btnExit.hideturtle()
        btnRetry.hideturtle()

        # set speed to fastest
        btnExit.speed("fastest")
        btnRetry.speed("fastest")

        # draw the button
        BasicShapes.roundedRectangle(btnExit, "grey", -250, -250, 100, 50, 50)
        # BasicShapes.roundedRectangle(btnRetry, ..., ..., ..., ..., ...)

        input("enter")

        # button action binding
        btnRetry.onclick(main())
        btnExit.onclick(_exit(0))
        
def main():
    # initialization
    print("please wait until the game is initialized")
    ProgramStatusControl.initialize(5)
    input("game initialized. press enter to continue")

    # listen for screen events
    turtle.listen() 

    # moving animations
    while True:
        # this for loop is used to make the control switch between all the objects
        for i in range(fallingObjNum):
            # falling objects
            globals()[f"falling{i}"].setpos(globals()[f"falling{i}"].xcor(), globals()[f"falling{i}"].ycor() - fallingSpeed[i]) # regular falling

            # missed decision
            if globals()[f"falling{i}"].ycor() <= -465:
                FallingObjectControl.reset(i)
                stat.updateMissedCount(1)

            # caught decision
            elif globals()[f"falling{i}"].ycor() > catcher.ycor() + 92 and globals()[f"falling{i}"].ycor() < catcher.ycor() + 112 and abs(globals()[f"falling{i}"].xcor() - catcher.xcor()) < 112:
                FallingObjectControl.reset(i)
                stat.updateCaughtCount(1)
            
if __name__ == '__main__':
    main()