print ("Build a simple age checker: Ask the user for their age and tell them if they are eligible for certain 
services")

#Ask for user input for age
age = int(input("How old are you?"))
#Check if user is eligible for a particular service
if age >= 20:
    print("You are allowed to stay up until midnight")
elif age >=15:
    print("Go to bed before midnight")
else:
    print("Go to bed now, kid!")
  
