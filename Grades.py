




userInput = input("how many grades make up gpa? \n")
numGrades = int(userInput)
sum = 0.0
anotherOne = False
nextStudent = "e"
nextStudent = input("Continue to the next student? (y/n) \n")
if nextStudent == "y":
    anotherOne = True
elif nextStudent == "n":
    anotherOne = False
else:
    print("please enter lower case y or n only")
   
while anotherOne == True:
    for i in range(1, numGrades):
        gradeString = input("Enter grade \n")
        grade = float(gradeString)
        sum = sum + grade
averageGPA = sum/numGrades
print(averageGrade)
