
import json
import os
from os import path
doctorsData = []                # Global array to create new json array

'''
Function:
        The function addDoctor() is to add new doctors in the JSON file.
Arguments:
        calls function createData() to take user input.
        calls function deSerialzeJson() to create/read JSON file.
Returns:
        none.
Errors:
        none.
'''
def addDoctor():
    os.chdir('D:/vs studio/bridgeLabz/codes')

    if(path.exists("clinicData.json")):

        with open('clinicData.json') as f:
            if f.read() == '':
                
                data= {} 
                x = createData()
                doctorsData.append(x)
                data['doctorsData'] = doctorsData
                json_obj = json.dumps(data, indent=2)

                with open("clinicData.json", "w") as f:
                    f.write(json_obj)
            else:

                data = deSerialzeJson()
                x = createData()

                data["doctorsData"].append(x)
                json_obj = json.dumps(data, indent=2)

                with open("clinicData.json", "w") as f:
                    f.write(json_obj)
        
    else:
        
        data= {} 
        x = createData()

        doctorsData.append(x) 
        data['doctorsData'] = doctorsData
        json_obj = json.dumps(data, indent=2)

        with open("clinicData.json", "w") as f:
            f.write(json_obj)
'''
Function:
        The function doctorID() is to add ID to the doctors in the JSON file.
Arguments:
        calls function deSerialzeJson() to create/read JSON file.
Returns:
        id.
Errors:
        none.
'''
def doctorID():
    id = 1
    os.chdir('D:/vs studio/bridgeLabz/codes')
    if(path.exists("clinicData.json")):
        with open('clinicData.json') as f:
            if f.read() == '':
                return(id)
            else:
                
                data = deSerialzeJson()
                id = len(data['doctorsData'])
                return(id+1)
'''
Function:
        The function shiftInput() is to add shift for doctors.
Arguments:
        none.
Returns:
        none.
Errors:
        none.
'''
def shiftInput():
    checkShift = input("Enter shift AM/PM/BOTH : ").upper()
    if (checkShift == 'AM') or (checkShift == 'PM') or (checkShift == 'BOTH'):
        return(checkShift)
    else:
        print("Please enter a proper shift : ")
        shiftInput()
'''
Function:
        The function createData() is to take user input and send it to addDoctor().
Arguments:
        calls function shiftInput() to add shift of the doctor.
Returns:
        x an object of userInput in the form of dictonary.
Errors:
        none.
'''
def createData():
    name = input("Enter the name : ").upper()
    id = str(doctorID())
    specialization = input("Enter the doctors specialization : ").upper()
    shift = shiftInput()

    x = {
        'name': 'DR '+name, 
        'id'   : id,
        'specialization': specialization,
        'shift': shift
        }    

    return(x)
'''
Function:
        The function showDoctor() is depict all the doctors from JSON file.
Arguments:
        calls function deSerialzeJson() to create/read JSON file.
Returns:
        none.
Errors:
        none.
'''
def showDoctor():

    # Read Json File ->  Record.Json file
    data = deSerialzeJson()
    count = 0
    for doctors in data['doctorsData']:
        print("\nname: " + doctors['name'] + "\n" + "id : " + doctors['id'] + "\n" + "specialization : " + doctors['specialization'] + "\n" +
                "shift : " + doctors['shift']+"\n")
'''
Function:
        The function deSerialzeJson() to create/read JSON file.
Arguments:
        none.
Returns:
        none.
Errors:
        none.
'''
def deSerialzeJson():
    with open('clinicData.json') as f:
        data = json.loads(f.read())
    return(data)
