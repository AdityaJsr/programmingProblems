"""
title - This is a program calculate Euclidean distance from the coordinates.
author name - Aditya Kumar
creation time - 22 ‎February ‎2021, ‏‎16:05:21
modified time - 22 ‎February ‎2021, ‏‎16:08:08

"""

import math

def user_input():
    a = []
    for i in range (4):
        a.append(int(input("Enter the Coordinates: ")))
    return a

def distance():
    x1,y1,x2,y2 = user_input()
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("The Euclidean Distance is " + str(dist))

if __name__ == "__main__":
    distance()