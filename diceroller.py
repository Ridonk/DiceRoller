#!/usr/bin/env python

import random

print("Hello! Welcome to DiceRoller.")
while True:
    numberDice = input("Please enter how many dice: ")
    sidesDice = input("Please  enter how many sides on each die: ")
    print("You entered " + numberDice + " dice and " + sidesDice + " sides per die.")
    results = []
    for x in range(0, int(numberDice)):
        results.append(random.randint(1, int(sidesDice)))
        x += 1
    results.sort()
    for result in results:
        print(result)
    check_quit = input("To quit type q or press enter to continue: ")
    if check_quit == 'q':
        break
