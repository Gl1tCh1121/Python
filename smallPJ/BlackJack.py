import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

y_n =  input("Do you want to play a game of Blackjack? Type 'y' or 'n':  ").lower()

def game_over():  

    yes_no = input("Do you want to play a game of Blackjack again?? Type 'y' or 'n':  ").lower()
    if yes_no == "y": 
        return False
    else: 
        print("GoodBye") 
        return True   
    

def score(pc_hand, user_hand):
    print(f"Your final hand: {user_hand}, final score: {sum(user_hand)}")
    print(f"Pc final hand: {pc_hand}, final score: {sum(pc_hand)}")

  
def win_lose(pc_hand, user_hand):             
    if sum(user_hand) > 21:
        score(pc_hand, user_hand)
        print("You went over. You lose")
    elif sum(pc_hand) > 21:
        score(pc_hand, user_hand)
        print("Pc went over. You won")
    else:
        print(f"Your score: {user_hand}, final score: {sum(user_hand)}")
        print(f"Pc score: {pc_hand[0]}")
    return 0   

        
def logic(pc_hand, user_hand):
    yes_no = ""
    while yes_no != "n" and sum(pc_hand) < 22 and sum(user_hand) < 22:
        yes_no =  input("Type 'y' to get another card, type 'n' to pass:  ").lower()
        if yes_no == "y":
            add_card(user_hand)
            win_lose(pc_hand, user_hand)
        elif yes_no == "n":
            if sum(user_hand) > sum(pc_hand):
                score(pc_hand, user_hand)
                print("You have more score. You won")      
            elif sum(pc_hand) > sum(user_hand):
                score(pc_hand, user_hand)
                print("Pc have more score. You lose")
            elif sum(user_hand) == sum(pc_hand):
                score(pc_hand, user_hand)
                print("Both have same score. Draw")

def add_card(who):
    is11 = int(random.choice(cards))
    if is11 == 11:
        if sum(who)+11 < 22:
           who.append(is11)
        else:
            who.append(1)
    else:
        who.append(is11)


def whitejack():
    print("""
****************************************************
*                                                  *
*     ♠ ♣ ♦ ♥  Let's Play Blackjack! ♥ ♦ ♣ ♠       *
*                                                  *
****************************************************
            .------.            .------.
            |A_  _ |            |A_  _ |
            |( \/ )|            |( \/ )|
            | \  / |            | \  / |
            |  \/ A|            |  \/ A|
            `------'            `------'
            
""")
    pc_hand = []
    user_hand = []
    for _ in range(2):
        add_card(pc_hand)
        add_card(user_hand)

    while sum(pc_hand) < 16: 
         add_card(pc_hand)

    print(f"Your cards:{user_hand}, current score {sum(user_hand)}")
    print(f"Computer's first card: {pc_hand[0]}")
        
    logic(pc_hand, user_hand)  

whitejack()

while not game_over():
    whitejack()
