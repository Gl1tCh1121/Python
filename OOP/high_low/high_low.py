from data import data
import art
import os 
import random

print(art.game)

def get_list(num,thing):
    if thing == 'name':
        return data[num]['name']
    elif thing == 'follower_count':
        return data[num]['follower_count']
    elif thing == 'description':
        return data[num]['description']
    else:
        return data[num]['country']
    
def compare():

    random_number = random.randint(0, 49)
    random_number2 = random.randint(0, 49)

    if random_number == random_number2:
        random_number2 = random.randint(0, 49)


    score = 0
    lose = False 

    def get_items():
            print(f"Compare A: {get_list(random_number,'name')} , a {get_list(random_number,'description')}, from {get_list(random_number,'country')}.")
            print(art.vs)
            print(f"Against B: {get_list(random_number2,'name')} , a {get_list(random_number2,'description')}, from {get_list(random_number2,'country')}.")
    get_items()

    while not lose:
        
        a_b = input("Who has more followers? Type 'A' or 'B':").lower()
        winner = ""

        if get_list(random_number, 'follower_count') > get_list(random_number2,'follower_count'):
            winner = "a"
        elif get_list(random_number, 'follower_count') < get_list(random_number2,'follower_count'):
            winner = "b"
        else:
            winner = "tie"

        if a_b == "a" and winner == "a" or winner == "tie":
            score += 1
            random_number = random_number2
            random_number2 = random.randint(0, 49)
            os.system('cls')
            print(art.game)
            print(f"Win! Current score: {score}.")
            get_items()
        elif a_b == "b" and winner == "b" or winner == "tie":
            score += 1
            random_number = random_number2
            random_number2 = random.randint(0, 49)
            os.system('cls')
            print(art.game)
            print(f"Win! Current score: {score}.")
            get_items()
        else:
            os.system('cls')
            print(art.game)
            print(f"Sorry, that's wrong. Final score: {score}")
            lose = True
            break

compare()

