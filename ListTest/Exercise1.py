import random

print("Please enter how many numbers you would like to generate: ")
answer=input()
numbers = []
for x in range(int(answer)):
    numbers = numbers+[random.randint(0,9)]
print (numbers)

    
   

