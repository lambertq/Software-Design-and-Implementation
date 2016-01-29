#-------------------------------------------------------------------------------
# Name:      lambertq-rhodese-L1
#Purose:     To play the game of nim with the user
#
#Author:      lambertq(Quinten Lambert)
#Co-author:   rhodese(Eric Rhodes)
#Acknowledgements: Collaberated with Kye Hoover(Hooverk)
#
#Created:     31/01/2014
#Copyright:   (c) lambertq 2014
#-------------------------------------------------------------------------------
##############################################################################
#Imported the libraries that were needed within the program
import math
import time
import random
##############################################################################
# Say hello to the sole function of this program. Quite a fruitful one at that
def computer_choice(number):
    """This section of code determines how many balls the computer will take
    however if the ball number is less than 5, the computer will win the
    game."""
    if number <= 4: # if the number is 4 or less the computer wins the game
        return number
    # if the number is divisible by 5 take a random value
    elif number % 5 == 0:
        a = 1
        b = 2
        c = 3
        d = 4
        number = random.choice([a,b,c,d])
        number = str(number)
        print('The computer has taken, ' +number)
        number = int(number)
        return number
    else:
        # If the number is not divisible by 5 then take the remainder to get
        # back to the multiple of 5
        take = number % 5
        number = take
        number = str(number)
        print('The computer has taken, ' +number)
        number = int(number)
        return number
##############################################################################
#This asks the user to input a number of balls and if they input less than 15
#the computer will continue to ask them for a number until a value of 15 or
#higher is given
number = raw_input('How many balls?')
number = int(number)
while (number <= 14):
    number = int(raw_input('Thats not enough, please pick 15 or higher.'))
print('Alright then lets play the game.')
print ("You play first")

print #This is a blank line
time.sleep(0.5) #Gives the program a slight delay

while number > 0:
    #This area asks the user how many balls do they want to take
    time.sleep(1) #Gives the program a slight delay
    number = str(number)
    display_number='How many would you like to take? There are '+ number +' balls left.'
    second_input = raw_input (display_number)
    second_input = int(second_input)
    number = int(number)

    #This keeps asking the user for a number within the appropiate range.
    if second_input > 4:
        time.sleep(1) #Gives the program a slight delay
        print ('Thats outside the number range, pick between 1-4')

    #This is telling the user that they can not take 0 balls.
    elif second_input == 0:
        time.sleep(1) #Gives the program a slight delay
        print('This is not a number, please select between 1-4')

    #This next section of code depends solely on how many balls the user had
    #wanted to take from the inital pool of balls.
    elif second_input <= 4:
        time.sleep(1) #Gives the program a slight delay
        players_pick = int(second_input)

        #This shows the user how much they took from the pile
        number = number - players_pick

        #This shows how much the user has taken from the pile
        print #This is a blank line
        print('You have taken, ' +str(second_input))

        #This is when the computer loses the game.
        if number == 0:
            print #This is a blank line
            print ('AWWW MAN! I lost!')

        #When the number is not 0 the computer will continue on with its choice
        #and keep playing the game
        elif number != 0:
            number = number - computer_choice(number)

            #This allows the user to see how many balls are left
            time.sleep(0.5) #Gives the program a slight delay
            print #This is a blank line
            print('There are ' +str(number)+ ' balls remaining.')

            #This turns the two values back into integers so they may be used
            #again next time through the code
            number = int(number)
            second_input = int(second_input)

            if number == 0:
                print('Alright I get to take the rest!')
                print #This is a blank line
                time.sleep(0.5) #Gives the program a slight delay
                print ('Pack your bags, and get out. I just won...everything.')