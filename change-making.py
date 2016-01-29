######################################################################
# A flawed change making program
#
# Author: Quinten Lambert
#
#
# Purpose: This program has a bunch of problems with that need to be
#   fixed. It should be simple enough to be able to trace using the
#   debugger and find out what is wrong.
#   It is supposed to make change. After it asks the user for the
#   amount of money in cents, it outputs the number of quarters, dimes,
#   nickels and pennies needed to make the change.
#
# A SAMPLE RUN OF THIS PROGRAM with 34 CENTS OUTPUTS:
#   You need 1 coins worth 25 cents.
#   You need 0 coins worth 10 cents.
#   You need 1 coins worth 5 cents.
#   You need 4 coins worth 1 cents.
#
# MODIFIED: February 5, 2014
#  - simplified the code by taking out extra things that are not related
#    to the errors.
#  - added comments to explain what this program is doing
######################################################################
# Acknowledgements:
# This is original BAD code
######################################################################

response = "no"
while response != "yes" or response != "YES":	# Loop check to stop asking when the user says no

    if response == "no" or response == "No": 	# The user wants to do this again.

        change = int(raw_input("Great! How much money do we have to make change for(in cents)? "))

    # now that we are continuing, let's make some change!
    if( change <= 0 ):
        # Check to make sure that we are putting in a valid number. We cannot make
        # change on a negative number.
        print('Can you put in a positive number?')
    else:
        # Ok, output the number of each coin needed to make change
        # starting with the quarters, dimes, nickels and then pennies
        for coin in [25, 10, 5, 1]:
            num_coins = change // coin	# find the number of each type of coin
            change = change % coin		# find out how much is left after taking out
                                        # this change.
        # output the number of each kind of coin
        #The following line of code was tabbed in to get the line to print each time the code
        #went through to print all of the values.
            print( 'You need '+ str(num_coins) + ' coins worth ' + str(coin) + ' cents.' )

        response = raw_input("Are we done?")	# Ask the user if he/she wants to quit