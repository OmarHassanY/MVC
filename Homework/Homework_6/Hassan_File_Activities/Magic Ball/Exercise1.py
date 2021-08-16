import random
import os
if os.path.exists('responses.txt'):
    while True:
        print("Enter your question")
        answer=input()
        with open('responses.txt') as file:
            
            line=file.readlines()
            print(line.__getitem__(random.randint(0,9)))

            print("Do you want to ask another question? (y or n)")
            choice=input()
            if choice =='n':
                break
else: print('File does not exist')
    
