# This is a program to to find the percentage of Heads/Tails of a coin flip


import random

def flip():
    heads = 0
    user_input = input("Enter the number of times you want to flip a coin : ")
    for i in range(int(user_input)):
        coin = random.randint(0 , 1)
        if coin==1:
            heads += 1
    percent = (heads / int(user_input)*100)
    print("The probability for Heads = " + str(percent) +"%\n")
    print("The probability for tails = " + str(100-percent) +"%\n")


if __name__=='__main__':
    flip()