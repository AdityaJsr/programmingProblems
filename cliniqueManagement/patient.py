
# This module is to add patients
import json
import os
from os import path


patientData = []
data = {}


def addPatient():

    os.chdir('D:/vs studio/bridgeLabz/codes')

    if(path.exists("patientRecord.json")):

        with open('patientRecord.json') as f:
            if f.read() == '':

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
        
        x = createPatientData()
        patientData.append(x) 
        data['patientData'] = patientData
        json_obj = json.dumps(data, indent=2)

        with open("patientRecord.json", "w") as f:
            f.write(json_obj)


def createPatientData():
    name = input("Enter the name of the patient : ").upper()
    id = input("Enter the id of the patient : ")
    mobileNumber = input("Enter your mobile number : ")
    age = input("Enter your age : ")

    x = {
        'name': name, 
        'id'   : id,
        'specialization': mobileNumber,
        'shift': age
        }    

    # print("X is being returned")

    return(x)


def deSerialzePatientData():
    with open('patientRecord.json') as f:
        data = json.loads(f.read())
    return(data)



if __name__ == "__main__":
    choice = input("Enter 1 if you want an appointment : ")
    if (choice == '1'):
        addPatient()