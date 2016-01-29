#################################################################################
# Author: Quinten Lambert(lambertq)
# Purpose: To very demonstrate the turtle library to demo the use of funcitons
######################################################################
# Acknowledgements:
# None--original work

# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

#################################################################################
import turtle
#__import__("turtle").__traceable__ = False # prevents stepping into library

turtle.colormode(255)   # change color modes
wn = turtle.Screen()    # make screen close cleanly
wn.bgcolor("#466446")   # Hexadecimal colors RGB
#################################################################################

#################################################################################
def make_house(x,y, sideroof_color, frontroof_color, side_color, house_color, door_color, window_color, size):
    """Draws a house that uses the given colors and moves it across the screen"""
    bob=turtle.Turtle()
    bob.speed(0)
    bob.hideturtle()
    bob.up()
    bob.setpos(x,y)

# makes the main part of the house
    bob.color(house_color)
    bob.begin_fill()
    for wall in range(4):
        bob.forward(size)
        bob.right(90)
    bob.left(135)
    bob.end_fill()

# makes the side wall
    bob.color(side_color)
    bob.begin_fill()
    for wall in range(2):
        bob.forward(size)
        bob.left(135)
        bob.forward(size)
        bob.left(45)
    bob.end_fill()

# makes the front of the roof
    bob.color(frontroof_color)
    bob.begin_fill()
    for roof in range(2):
        bob.right(90)
        bob.forward(85)
    bob.end_fill()
    bob.right(180)
    bob.forward(85)

# makes the side of the roof
    bob.color(sideroof_color)
    bob.begin_fill()
    for roof in range(2):
        bob.forward(size)
        bob.left(90)
        bob.forward(85)
        bob.left(90)
    bob.end_fill()

#This next section of code is moving the cursor into place where I need it next.
    bob.penup()
    bob.left(90)
    bob.forward(85)
    bob.right(90)
    bob.forward(90)
    bob.left(135)
    bob.forward(50)
    bob.left(45)
    bob.pendown()

# Decoration time! First the window on the side wall...
    bob.color(window_color)
    bob.begin_fill()
    for window in range(2):
        bob.forward(40)
        bob.right(45)
        bob.forward(25)
        bob.right(135)
    bob.end_fill()

#This next section of code is moving the cursor into place where I need it next.
    bob.penup()
    bob.left(135)
    bob.forward(50)
    bob.right(135)
    bob.forward(90)
    bob.right(45)
    bob.forward(size)
    bob.left(90)
    bob.forward(70)
    bob.left(90)
    bob.pendown()

#Finally its time to make that awesome door up front...
    bob.color(door_color)
    bob.begin_fill()
    for door in range(2):
        bob.forward(60)
        bob.right(90)
        bob.forward(30)
        bob.right(90)
    bob.end_fill()

#This is the end of the: make_house function
#################################################################################

#################################################################################
# Makes a blue sky in the background
my_street=turtle.Turtle()
my_street.speed(0)
my_street.pencolor('light blue')
my_street.penup()
my_street.setpos(-350,200)
my_street.pendown()
my_street.pensize(350)
my_street.forward(800)
my_street.up()

#################################################################################
# Makes the sun shine bright in the upper left corner of the screen
sun=turtle.Turtle()

sun.color('gold')
sun.begin_fill()
sun.penup()
sun.setpos(-350,200)
sun.pendown()
sun.circle(100)
sun.end_fill()

#################################################################################
# Makes a street in front of the houses
my_street=turtle.Turtle()
my_street.speed(0)
my_street.pencolor('black')
my_street.penup()
my_street.setpos(-350,-200)
my_street.pendown()
my_street.pensize(100)
my_street.forward(800)
my_street.up()

# Makes a dotted yellow line in the middle of the street
my_line=turtle.Turtle()
my_line.speed(0)
my_line.pencolor('yellow')
my_line.penup()
my_line.setpos(-350,-200)
my_line.pendown()
my_line.pensize(2)
for line in range(20):
    my_line.forward(20)
    my_line.penup()
    my_line.forward(20)
    my_line.pendown()
my_line.up()

#This is the end of the street making process.
#################################################################################
####################################################################
# Making 3 houses by running the make_house code function
for i in range(3):
    my_bob=make_house(i*220-240, i-20, 'light grey', 'grey', 'goldenrod', 'dark goldenrod', 'saddle brown', 'dim gray', 120)
# This is the end of the usage of the make_house function to create the
# neighborhood.
#################################################################################

wn.exitonclick() #Turtle screen exits on click.

#################################################################################



