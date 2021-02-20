"""
title - This is a program to generate the exponent table of 2 from from user-input
author name - Aditya Kumar
creation time - 18 ‎February ‎2021
modified time - 20 ‎February ‎2021

"""

def exponent():
    user_input = input("Enter a exponent value: ")
    if(user_input.isdigit()):
        expo = int(user_input)
        if(expo>=0) and (expo<= 31):
            for i in range(expo):
                print("2^"+str(i)+" = "+str(pow(2,i)))
        else:
            print("The exponent value cannot be less than 0 or more than 31")
            exponent()
    else:
        print("The input has to be an integer")
        exponent()
if __name__ == "__main__":
    exponent()
