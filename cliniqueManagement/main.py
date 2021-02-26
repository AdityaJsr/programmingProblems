import doctor as d
import patient as p
import searchDoctor as sd

def main():
    print("Clinique Management System")
    ch = input("1. Enter 1 to add a doctor \n2. Enter 2 to see all avaiable doctors \n3. Search Doctors: \nEnter your choice : ")

    if (ch =='1'):
        d.addDoctor()
    elif (ch == '2'):
        d.showDoctor()
    elif(ch == '3'):
        sd.keySearch()
    

if  __name__ == "__main__":
    main()
