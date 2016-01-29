# Author: Quinten Lambert
# username: lambertq
#
# Assignment: P2 6 point star
# Purpose: To use Turtles to make a 6 point star
######################################################################
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# Objectives: Use Turtles to make a 6 point star
######################################################################
# Acknowledgements: Modified by Quinten Lambert
#################################################################################

import turtle
wn = turtle.Screen()

myturtle = turtle.Turtle()
turtle.bgcolor('black')

myturtle.shape('turtle')
myturtle.hideturtle()

myturtle.pensize(5)

myturtle.penup()

myturtle.forward(100)
myturtle.right(90)
myturtle.forward(100)
myturtle.left(90)

myturtle.right(180)
myturtle.pendown()

myturtle.color('red')

for i in range(3):
    myturtle.forward(200)
    myturtle.right(120)

myturtle.penup()
myturtle.left(270)
myturtle.forward(115)
myturtle.left(90)
myturtle.pendown()

myturtle.color('blue')

for i in range(3):
    myturtle.forward(200)
    myturtle.left(120)

wn.exitonclick()
