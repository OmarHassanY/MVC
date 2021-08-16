import random
president = {'Lincoln':'Kentucky','Truman':'Missouri','Hoover':'Iowa','Ford':'Nebraska','Grover':'New Jersey','Richard':'California','Jimmy':'Georgia'}
incorrect=0
correct=0
while True:
    data = list(president.items())
    random.shuffle(data)
    print("What is the birthplace of "+str(data[0][0])+"? (or enter 0 to quit)")
    answer = input()
    if(str(answer)==str(data[0][1])):
        print("That is correct")
        correct=correct+1
    elif(str(answer)==str(0)):
        break
    else:
        print("That is incorrect ")
        incorrect = incorrect+1
print("You had "+str(correct)+" correct responses and "+str(incorrect)+" incorrect responses")
   
        

