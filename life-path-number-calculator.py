######################################################################
# Author: Quinten Lambert
# username: lambertq
#
# Purpose: demonstration of the use of fruitful function and return values.
#   (1) function returns a string, omitting denominations with zero number
#   (2) function uses fruitful functions to find life path number
#   (3) added lots of comments to explain what the functions do
######################################################################
# Acknowledgements:
#
# Collaberated with classmates: Eric Rhodes(rhodese) and Kye Hoover(hooverk)
#
# Original code started completely from scratch
######################################################################

#These are the things I needed to import for the
import turtle
import random
import time

#################################################################################
#These are the main functions of the coding that split the data input into the
#function
def month_number(amount):
    """This takes the raw data that was input by the user and splits it into
    individual digits, then adds them together. Specifically for the month that
    the user input for their birthday."""
    for i in (month):
        if month == '11':
            return int(11)
        else:
            unit_one = int(month[:1])
            unit_two = int(month[1:2])

            return int(unit_one+unit_two)

def day_number(amount):
    """This takes the raw data that was input by the user and splits it into
    individual digits, then adds them together. Specifically for the day that
    the user input for their birthday."""
    for i in (day):
        if day == '11':
            return int(11)
        elif day == '22':
            return int(22)
        else:
            unit_one = int(day[:1])
            unit_two = int(day[1:2])

            return int(unit_one+unit_two)

def year_number(amount):
    """This takes the raw data that was input by the user and splits it into
    individual digits, then adds them together. Specifically for the year that
    the user input for their birthday."""
    for i in (year):
        if year == '11':
            return int(11)
        else:
            unit_one = int(year[:1])
            unit_two = int(year[1:2])
            unit_three = int(year[2:3])
            unit_four = int(year[3:4])

            return int(unit_one+unit_two+unit_three+unit_four)

def total_number(amount):
    """This takes the total number that was gained from all of the previous
    functions and adds them together, leaving exceptions for the master
    numbers."""
    for i in (total):
        if prelife_number == int(11):
            return int (11)
        elif prelife_number == int(22):
            return int (22)
        elif prelife_number == int(33):
            return int (33)
        else:
            unit_one = int(total[:1])
            unit_two = int(total[1:2])

            return int(unit_one+unit_two)

def final_calculation (amount):
    """This code is used in the rare occasion that the life number would have
    turned out to be a 10 or a 12. In each of those cases it causes them to
    split apart and add together, however if the life path number would be
    anything else other than the master numbers, it would just return the
    number and continue on."""
    for i in (final):
        if complete == int(11):
            return int(11)
        elif complete == int(10):
            unit_one = int(final[:1])
            unit_two = int(final[1:2])

            return int(unit_one+unit_two)
        elif complete == int(12):
            unit_one = int(final[:1])
            unit_two = int(final[1:2])

            return int(unit_one+unit_two)
        else:
            return final
#################################################################################
#Introduction to the program
print('Welcome to the Life Path Number Calculator!')
print
time.sleep(1.5)
print('Today we are going to find your Life Path Number!')
print
time.sleep(1.5)
print('All you need to do is enter your birthday and then you can find out your Life Path Number!')
print
time.sleep(1.5)

#Getting the birthday(raw data)
month = raw_input('Input the two digit month of which you were born. Ex. May would be "05".')
time.sleep(0.5)
day = raw_input ('Input the two digit day of which you were born. Ex."05".')
time.sleep(0.5)
year = raw_input('Input the four digit year of which you were born. Ex. "1995".')
time.sleep(1.5)

#Taking all of the data received from the user and making it into one number
prelife_number = month_number(month)+day_number(day)+year_number(year)

#Turns the integer number recieved by the prelife_number and turns it into a string
total = str(prelife_number)

#Taking the data received from by the total_number function and naming it
complete = total_number(total)

#Taking the data received from total_number function and making it a string
final = str(complete)

print('We are now calculating your life number...')
time.sleep(1)
print('....')
time.sleep(1)
print('....')
time.sleep(1)
print('Alright your life path number is...')
time.sleep(2.0)

#################################################################################

#Prints the number on a screen for the user to see, in all its flashy goodness
print('')
wn = turtle.Screen()
wn.bgcolor(random.random(),random.random(), random.random())
number = turtle.Turtle()
number.up()
number.setpos(0,-220)
number.hideturtle()

for i in range(2000):
    number.speed(0)
    number.color(random.random(),random.random(), random.random())
    wn.bgcolor(random.random(),random.random(), random.random())
    number.write(str(final_calculation(final)),move=False,align='center',font=("Algerian",350,("bold","normal")))
wn.exitonclick()

#################################################################################