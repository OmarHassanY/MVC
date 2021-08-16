import random;
def getDice():
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    print("You rolled "+str(dice1)+" + "+str(dice2)+" ="+str(dice1+dice2))
    return dice1+dice2
dice=getDice()
print (str(dice))
