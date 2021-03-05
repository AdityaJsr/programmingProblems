"""
title - This is a program called addressbook which records a person's first and last names, address, city, state, zip, and
phone number.
author name - Aditya Kumar
creation time - 24 ‎February ‎2021, 17:23:24
modified time - ‎24 ‎February ‎2021, ‏‎

"""
import json
import pprint


def createUser():
    # Read Json File ->  Record.Json file
    data = serialzeJson()

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

    # Saving Serialized Json to Record.Json file after appending.
    with open("record.json", "w") as f:
        f.write(json_obj)


def showUserInJson():
    # Read Json File ->  Record.Json file
    data = serialzeJson()
    pprint.pprint(data)


def showUser():

    # Read Json File ->  Record.Json file
    data = serialzeJson()

    for user in data['person']:
        print("\nFirstName: " + user['firstName'] + "\n" + "Last Name : " + user['lastName'] + "\n" + "Address : " + user['address'] + "\n" +
                "City : " + user['city'] + "\n" + "State : " + user['state'] + "\n" + "Zipcode : " + user['zip'] + "\n" + "Phone Number : " + user['phoneNumber'] + "\n")

def delUser():
    # Read Json File ->  Record.Json file
    data = serialzeJson()

    # index to display for delete option
    index = 1
    for user in data['person']:
        print(str(index)+"\t" + user['firstName']+" "+user['lastName']+"\n")
        index += 1
    indexDelete = int(input("Input the index number of the user you want to delete : "))
    del (data["person"][indexDelete-1])

    # Serialize the date to json format
    json_obj = json.dumps(data, indent=2)
    # Saving Serialized Json to Record.Json file after deleting.
    with open("record.json", "w") as f:
        f.write(json_obj)

def editUser():
    # Read Json File ->  Record.Json file
    data = serialzeJson()

    index = 1
    for user in data['person']:
        print(str(index)+"\t" + user['firstName']+" "+user['lastName']+"\n")
        index += 1
    indexEdit = int(input("Input the index number of the user you want to edit : "))
    print("1. lastName \n2. address\n3. city \n4. state \n5. zip \n6. phoneNumber")
    choice = str(input("Enter the field you want to edit : "))
    update = str(input("Enter the Updated Data : "))
    for user in data['person']:
        data["person"][indexEdit-1][choice] = update

    # Serialize the date to json format
    json_obj = json.dumps(data, indent=2)
    # Saving Serialized Json to Record.Json file after deleting.
    with open("record.json", "w") as f:
        f.write(json_obj)

def serialzeJson():
    with open('record.json') as f:
        data = json.loads(f.read())
    return(data)

if __name__ == "__main__":
    while True:
        print(" ")
        print("User Management Panel")
        print(" 1.Create User \n 2.Show Users In Json Format \n 3. Show Users \n 4. Delete User \n 5. edit User")

        val = input("Enter your choice : \t")

        if(val == "1"):
            createUser()
        elif (val == "2"):
            showUserInJson()
        elif (val == "3"):
            showUser()
        elif (val == "4"):
            delUser()
        elif (val == "5"):
            editUser()
        else:
            print("Choose menu options as 1 , 2 , 3 , 4 or 5 to proceed further")