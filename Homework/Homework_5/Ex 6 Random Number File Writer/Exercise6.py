import os
import random
print("Enter the name of the file to which results should be written")
doc=input()
print("Enter the number of random numbers to be wriitten to the file")
number=input()

if os.path.exists(doc):
    with open(doc,'w') as file:
        for i in range(int(number)):
            file.write(str(random.randint(1,500)))
            file.write('\n')  
else:
    print("File does not exist")