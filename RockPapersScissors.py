import random
def rpsgame():
    choices = ["rock", "paper", "scissors"]
    picked = random.choice(choices)
    guess = input('Rock, paper or scissors: ').strip().lower()
    if guess == picked.strip().lower():
        print('Correct!')
    else:
     print('Incorrect')
     return rpsgame()

rpsgame()


