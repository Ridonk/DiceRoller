#!/usr/bin/env python

import random


# Roll n dice with x sides and return a list of the results
def roll(numberofdice, numberofsides):
    results = []
    for i in range(0, numberofdice):
        results.append(random.randint(1, numberofsides))
        i += 1
    results.sort()
    return results


# Print each result in a list
def print_roll(roll_list):
    for result in roll_list:
        print(result)


print("Hello! Welcome to DiceRoller.")

# Groundwork for a more adaptive menu
running = True

# Main Loop
while running:
    # Store the number of dice to roll
    ndice = int(input("Please enter how many dice: "))
    # Store how many sides each die has
    xsides = int(input("Please  enter how many sides on each die: "))
    # Tell the user what we're processing
    print("You entered " + str(ndice) + " dice and " + str(xsides) + " sides per die.")
    # Sanity check before bothering to generate random numbers.
    if ndice > 0 and xsides > 0:
        print_roll(roll(ndice, xsides))
    else:
        print("Invalid roll attempted. The FBI has been notified.")
    check_quit = input("To quit enter q or just press enter to continue: ")
    if check_quit != 'q':
        running = True
    else:
        running = False
