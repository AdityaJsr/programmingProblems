def exponent():
    user_input = input("Enter a exponent factor: ")
    expo = int(user_input)
    if(expo>=0)and (expo<= 31):
        output = pow(2, expo)
        print("The output for the above expo facor is:"+str(output))

if __name__ == "__main__":
    exponent()
