"""
title - This is a program to print the harmonic number
author name - Aditya Kumar
creation time - 19 ‎February ‎2021
modified time - 20 ‎February ‎2021

"""

def harmonic():
    user_input = input("Enter the number to find the nth value :")
    value = int(user_input)
    hVal = 0
    if(user_input.isdigit()):
        for i in range(1,value):
            hVal = hVal+(1/i)
            print(hVal)
    else:
        print("The input should be a numeric value :")
        harmonic()

if __name__ == "__main__":
    harmonic()
