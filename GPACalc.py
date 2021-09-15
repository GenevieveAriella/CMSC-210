###############################
#Meredith Dooley
#Project 4: GPA Calc
#outputs average GPA after asking user how many grades and what they were
#6-28-21
################################
#asks for user input on number of grades
userInput = input("how many grades make up gpa? \n")\
#casts to integer            
numGrades = int(userInput)
#initialize loop control boolean
anotherOne = True
#initializes user input variable inside loop
nextStudent = "e"
#start of while loop
while anotherOne == True:
    #initializes sum variable
    sum = 0.0
#while loop with boolean condition
    #for loop, with range 1 to numGrages (stops before reaches numGrades + 1)
    for i in range(1, numGrades + 1):
        #prompts user input for grades
        gradeString = input("Enter grade \n")
        #casts to float
        grade = float(gradeString)
        #increments sum
        sum = sum + grade
    #calculate and outputs average before loop ends
    averageGPA = sum/numGrades
    print(averageGPA)
    #prompts for user input on if more than one loop
    nextStudent = input("Continue to the next student? (y/n) \n")
    #checks if y or n, changes boolean accordingly
    if nextStudent == "y":
        anotherOne = True
    elif nextStudent == "n":
        anotherOne = False
    else:
        print("please enter lower case y or n only")
