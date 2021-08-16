import os
import random
if os.path.exists('my_random.txt'):
    with open('my_random.txt') as file:
        sum=0
        counter=0
        while True:
            try:
                line = int(file.__next__())
                sum=sum+line
                counter=counter+1
            except StopIteration:
                break 
else:
    print("File does not exist")
print('Total: '+str(format(sum,',')))
print(str(counter)+" numbers were read from the file")