"""
title - This is a program converts temperature from Fahrenheit to Celsius or viceversa.
author name - Aditya Kumar
creation time - ‎22 ‎February ‎2021, ‏‎11:30:03
modified time - 23 ‎February ‎2021, ‏‎12:29:21

"""
# The function for user_input() for choice.
def user_input():
    choice = int(input("Enter 1 to convert Celsius to Fahrenheit : \nEnter 2 to convert Fahrenheit to Celsius :\n ch = : "))
    if choice == 1:
        temp = float(input("Enter the temperature in Celsius : "))
        celsiusToFahrenheit(temp)
    elif choice ==2:
        temp = float(input("Enter the temperature in Fahrenheit : "))
        fahrenhietToCelsius(temp)
    else:
        print("Please enter a valid choice between 1 and 2 : ")
        user_input()
    

# The function for temperature conversion from Celsius to Fahrenheit.
"""
function:
celsiusToFahrenheit() converts temperature from Fahrenheit to Celsius.

argument:
temp - user-input to temperature(from celsius to fahrenhiet)

return value:
output - the converted value of user_input(in fahrenheit)

error:
none

"""
def celsiusToFahrenheit(temp):
    output = int((temp*1.8)+32)
    print("The Fahrenheit equivalent of "+str(temp)+"°C = "+str(output)+"°F")
    return round(output)
"""
function:
fahrenhietToCelsius() converts temperature from Fahrenheit to Celsius

argument:
temp - user-input to temperature(from fahrenhiet to celsius)

return value:
output - the converted value of user_input (in celsius)

error:
none

"""
# The function for temperature conversion from Fahrenheit to Celsius.
def fahrenhietToCelsius(temp):
    output = (temp - 32)*(5/9)
    print("The Celsius equivalent of "+str(temp)+"°F = "+str(output)+"°C")
    return round(output)

# The main function.
if __name__ == "__main__":
    user_input()
