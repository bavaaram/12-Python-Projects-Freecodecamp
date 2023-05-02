#! /usr/bin/python3
"""
This Program is for Guessing the number that user entered by computer.
"""

import random


def guess_by_pc(x_1):
    """
    This function is a game. You Enter a Number betwen
    1 & 100 and computer must guess it!
    """
    low, high, stat = 1, x_1, ""
    guess = random.randint(low, high)
    while stat != "c":
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
    print(f"Correct! the number is {guess}")


guess_by_pc(1000)
