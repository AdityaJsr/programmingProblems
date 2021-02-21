"""
title - This is a program that computes the prime factorization of N using brute force.
author name - Aditya Kumar
creation time - 18 ‎February ‎2021
modified time - 20 ‎February ‎2021

"""
import math

def factorization():
    user_input = input("Enter the number to find it's Prime-factoes : ")
    num = int(user_input)
    while num%2== 0:
        print(2)
        num = num/2
    for i in range(3, int(math.sqrt(num))+1, 2): 
        while num % i == 0: 
            print (i)
            num = num / i 

    if num > 2: 
        print (num) 

if __name__ == '__main__':
    factorization()

