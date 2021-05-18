"""
title - This program is Clinic Management system which keeps records a doctor's as well as patient's attributes .
author name - Aditya Kumar
creation time - ‎26 ‎February ‎2021, ‏‎23:28:05
modified time - ‎‎26 ‎February ‎2021, ‏‎23:41:34‏‎

"""

import doctor as d
import patient as p
import searchDoctor as sd
import appointment as ap
import logging


def main():
    print("Clinique Management System")
    ch = input("1. Enter 1 to add a doctor \n2. Enter 2 to see all avaiable doctors \n3. Search Doctors \n4. Get an appointment \nEnter your choice : ")

    if (ch =='1'):
        d.addDoctor()
    elif (ch == '2'):
        d.showDoctor()
    elif(ch == '3'):
        sd.keySearch()
    elif(ch == '4'):
        ap.appointDoctor()
    else:
        print("enter a proper choice :  \n")
        main()
    

if  __name__ == "__main__":
    main()
