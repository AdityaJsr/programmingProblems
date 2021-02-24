"""
title - This is a program called addressbook which records a person's first and last names, address, city, state, zip, and
phone number.
author name - Aditya Kumar
creation time - 24 ‎February ‎2021, 17:23:24
modified time - ‎24 ‎February ‎2021, ‏‎

"""
import json
# class AddressBook:

    # def newEntry(self , first, last, address , city , state , zip, phoneNumber):
    #     self.first = first
    #     self.last = last
    #     self.address = address
    #     self.city = city
    #     self.state = state
    #     self.zip = zip
    #     self.phoneNumber = phoneNumber
data = {}
def createUser():
    firstName = input("Enter the first name : ")
    lastName = input("Enter the last name : ")
    address = input("Enter the address : ")
    city = input("Enter city : ")
    state = input("Enter state : ")
    zip = input("Enter the zip code : ")
    phoneNumber = input("Enter your Phone-Number : ")

    data["firstName"] = firstName
    data["lastName"] = lastName
    data["address"] = address
    data["city"] = city
    data["state"] = state
    data["zip"] = zip
    data["phone-Number"] = phoneNumber
    json_obj = json.dumps(data, indent=2)
    return(json_obj)

def saveUser(json_obj):
    record = open("myfile.json", "w") 
    json.dump(json_obj, record, indent = 2) 
    record.close()  


if __name__ == "__main__":
    data = createUser()
    saveUser(data)
