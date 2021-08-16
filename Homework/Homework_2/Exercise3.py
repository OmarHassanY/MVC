import random;
def game():
    secretNumber = random.randint(1, 100)
    print('I am thinking of a number between 1 and 100.')
    print('Take a guess.')
    guess = int(input())
    if guess < secretNumber:
        print('Your guess is too low.')
        game();
    elif guess > secretNumber:
        print('Your guess is too high.')
        game();
    else:
        print('Good job! You guessed my number in ' + str(guessesTaken) + ' guesses!')
print(game())
