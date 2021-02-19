def leapYear():
    user_input = input("Enter the Year : ")
    input_lenghth = len(user_input)
    if user_input.isdigit():
 
    else:
        print("years can be entered only as a numeric value :")
        leapYear()

if __name__ == "__main__":
    leapYear()

