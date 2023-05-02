#! /usr/bin/python3

import random


def hads():
    """
    This Function actually generate a random integer between 1 and x_1
    """
    x_1 = input("Please Enter Range: ")
    while 1:
        try:
            random_number = random.randint(1, int(x_1))
        except ValueError:
            print("Invalid Input. ")
            x_1 = input("Please Enter Range: ")
            continue
        else:
            break
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Please Guess a number between 1 & {x_1}: "))
        except ValueError:
            print("Invelid Input. ")
            continue
        if guess < random_number:
            print("is Low!")
        if guess > random_number:
            print("Higher")
    print(f"Correct! The guessed number is {x_1}")


hads()
