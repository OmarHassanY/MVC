import random
def main():
    number=str(random.randint(1000,9999))
    numberList = []
    print("For debugging only "+str(number))
    print(" ")
    print("Welcome to Trees and Stumps! ")

    answer=[]
    guesses=1
    while True:
        
        print("Enter a 4 digit number ")
        digits=input()
        print(" ")
        if(len(digits)!=4 ):
            print("4 digits only! Try again.")
            continue
        for i in range(len(number)):
            answer.append(digits[i])
            numberList.append(number[i])
        
        treeCount=0
        stumpCount=0
        for i in range(len(answer)):
            if(answer[i]!=number[i]):
                continue
            if(answer[i] in number and answer[i]==number[i]) :
                treeCount=treeCount+1
                answer[i]='x'
                numberList[i]='y'
        for i in range(len(answer)):
            if(answer[i] in number):
                stumpCount=stumpCount+1
            else:
                continue    
       

        def playAgain():
            print("Play again? (y or n) ")
            choice=input()
            lowerChoice=choice.lower()
            if(lowerChoice=="y" or lowerChoice=="yes"):
                main()
            elif(lowerChoice=="n" or lowerChoice=="no"):
                print(" ")
          
            else:
                playAgain()
        if(treeCount==4 and stumpCount==0):
            print("You win! You guessed the number "+number+" in "+str(guesses)+" tries") 
            print(" ")
            playAgain()
            break

        else:  
            print("Tree = "+str(treeCount)+"   Stump= "+str(stumpCount))
            print("You have made "+str(guesses)+" guesses")
            print(" ")
            

        guesses=guesses+1
        answer.clear()
        numberList.clear()
        
main()
