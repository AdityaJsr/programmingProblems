"""
title - This is a program is to calculate the roots of quadratic equation.
author name - Aditya Kumar
creation time - 22 ‎February ‎2021, ‏‎10:23:12
modified time - ‎22 ‎February ‎2021, ‏‎16:09:05

"""
import cmath 


def quadEq():
    
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    c = int(input("Enter the value of c : "))
    dis = (b**2) - (4 * a*c) 

    ans1 = (-b-cmath.sqrt(dis))/(2 * a) 
    ans2 = (-b + cmath.sqrt(dis))/(2 * a) 

    print('The roots are') 
    print(ans1) 
    print(ans2) 
    
    

if __name__ == "__main__":
    quadEq()




