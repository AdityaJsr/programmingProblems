import math

def user_input():
    a = []
    for i in range (4):
        a.append(int(input("Enter the Coordinates: ")))
    return a

def distance():
    x1,y1,x2,y2 = user_input()
    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    print("The Euclidean Distance is " + str(dist))

if __name__ == "__main__":
    distance()