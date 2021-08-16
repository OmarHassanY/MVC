import random
president = {'Alaska':'Juneau','Arizona':'Phoenix','California':'Sacramento','Colorado':'Denver','Deleware':'Dover','Georgia':'Atlanta','Idaho':'Boise','Kansas':'Topeka5'}
incorrect=0
correct=0
while True:
    data = list(president.items())
    random.shuffle(data)
    print("What is the captial of "+str(data[0][0])+"? (or enter 0 to quit)")
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
 
