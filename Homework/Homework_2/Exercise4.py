import random;
def game():
    computer=random.randint(1,3);
    print("Choose rock,paper or scissors");
    choice=input();
    if choice.lower()=="rock":
        player=1;
    elif choice.lower()=="paper":
        player=2;
    elif choice.lower()=="scissors":
        player=3;
    else:print("That is an Invalid choice");   
    if player==computer:
        game();
    elif player==1:
        if computer==2:
            print("You lose because Paper wraps rock");
        else:print("You win because Rock smashes scissors");
    elif player==2:
        if computer==3:
            print("You lose because Scissors cuts paper");
        else:print("You win Paper wraps rock");
    elif player==3:
        if computer==1:
            print("You lose because Rock smashes scissors");
            print("You win because Scissors cuts paper ")
print(game());
            
