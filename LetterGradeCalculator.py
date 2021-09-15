############################################
#Meredith Dooley
#Project 5: GPA Calculator
#calculated letter grade from gpa input
#7-6-21
##########################################
#defines main method
def main():
    #prompts for user input and stores in variable
    userInput = input("Enter a grade of -999 to quit: \n")
    #casts to float
    possibleGrade = float(userInput)
    #checks boolean as condition for while loop
    if possibleGrade == -999:
        stayOrGo = False
    else:
        stayOrGo = True
    #boolean true is condition for while loop
    while stayOrGo:
        #prints the letter grade
        print("The grade for a GPA is "+ str(float(possibleGrade)) + " is " + str(gradeCalculator(possibleGrade)))
        #repeats user prompt so there is not an infinite loop
        userInput = input("Enter a grade of -999 to quit: \n")
        possibleGrade = float(userInput)
        if possibleGrade == -999:
            stayOrGo = False
        else:
            stayOrGo = True
    #after kicked out of while loop, prints goodbye
    print("Thank you for using Letter Grade Calc! Goodbye!")
#defines grade calculator
def gradeCalculator(num):
    #initializes grade variable
    grade = "nothing"
    #if elif clauses to change letter grade variable depending on possibleGrade
    if(num >= 90.0):
        grade = "A"
    elif(num >=80.0):
        grade = "B"
    elif(num >= 70.0):
        grade = "C"
    elif(num >= 60.0):
        grade = "D"
    elif(num >= 0.0):
        grade = "F"
    #tells user they entered value which none of conditions match i.e. negative
    else:
        print("number or value entered is nonsensical")
    #when this method is called, it will output this
    return grade
#main method called
main()      
    
        
    
