"""
title - This is a program converts temperature from Fahrenheit to Celsius or viceversa.
author name - Aditya Kumar
creation time - ‎22 ‎February ‎2021, ‏‎11:30:03
modified time - 23 ‎February ‎2021, ‏‎12:29:21

"""
# The function for user_input() for choice.
def user_input():
    choice = int(input("Enter 1 if you want to convert Celsius to Fahrenheit : \n or 2 to convert Fahrenheit to Celsius :"))
    # Returning the choice to convertor function().
    return (choice)

# The function for temperature conversion.
def convertor():
    ch = int(user_input())
    # Choice 1 for converting Celsius to Fahrenheit.
    if (ch == 1):
        temp = float(input("Enter the temperature in Celsius : "))
        output = (temp*1.8)+32
        print("The Fahrenheit equivalent of "+str(temp)+"°C = "+str(output)+"°F")
    # Choice 2 for converting Fahrenheit to Celsius.
    elif(ch == 2):
        temp = float(input("Enter the temperature in Fahrenheit : "))
        output = (temp - 32)*(5/9)
        print("The Celsius equivalent of "+str(temp)+"°F = "+str(output)+"°C")
    # # Error message for wrong choice.
    # else:
    #     print("select a proper value for conversion : ")
    #     user_input()

# The main function.
if __name__ == "__main__":
    convertor()
