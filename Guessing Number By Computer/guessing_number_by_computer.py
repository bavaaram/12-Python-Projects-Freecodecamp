#! /usr/bin/python
"""
This Program is for Guessing the number that user entered by computer.
"""

import random


def guess_by_pc():
    """
    This function is a game. You Enter a Number betwen
    1 & 100 and computer must guess it!
    """
    low, high = 1, 100
    while 1:
        try:
            x_1 = int(input("Please Enter a number between 1 & 100: "))
        except ValueError:
            print("Invalid Input.")
            continue
        else:
            break
    guess = random.randint(low, high)
    while low != high:
        while 1:
            print(f"The Guessed number is {guess}. status? l/h/c", end="\t")
            stat = input()
            if stat not in ("l", "h", "c"):
                print("Invalid Input.")
            else:
                break
        if stat == "l":
            low = guess + 1
            guess = random.randint(low, high)
        elif stat == "h":
            high = guess - 1
            guess = random.randint(low, high)
    print(f"Correct! the number is {x_1}")


guess_by_pc()
