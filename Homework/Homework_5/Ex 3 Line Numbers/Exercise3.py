import os
print("Enter the name of the file")
test=input()
if os.path.exists(test):
    with open(test) as file:
        counter=1
        while True:
            try:
                line = file.__next__()
                print(str(counter)+": "+line,end='')
                counter=counter+1
            except StopIteration:
                break
else:
    print("File does not exist")