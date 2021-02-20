"""
title - This is a program to to find the percentage of Heads/Tails of a coin flip
author name - Aditya Kumar
creation time - 18 ‎February ‎2021
modified time - 20 ‎February ‎2021

"""

import random

def flip():
    heads = 0
    user_input = input("Enter the number of times you want to flip a coin : ")
    val = user_input
    try:
        val = int(user_input)
    except ValueError:
        print("That's not an int!")
    for i in range(val):
        coin = random.randint(0 , 1)
        if coin==1:
            heads += 1
    percent = (heads / int(user_input)*100)
    print("The probability for Heads = " + str(percent) +"%\n")
    print("The probability for tails = " + str(100-percent) +"%\n")


if __name__=='__main__':
    flip()