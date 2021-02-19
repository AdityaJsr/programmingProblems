"""
 First Project 
This is a basic program for string replacement
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