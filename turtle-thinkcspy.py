#######################################################################################################################################################
# turtle test
# original from http://interactivepython.org/runestone/static/thinkcspy/index.html#
# Purpose: To demonstrate the turtle library
######################################################################
# Acknowledgements:
# original from http://interactivepython.org/runestone/static/thinkcspy/index.html

# Modifications by Dr. Jan Pearce
# converted to Windows, removed def function, added Screen for clean close
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
#################################################################################

import turtle

turtle.color('purple')   #Used to change the color to purple
wn = turtle.Screen()
turtle.bgcolor('blue')

myturtle = turtle.Turtle()

myturtle.shape('turtle')
myturtle.hideturtle()
myturtle.speed(0)

myturtle.pensize(2)

myturtle.begin_fill()
myturtle.fillcolor(1,0,1)

#This next bit of code is making the walls around the house and filling them
#in with a purple color.
for i in range(4):
    myturtle.forward(150)
    myturtle.right(90)

myturtle.right(-135)
myturtle.forward(100)
myturtle.left(135)
myturtle.forward(150)
myturtle.left(45)
myturtle.forward(100)
myturtle.left(135)
myturtle.forward(150)

myturtle.end_fill()

#Now for the Roof
myturtle.begin_fill()
myturtle.fillcolor(.5,0,1)

myturtle.right(45)
myturtle.forward(106)
myturtle.right(90)
myturtle.forward(106)
myturtle.right(135)
myturtle.forward(150)
myturtle.right(45)
myturtle.forward(100)
myturtle.right(90)
myturtle.forward(106)
myturtle.right(90)
myturtle.forward(100)

myturtle.end_fill()


#The following code will be making the various windows and a door on the building.
#First off the circular window for the attic.
myturtle.penup()  #moving the cursor into place
myturtle.right(30)
myturtle.forward(40)
myturtle.right(90)
myturtle.forward(10)
myturtle.pendown()

myturtle.forward(1)
myturtle.circle(15)
myturtle.right(-75)
myturtle.penup()
myturtle.forward(122)
myturtle.pendown()

myturtle.begin_fill
myturtle.fillcolor(1,0,1)

for i in range(4):
    myturtle.forward(60)
    myturtle.left(90)
    myturtle.forward(40)
    myturtle.left(90)

myturtle.end_fill()


wn.exitonclick()




