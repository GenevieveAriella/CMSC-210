#Enter your name here after the colon:Maggie Dooley
#
#Project 6 - List and string methods
#
#Provide the missing code in the 10 empty lines below as specified
#in each code segment.
#Each line of code is worth 3 points for a total of 30 points for the project.
#
#DO NOT change anything else in this code!!!
#
#Code 1: Use the append method to add "Volkswagen" to the cars list:
cars = ["Ford", "Toyota", "Volvo","Mercedes"]
cars.append("Volkswagen")
print('Result 1: ',cars)
#
#Code 2: Use the insert method to add "Honda" as the second item in the cars list:
cars = ["Ford", "Toyota", "Volvo","Mercedes"]
cars.insert(1,"Honda")
print('Result 2: ',cars)
#
#Code 3: Use the remove method to remove "Volvo" from the cars list:
cars.remove("Volvo")
print('Result 3: ',cars)
#
#Code 4: Use the pop() method to remove the third element of the cars list:
cars = ["Ford", "Toyota", "Volvo","Mercedes"]
cars.pop(2)
print('Result 4: ',cars)
#Code 5: Use the sort() method to sort the elements of the list:
cars = ["Ford", "Toyota", "Volvo", "Mercedes"]
cars.sort()
print('Result 5: ',cars)
#
#PART B: STRING METHODS
#
#Code 6: Use the strip() method to remove the blank spaces
#at the beginning and the end of the mySpaceyString object and assign
#the result to the myString variable.
mySpaceyString='  odyssey'
myString=''
myString = mySpaceyString.strip()
print('Result 6:  Text after strip():'+ myString)
#
#Code 7: Use the upper() method to convert the value of the
#lowerCase object to upper case and assign the result to the
#variable upperCase.
lowerCase = 'high rise'
upperCase = ''
upperCase = lowerCase.upper()
print('Result 7:  Text after upper(): '+ upperCase)
#
#code 8: Use the count() method to count the number of times
#the word "love" appears in the myText string object
#and assign the result to the numTimes variable.
myText='I love you! I love you! I love you!'
numTimes = ''
numTimes = myText.count("love")
print('Result 8:  Word count - love:',numTimes)
#
#Code 9: Use the endswith() method to check if the string object myText
#ends with a period and assign the result this mmethod (a Boolean value)
#to the variable periodFound.
myText = "I often forget the period at the end of a sentence"
periodFound = ''
periodFound = myText.endswith(".")
print('Result 9:  Sentence ends with a period:',periodFound)
#
#Code 10: Use the find() method to locate the position of the word 'needle'
#in the myText object and assign this position to the needlePosition variable.
myText = "There is a needle in this haystack."
needlePosition = ''
needlePosition = myText.find("needle")
print('Result 10: The needle was found at position: ', needlePosition)
#End of the project
