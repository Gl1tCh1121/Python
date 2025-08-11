import random

print('''  
      
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|       
       
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.''')

easy_hard = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
random_number = random.randint(1, 100)

hard_or_easy = int(0)

if easy_hard == "easy":
    hard_or_easy = 10
else:
    hard_or_easy = 5

print(f"You have {hard_or_easy} attempts remaining to guess the number.")


def is_num():
    attempts = hard_or_easy
    for _ in range(0, hard_or_easy):
        guess = int(input("Make a guess: "))
        if guess == random_number:
            print(f"You got it! The answer was {random_number}.")
            break
        elif guess > random_number:
            attempts -= 1
            print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
            
        else:
            attempts -= 1
            print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")

        if attempts == 0:
            print(f"Number was {random_number}")

is_num()