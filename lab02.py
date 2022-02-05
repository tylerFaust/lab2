########################################################################
##
## CS 101 Lab
## Program #2
## Tyler Faust
## tefqhg@umsystem.edu
##
## PROBLEM : grades need calculating
##
## ALGORITHM : 
##      1. get user to input a name
##      2. get user to input a number for each type of grade
##      2.1. fix input if it was not between 0 and 100 inclusive.
##      3. print the weighted grade
##      4. print a goodbye message and exit
## 
## ERROR HANDLING:
##      
##
## OTHER COMMENTS:
##      
##
########################################################################

if __name__ == "__main__":
    print("Welcome to the LAB grade calculator")
    name = input("\nEnter name: ")

    labGrade = int(input("\nEnter labs grade: "))
    if labGrade < 0:
        labGrade = 0
        print("The value entered should be greater than 0. It has been changed to 0.")
    elif labGrade > 100:
        labGrade = 100
        print("The value entered should be less than 100. It has been changed to 100.")

    examGrade = int(input("\nEnter exams grade: "))
    if examGrade < 0:
        examGrade = 0
        print("The value entered should be greater than 0. It has been changed to 0.")
    elif examGrade > 100:
        examGrade = 100
        print("The value entered should be less than 100. It has been changed to 100.")

    attendanceGrade = int(input("\nEnter attendance grade: "))
    if attendanceGrade < 0:
        attendanceGrade = 0
        print("The value entered should be greater than 0. It has been changed to 0.")
    elif attendanceGrade > 100:
        attendanceGrade = 100
        print("The value entered should be less than 100. It has been changed to 100.")

    letterGrade = ""

    weightedGrade = (labGrade * .7) + (examGrade * .2) + (attendanceGrade * .1)

    if weightedGrade >= 90:
        letterGrade = "A"
    elif weightedGrade >= 80:
        letterGrade = "B"
    elif weightedGrade >= 70:
        letterGrade = "C"
    elif weightedGrade >= 60:
        letterGrade = "D"
    else:
        letterGrade = "F"

    print("\n{} has a letter grade of {}".format(name, letterGrade))
    print("\nThanks for using this lab grade calculator")