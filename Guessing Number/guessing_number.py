#! /usr/bin/python3

import random


def hads(x_1: int):
    """
    This Function actually generate a random integer between 1 and x_1
    """
    random_number = random.randint(1, int(x_1))
    guess = 0
    while guess != random_number:
        try:
            guess = int(input(f"Please Guess a number between 1 & {x_1}: "))
        except ValueError:
            print("Invelid Input. ")
            continue
        if guess < random_number:
            print("is Low!")
            continue
        if guess > random_number:
            print("Higher")
            continue
        print("Correct!")


while 1:
    try:
        ran = input("Please Enter your Range: ")
    except ValueError:
        print("Invalid Input. ")
        continue
    else:
        break

print(hads(ran))
