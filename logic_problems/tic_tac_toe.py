# # Create a game board of 3*3 matrix


# # def player():
# #     r = int("Enter the row index :")
# #     c = int("Enter the col index :")
# #     if ()

# # if __name__  == "__main__":
# #     gameBoard()
# # A basic code for matrix input from user 
  
# R = 3 
# C = 3
  
# # Initialize matrix 
# matrix = [] 
# # print("Enter the entries rowwise:") 
  
# # For user input 
# for i in range(R):          # A for loop for row entries 
#     a =[] 
#     for j in range(C):      # A for loop for column entries 
#          a.append(0) 
#     matrix.append(a) 
  
# # For printing the matrix 
# for i in range(R): 
#     for j in range(C): 
#         print(matrix[i][j], end = " ") 
#     print() 

# # For user input and matrix manipulation:
# x = int(input("Enter the row number you want to manipulate : "))
# y = int(input("Enter the col number you want to manipulate : "))

# for i in range(x):
#     for j in range (y):
#         if (matrix[x][y]) == 0):
#             matrix[x][y] = "X"
#         # else:
#         #     print("Invalid move Try again : ")
# for i in range(R): 
#     for j in range(C): 
#         print(matrix[i][j], end = " ") 
#     print()

import numpy as np

a = np.array([[0,0,0],[0,0,0],[0,0,0]])
print(a)
# For user input and matrix manipulation:
x = int(input("Enter the row number you want to manipulate : "))
y = int(input("Enter the col number you want to manipulate : "))

if (a[x,y] != 0):
    a[x,y] = "1"
    print(a)
    

