"""
title - This is a program called addressbook which records a person's first and last names, address, city, state, zip, and
phone number.
author name - Aditya Kumar
creation time - 24 ‎February ‎2021, 17:23:24
modified time - ‎24 ‎February ‎2021, ‏‎

"""
import json
import pprint

data = {}


def choice():
    ch = 0
    print("Enter 1 to add ")
    print("Enter 2 to edit ")
    print("Enter 3 to delete ")
    print("Enter 1 to add ")


def createUser():
    # Read Json File ->  Record.Json file
    with open('record.json') as f:
        data = json.loads(f.read())

    # User Input Details
    firstName = input("Enter the first name : ")
    lastName = input("Enter the last name : ")
    address = input("Enter the address : ")
    city = input("Enter city : ")
    state = input("Enter state : ")
    zip = input("Enter the zip code : ")
    phoneNumber = input("Enter your Phone-Number : ")

    # Create Details Dictionary ( JSON )
    x = {"firstName": firstName,
         "lastName": lastName,
         "address": address,
         "city": city,
         "state": state,
         "zip": zip,
         "phoneNumber": phoneNumber
         }

    # Append  Details Dictionary to JSON['person']
    data["person"].append(x)

    # Serialize the date to json format
    json_obj = json.dumps(data, indent=2)

    # Saving Serialized Json to Record.Json file
    with open("record.json", "w") as f:
        f.write(json_obj)


def showUserInJson():

    # Read Json File ->  Record.Json file
    with open('record.json') as f:
        data = json.loads(f.read())
        pprint.pprint(data)


def showUser():

    # Read Json File ->  Record.Json file
    with open('record.json') as f:
        data = json.loads(f.read())

        for user in data['person']:
            print("\nFirstName: " + user['firstName'] + "\n" + "Last Name : " + user['lastName'] + "\n" + "Address : " + user['address'] + "\n" +
                  "City : " + user['city'] + "\n" + "State : " + user['state'] + "\n" + "Zipcode : " + user['zip'] + "\n" + "Phone Number : " + user['phoneNumber'] + "\n")


if __name__ == "__main__":
    while True:
        print(" ")
        print("User Management Panel")
        print("1.Create User  |  2.Show Users In Json Format   | 3. Show Users ")

        val = input("Enter your choice : \n\n")

        if(val == "1"):
            createUser()
        elif (val == "2"):
            showUserInJson()
        elif (val == "3"):
            showUser()
        else:
            print("Choose menu options as 1 , 2 pr 3 to proceed further")