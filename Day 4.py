#Create a simple countdown program

#Using a for loop for countdown from 10 to 1
print("Countdown using a for loop:")

count = 10

for count in range(10, 0, -1): #Start at 10, down to 1, decrement by 1
    print(count)

#Using a while loop for countdown from 10 to 1
print("Countdown using a while loop:")

count = 10
while count > 0:
    print(count) #print the current number
    count -= 1 #Decrease count by 1

print("end of loop") #Message after while loop countdown
