import json
import os
from os import path
from doctor import deSerialzeJson

'''
Function:
        The function checkDoctor() is check if the doctor exists in the JSON file.
Arguments:
        calls function createPatientData() to take user input.
        calls function deSerialzeJson() to create/read JSON file.
Returns:
        doctorMatch : The name of the doctor that matches the search value.
Errors:
        none.
'''

def checkDoctor():
    queryName = input("Enter the name of the doctor you want you appointment with : ").upper()
    data = deSerialzeJson()
    for doctors in data['doctorsData']:
        if(doctors['name'] == queryName):
            doctorMatch = doctors['name']
            return(doctorMatch)
            # Able to search doctors;

'''
Function:
        The function appointDoctor() is add appointments of doctor in the JSON file.
Arguments:
        calls function checkDoctor() to check if the doctor exists in the JSON file.
        calls function deSerialzeJson() to create/read JSON file.
Returns:
        none.
Errors:
        none.
'''
def appointDoctor():

    match = checkDoctor()
    client = input("Enter the your name : ")
    appointment = []
    appointment.append(client)
    data = deSerialzeJson()
    flag = False
    for doctors in data['doctorsData']:
        # print ( doctors['name'], match)
       
        if doctors['name'] == match:
                flag =True
                if 'appointment' in list(doctors.keys()):

                    if len(doctors['appointment'])<5:
                        doctors['appointment'].append(client)
                        
                    else:
                        print('Sorry appointment list is full : ')    
                else:
                    doctors['appointment'] = appointment
    if flag is not True:
            print("Doctor unavailable : ")

    json_obj = json.dumps(data, indent=2)
    with open("clinicData.json", "w") as f:
        f.write(json_obj)


if __name__ == "__main__":
    appointDoctor()

