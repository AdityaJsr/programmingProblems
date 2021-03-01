
# This module is to add patients
import json
import os
from os import path


patientData = []            # Global empty array.

'''
Function:
        The function addPatient() is to add new patient in the JSON file.
Arguments:
        calls function createPatientData() to take user input.
        calls function deSerialzePatientData() to create/read JSON file.
Returns:
        none.
Errors:
        none.
'''
def addPatient():

    os.chdir('D:/vs studio/bridgeLabz/codes')

    if(path.exists("patientRecord.json")):

        with open('patientRecord.json') as f:
            if f.read() == '':
                data = {}
                x = createPatientData()

                patientData.append(x) 
                data['patientData'] = patientData
                json_obj = json.dumps(data, indent=2)

                with open("patientRecord.json", "w") as f:
                    f.write(json_obj)
                
            else:

                data = deSerialzePatientData()
                x = createPatientData()

                data["patientData"].append(x)
                json_obj = json.dumps(data, indent=2)

                with open("patientRecord.json", "w") as f:
                    f.write(json_obj)
        
    else:
        
        data = {}
        x = createPatientData()
        patientData.append(x) 
        data['patientData'] = patientData
        json_obj = json.dumps(data, indent=2)

        with open("patientRecord.json", "w") as f:
            f.write(json_obj)
'''
Function:
        The function patientId() is to add ID to the patient in the JSON file.
Arguments:
        calls function deSerialzePatientData() to create/read JSON file.
Returns:
        id.
Errors:
        none.
'''
def patientId():
    id = 1
    os.chdir('D:/vs studio/bridgeLabz/codes')
    if(path.exists("patientRecord.json")):
        with open('patientRecord.json') as f:
            if f.read() == '':
                return(id)
            else:    
                data = deSerialzePatientData()
                id = len(data['patientData'])
                return(id+1)
'''
Function:
        The function validateMobileNumber() is to validate and add patients mobile number in the JSON file.
Arguments:
        none.
Returns:
        id.
Errors:
        none.
'''
def validateMobileNumber():
    mobileNumber = input("Enter your mobile number : ")
    if(mobileNumber.isdigit() == True) and (len(mobileNumber) == 10) and (mobileNumber != None):
        return(mobileNumber)
    else:
        print("'Error' , Please Enter a valid Phone Number :")
        validateMobileNumber()
'''
Function:
        The function validateAge() is to validate and add patients age in the JSON file.
Arguments:
        none.
Returns:
        age.
Errors:
        none.
'''
def validateAge():
    age = input("Enter your age : ")
    if(age.isdigit() == True) and (int(age)>0) and (int(age)<120):
        return(age)
    else:
        print("'Error' , Please Enter a valid age :")
        validateAge()
'''
Function:
        The function createPatientData() is take userInput for patient details.
Arguments:
        calls function patientId() to add Id create/read JSON file.
        calls function validateAge() to add age create/read JSON file.
        validateAge
Returns:
        none.
Errors:
        none.
'''
def createPatientData():
    name = input("Enter the name of the patient : ").upper()
    id = patientId()
    mobileNumber = validateMobileNumber()
    age = validateAge()

    x = {
        'name': name, 
        'id'   : id,
        'mobileNumber': mobileNumber,
        'age': age
        }    

    return(x)
'''
Function:
        The function deSerialzePatientData() to create/read JSON file.
Arguments:
        none.
Returns:
        none.
Errors:
        none.
'''
def deSerialzePatientData():
    with open('patientRecord.json') as f:
        data = json.loads(f.read())
    return(data)


if __name__ == "__main__":
    choice = input("Enter 1 if you want an appointment : ")
    if (choice == '1'):
        addPatient()