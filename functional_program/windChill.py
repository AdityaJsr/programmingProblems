"""
title - This is a program that calculates the WindChill by taking the Temerature and velocity of wind as an input.
author name - Aditya Kumar
creation time - ‎22 ‎February ‎2021, ‏‎11:06:57
modified time - 22 ‎February ‎2021, ‏‎15:07:26

"""

# Importing math package
import math

# Function to input and do the computation.
def windChill():
    # User input for temperature in Fahrenheit.
    t = float(input("Enter the temperature in Fahrenheit : "))
    # User input for wind speed in Miles/hour.
    v = float(input("Enter the wind speed in Miles/hour : ")) 
    # Condition for the computaion to be correct.
    if (t>50) or (v>120) or (v<3):
        print("Unable to calculate the windchill index as the values are out of range :\n Try again")
        # Recall the function.
        windChill()
    else:
        # Formula to calculate windchill.
        wci = 35.74 + 0.6215*t + ((0.4275*t)*math.pow(v, 0.16) - 35.75*math.pow(v, 0.16))
        print("The wind chill index is", int(round(wci, 0)))

# The main function.
if __name__ == "__main__":
    windChill()
