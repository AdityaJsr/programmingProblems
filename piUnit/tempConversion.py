def user_input():
    choice = int(input("Enter 1 if you want to convert Celsius to Fahrenheit : \n or 2 to convert Fahrenheit to Celsius :"))
    return (choice)

def convertor():
    ch = int(user_input())
    temp = float(input("Enter the temperature : "))
    if (ch == 1):
        print("The Fahrenheit equivalent of "+str(temp)+"°C = "+str(output)+"°F")
        print(output)
    elif(ch == 2):
        output = (temp - 32)*(5/9)
        print("The Celsius equivalent of "+str(temp)+"°F = "+str(output)+"°C")
    else:
        print("select a proper value for conversion : ")
        user_input()

if __name__ == "__main__":
    convertor()
