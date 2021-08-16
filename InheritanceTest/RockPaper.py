import random
class Contestant:
    
    def __init__(self, humanName,compName):
        self.humanName=humanName
        self.compName=compName
       
class Human(Contestant):
    def __init__(self,humChoice):
        self.humChoice=humChoice
        self.value=0
        if self.humChoice.lower()=="rock":
            self.value=1
        elif self.humChoice.lower()=="paper":
            self.value=2
        elif self.humChoice.lower()=="scissors":
            self.value=3
        else:
            self.value=0
        Contestant.__init__(self,None,None)
class Computer(Contestant):
    def __init__(self,comChoice):
        self.comChoice=comChoice
        self.value=0
        if self.comChoice.lower()=="rock":
            self.value=1
        elif self.comChoice.lower()=="paper":
            self.value=2
        elif self.comChoice.lower()=="scissors":
            self.value=3
        else:
            self.value=0
            Contestant.__init__(self,None,None)
    # def getRandom(self):
    #     self.computer=random.randint(1,3)
    #     return self.computer

           
        
index=0       

humanScore=0 
computerScore=0      
print("Enter name of human")
humanName=input()
print("Enter the name of computer")
compName=input()
contestant=Contestant(humanName,compName)
while index<3:
    choice=random.randint(1,3)
    if choice ==1:
        comChoice='rock'
    if choice ==2:
        comChoice='paper'
    if choice ==3:
        comChoice='scissors'
    computer=Computer(comChoice)
    print(contestant.humanName+", enter your choice")
    humanChoice=input()
    human=Human(humanChoice)
    print(contestant.compName+" chooses "+computer.comChoice)
    if human.value==computer.value:
            continue
    elif human.value==1:
        if computer==2:
            humanScore=humanScore+1
        else:computerScore=computerScore+1
    elif human.value==2:
        if computer.value==3:
            continue
        else:humanScore=humanScore+1
    elif human.value==3:
        if computer.value==1:
            computerScore=computerScore+1
    print(contestant.humanName+": "+str(humanScore) +"  "+contestant.compName+" :"+str(computerScore))
    index=index+1

        
      
