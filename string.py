# First Project 
def replace():
    user_input = input("Enter the User name :")
    if(len(user_input) >= 3):
        print("Hello "+user_input+" , How are you?")
    else:
        print("Invalid user name\nminimum 3 characters")
        replace()
    

if __name__ =="__main__":
    replace()