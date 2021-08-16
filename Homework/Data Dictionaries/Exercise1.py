import random
cards = {'King of Diamonds':10,'Queen of Diamonds':10,'Jack of Diamonds':10,'10 of Diamonds':10,'9 of Diamonds':9,'8 of Diamonds':8,'Ace':1,'5 of spades':5,'4 of spades':4,'6 of spades':6,'7 of Clubs':7,'8 of clubs':8,'3 of clubs':3}
def main():
    print('How many cards should I deal?')
    answer = input()
    create_cards(answer)
def create_cards(answer):
    i=0
    total=0
    deck =list(cards.items())
    while i<int(answer):
        random.shuffle(deck)
        print(deck[0][0])
        total=total+deck[0][1]
        del deck[0]
        i=i+1
    deal_cards(total)
def deal_cards(total):
    print("Value of this hand "+str(total))
main()





