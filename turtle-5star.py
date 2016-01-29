# Author: Quinten Lambert
# username: lambertq
#
# Assignment: P2
# Purpose: To use Turtles to make a 5 point star
######################################################################
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# Objectives: Use Turtles to make a 5 point star
######################################################################
# Acknowledgements: Modified by Quinten Lambert
#################################################################################

import turtle
wn = turtle.Screen()

myturtle = turtle.Turtle()

myturtle.shape('turtle')
myturtle.hideturtle()

myturtle.pensize(3)

myturtle.forward(250)
myturtle.right(144)
myturtle.forward(250)
myturtle.right(144)
myturtle.forward(250)
myturtle.right(144)
myturtle.forward(250)
myturtle.right(144)
myturtle.forward(250)

wn.exitonclick()
