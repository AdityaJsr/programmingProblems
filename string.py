"""
title - This is a basic program for string replacement
author name - Aditya Kumar
creation time - 18 ‎February ‎2021
modified time - 20 ‎February ‎2021

"""

def replace():
    user_input = input("Enter the User name :")
    if(len(user_input) >= 3):
        if (user_input[0][0].isdigit()):
            print("invalid Username: usernames cannot start with a number")
        else:
            print("Hello "+user_input+" , How are you?")
    else:
        print("Invalid user name\nminimum 3 characters")
        replace()
    

if __name__ =="__main__":
    replace()