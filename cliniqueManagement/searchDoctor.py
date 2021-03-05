# This is the search module.
from doctor import deSerialzeJson
import json
import os
from os import path


def byName():

    key = input("Enter the name of the Doctor : ").upper()
    data = deSerialzeJson()

    for doctors in data['doctorsData']:
        try:
            dName = doctors['name'].split(' ')
            if(key == dName[1])or(key == dName[2])or(key == dName[1]+" "+dName[2]):
                print("\nname: " + doctors['name'] + "\n" + "id : " + doctors['id'] + "\n" + "specialization : " + doctors['specialization'] + "\n" +
                    "shift : " + doctors['shift']+"\n")
                return 
        except IndexError:
            pass
        except Exception as e:
            print("An unknown error is occouring", e)
    print("Doctor not found")


    
            
def byid():

    key = input("Enter the id of the Doctor : ")
    data = deSerialzeJson()

    for doctors in data['doctorsData']:
        if(key == doctors['id']):
            print("\nname: " + doctors['name'] + "\n" + "id : " + doctors['id'] + "\n" + "specialization : " + doctors['specialization'] + "\n" +
                "shift : " + doctors['shift']+"\n")
def bySpecialization():

    key = input("Enter the specialzation of the Doctor : ").upper()
    data = deSerialzeJson()

    for doctors in data['doctorsData']:
        if(key == doctors['specialization']):
            print("\nname: " + doctors['name'] + "\n" + "id : " + doctors['id'] + "\n" + "specialization : " + doctors['specialization'] + "\n" +
                "shift : " + doctors['shift']+"\n")
def byAvailability():

    key = input("AM/PM/Both : ").upper()
    data = deSerialzeJson()

    for doctors in data['doctorsData']:
        if(key == doctors['shift']):
            print("\nname: " + doctors['name'] + "\n" + "id : " + doctors['id'] + "\n" + "specialization : " + doctors['specialization'] + "\n" +
                "shift : " + doctors['shift']+"\n")
def keySearch():

    choice = input("Search doctor by : \n1. Name \n2. ID \n3. Specialization \n4. Availability \nEnter your choice : ")
    if (choice == '1'):
        byName()

    elif (choice == '2'):
        byid()
    
    elif (choice == '3'):
        bySpecialization()
    
    elif (choice == '4'):
        byAvailability()
    
    else:
        print("Enter a proper choice : ")
        keySearch()
