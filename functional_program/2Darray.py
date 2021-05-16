'''
 Author: Aditya Kumar
 Date: 2021-02-12 
 Last Modified date: 2021-02-14  
 Title : Create 2D array Problem
'''


while True:    
    try:
        row=int(input("enter the number of row: "))
        column=int(input("enter the number of coloumns: "))
        array=[ [input("enter the value: ") for c in range(column)] for r in range(row)]
        print("2D array:", array)
        break
    except ValueError:
        print("enter int number only try again!!")
