#!/usr/bin/env python

import random


class Dice:

    def __init__(self, sides):
        self.sides = sides
        self.results = []
        self.total_count = {}

    def _roll(self):
        return random.randint(1, self.sides)

    def roll(self, number_of_dice=1):
        for i in range(0, number_of_dice):
            self.results.append(self._roll())

    def print_die_results(self):
        for result in self.results:
            print(str(result))
        print(self.count_results())
        return

    def count_results(self):
        self.results.sort()
        for result in self.results:
            if result in self.total_count:
                self.total_count[result] += 1
            else:
                self.total_count[result] = 1
        return self.total_count


def get_number_input():
    while True:
        try:
            user_input = int(input(">>> "))
            return int(user_input)
        except ValueError:
            print("Invalid input. Try again with numbers.")


def main_menu():
    while True:
        print('''
        ==========
        MAIN MENU
        ==========

        1. Roll Dice
        2. Quit

        ''')
        user_input = get_number_input()
        if user_input == 1:
            print("How many dice? ")
            number_of_dice = get_number_input()
            print("How many sides per die? ")
            number_of_sides = get_number_input()
            print("You entered {} dice with {} sides.".format(number_of_dice, number_of_sides))
            dice = Dice(number_of_sides)
            dice.roll(number_of_dice)
            dice.print_die_results()
        elif user_input == 2:
            quit(0)


print("Hello! Welcome to DiceRoller.")

# Main Loop
main_menu()
