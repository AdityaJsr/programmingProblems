def leapYear():
    user_input = input("Enter the Year : ")
    input_lenghth = len(user_input)
    if user_input.isdigit():
        year = int(user_input)
        if (input_lenghth == 4):
            if(year%4 == 0):
                if(year%100 == 0):
                    if(year%400 == 0 ):
                        print("-----"+user_input+" is a Leap year-----")
                    else:
                        print("-----"+user_input+" is not a Leap year-----")
                else:
                    print("-----"+user_input+" is not a Leap year-----")
            else:
                print("-----"+user_input+" is not a Leap year-----")
        else:
            print("please enter a valid year :")
            leapYear()
    else:
        print("years can be entered only as a numeric value :")
        leapYear()

if __name__ == "__main__":
    leapYear()