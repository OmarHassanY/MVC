import os
print("Enter the name of the file")
test=input()
filePath=test
if os.path.exists(filePath):
    with open(filePath) as file:
        for i in range(5):
            line = file.__next__()
            print(line,end='') 
else:
    print("File does not exist")



