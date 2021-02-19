def exponent():
    user_input = input("Enter a exponent value: ")
    if(user_input.isdigit()):
        expo = int(user_input)
        if(expo>=0) and (expo<= 31):
            output = pow(2, expo)
            print("The output for the above expo facor is:"+str(output))
        else:
            print("The exponent value cannot be less than 0 or more than 31")
            exponent()
    else:
        print("The input has to be an integer")
        exponent()
if __name__ == "__main__":
    exponent()
