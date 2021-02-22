
import cmath 


def quadEq():
    
    a = int(input("Enter the value of a : "))
    b = int(input("Enter the value of b : "))
    c = int(input("Enter the value of c : "))

    # try:
    #     a.isdigit() == True
    #     b
    #     c
    # except ValueError:
    #     print("The values provided are not valid :")

    # calculating the discriminant 
    dis = (b**2) - (4 * a*c) 

    ans1 = (-b-cmath.sqrt(dis))/(2 * a) 
    ans2 = (-b + cmath.sqrt(dis))/(2 * a) 

    # printing the results 
    print('The roots are') 
    print(ans1) 
    print(ans2) 
    
    

if __name__ == "__main__":
    quadEq()




