# Author: Quinten Lambert
# username: lambertq
#
# Assignment: A03
# Purpose: To use Turtles to make a drawing
######################################################################
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# Objectives:
#- Introduces the use of the turtles library
######################################################################
# Acknowledgements:
# modified by Quinten Lambert
# modified from http://interactivepython.org/runestone/static/thinkcspy/PythonTurtle/helloturtle.html
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle
wn = turtle.Screen()

myturtle = turtle.Turtle()

myturtle.shape('turtle')
myturtle.hideturtle()
myturtle.color('Black')
myturtle.speed(0)


myturtle.pensize(5)

myturtle.penup()
myturtle.left(180)
myturtle.forward(80)
myturtle.right(90)
myturtle.forward(120)
myturtle.left(90)
myturtle.pendown()

for star in [0,1]:
    myturtle.right(120)
    myturtle.forward(150)

for star in [0,1,2,3,4]:
    myturtle.left(60)
    myturtle.forward(150)
    myturtle.right(120)
    myturtle.forward(150)

for star in [0,1,2]:
    myturtle.right(60)
    myturtle.forward(300)
    myturtle.right(60)
    myturtle.forward(150)
    myturtle.right(120)
    myturtle.forward(150)

myturtle.color('Yellow')

for star in [0,1,2,3,4,5]:
    myturtle.forward(150)
    myturtle.right(60)

myturtle.right(90)

for star in [0,1,2,3]:
    myturtle.forward(260)
    myturtle.left(90)
    myturtle.forward(150)
    myturtle.left(90)

wn.exitonclick()
