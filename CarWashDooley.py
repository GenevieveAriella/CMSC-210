############################################
#Meredith Dooley
#Project 3: Car Wash
#Calculates cost of customer dependign on the services they select
#6-22-21
#############################################
#prompt user input for if they are a valued customer and create valuedCustomer variable
print("is this a valued customer, type 1 for YES, 0 for NO")
valuedCustomer = input()

#prompt user input for the type of carwash they want
print("is this a super or basic car wash, type 2 for super, 1 for basic")
carWashType = input()

#prompt user input for car waxing
print("do you want a car wax, type 1 for yes, 0 for no")
carWax = input()
#initializing cost variable
totalCost = 0
#if they are a valued customer then this code block will run
if valuedCustomer == '1':
    #if super car wash
    if carWashType == '2':
        #if they request a car wax
        if carWax == '1':
            totalCost = 40
        #if they request no car wash
        elif carWax == '0':
            totalCost = 30
        #if they dont input 0 or 1
        else:
            print("bad value for car Wax")
    #if basic car wash
    elif carWashType == '1':
        #car wax requested
        if carWax == '1':
            totalCost = 30
        #car wax not requested
        elif carWax == '0':
            totalCost =20
        #if they dont input 0 or 1
        else:
            print("bad value for carwax.")
    #if they dont input 2 or 1
    else:
        print("bar value for carWashType")
#same code block inside except different total cost. This code block is for non-valued customers
elif valuedCustomer == '0':
    if carWashType == '2':
        if carWax == '1':
            totalCost = 45
        elif carWax == '0':
            totalCost =35
        else:
            print("bad value for car Wax")
    elif carWashType == '1':
        if carWax == '1':
            totalCost = 35
        elif carWax == '0':
            totalCost =25
        else:
            print("bad value for carwax.")
    else:
        print("bar value for carWashType")
#if you did not input 0 or 1 for valuedCustomer prompt
else:
    print("bad value for valuedCustomer")
#total cost was cast to string and appended to string
print("The cost is $" + str(totalCost))

    
