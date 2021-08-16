import random;
def getDice():
    dice1=random.randint(1, 6)
    dice2=random.randint(1, 6)
    print("You rolled "+str(dice1)+" + "+str(dice2)+" ="+str(dice1+dice2))
    return dice1+dice2
dice=getDice()
if dice==7 or dice==11:
    print("You win");
    exit()
elif dice==2 or dice==3 or dice==12:
    print("You lose");
    exit();
else:
    point=dice
    print("Your point is "+str(point))
    dice=getDice()
    while dice!=7 and dice!=point:
        getDice()
        if dice==7:
            print("You lose")
            exit();
        elif dice==point :
            print("You win")
            exit()
    


