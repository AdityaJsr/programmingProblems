"""
title - This program is Clinic Management system which keeps records a doctor's as well as patient's attributes .
author name - Aditya Kumar
creation time - 24 ‎February ‎2021, 17:23:24
modified time - ‎24 ‎February ‎2021, ‏‎

"""

import json

# data = {}
# doctorsData = []
def addDoctor():
    
    data = deSerialzeJson()
    
    name = input("Enter the name : ")
    id = input("Enter the id : ")
    specialization = input("Enter the doctors specialization : ")
    shift = input("Enter shift: ")

    x = {
        'name': 'Dr '+name, 
        'id'   : id,
        'specialization': specialization,
        'shift': shift
        }
    # Remember to add if condition to check if the clinicData.json file exist.
    # doctorsData.append(x)
    data["doctorsData"].append(x)
    json_obj = json.dumps(data, indent=2)

    with open("clinicData.json", "w") as f:
        f.write(json_obj)


    

def showDoctor():

    # Read Json File ->  Record.Json file
    data = deSerialzeJson()
    count = 0
    for doctors in data['doctorsData']:
        print("\nname: " + doctors['name'] + "\n" + "id : " + doctors['id'] + "\n" + "specialization : " + doctors['specialization'] + "\n" +
                "shift : " + doctors['shift']+"\n")


def deSerialzeJson():
    with open('clinicData.json') as f:
        data = json.loads(f.read())
    return(data)


if  __name__ == "__main__":
    print("Clinique Management System")
    ch = input("1. Enter 1 to add a doctor \n2. Enter 2 to see all avaiable doctors : \nEnter your choice : ")

    if (ch =='1'):
        addDoctor()
    elif (ch == '2'):
        showDoctor()