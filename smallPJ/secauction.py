import os 
print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-'''---------'' '-'
                          )"""""""(
                         /_________\|
                       .-------------.
                      /_______________}

""")

def add_bidder():
    bidders = {}
    highest_bidder = "someone"
    highest_bidder_bid = 0
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    
    if bid > highest_bidder_bid:
        highest_bidder = name
        highest_bidder_bid = bid
    
    def finishing():
        yer_no = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    
        if yer_no == "yes":
            os.system('cls')  
            add_bidder()
        
        else:
            print(f"The winner is {highest_bidder} with a bid of ${highest_bidder_bid}")

    finishing()        
    
add_bidder()