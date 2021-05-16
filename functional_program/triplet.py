"""
title - This is a program that Read in N integers and counts the number of triples that sum to exactly 0.
author name - Aditya Kumar
creation time - 20 ‎February ‎2021, ‏‎16:18:58
modified time - 20 ‎February ‎2021, ‏‎20:39:50

"""

# Function to take user-input.
def user_input():
    # Inetilization of an empty array to take user input.
    a = []
    # Take the number of inputs the user wants to give. 
    n = int(input("enter the number of inputs : "))
    # Loop to append the value in the array a.
    for i in range (n):
        a.append(input("Enter the value: "))
    # Return the values stored in array.
    return a

# Target function the computes the input and gives final output.
def triplet():
    # Collecting the returned value by the user_input function.
    values = user_input()
    # Counter for the number of triplets.
    count = 0
    # Loop 1 on 0th index of the array of user_input.
    for i in range(len(values)):
        # Loop 2 on 1st index of the array of user_input.
        for j in range(1,len(values)):
            # Loop 3 on 2nd index of the array of user_input.
            for k in range(2,len(values)):
                # Condition for triplets with output as 0
                if (int(values[i])+int(values[j])+int(values[k]) == 0):
                    print(int(values[i]),int(values[j]),int(values[k]))
                    # Increment count each time a triplet is found.
                    count += 1
    # The print function.
    print("Number of distinct triplets :"+str(count))

# The main function.
if __name__ == "__main__":
    triplet()
    

        