#! /usr/bin/python3

import random


def guess_by_pc():
    """
    This function is a game. You Enter a Number betwen
    1 & 100 and computer must guess it!
    """
    a, b = 1, 100
    while 1:
        try:
            x_1 = int(input("Please Enter a number between 1 & 100: "))
        except ValueError:
            print("Invalid Input.")
            continue
        else:
            break
    guess = random.randint(a, b)
    while guess != x_1:
        print(f"The Guessed number is {guess}. status? l/h", end="\t")
        while 1:
            stat = input()
            if stat not in ("l", "h"):
                print("Invalid Input.")
            else:
                break
        if stat == "l":
            a = guess + 1
            guess = random.randint(a, b)
        else:
            b = guess - 1
            guess = random.randint(a, b)
    print(f"The Guessed number is {guess}.\n Correct!")


guess_by_pc()
