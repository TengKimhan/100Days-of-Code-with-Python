from os import system
from art import logo

def find_highest_bidder(bidders):
    highest_bid = 0
    winner = {}
    for name, bid in bidders.items():
        if bid > highest_bid:
            highest_bid = bid
            winner = {name: bid}

    return winner

def start_page():
    print(logo)
    print("Welcome to the secret auction program.")

start_page()
bidders = {}
winner = {}

while(True):  
    name = input("What is your name?: ")
    bid = float(input("What is your bid?: $"))
    bidders[name] = bid
    winner = find_highest_bidder(bidders)
    
    check_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    if check_bidders == "yes":
        system("clear")
    elif check_bidders == "no":
        print("Auction ended.")
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")
        continue

for name, bid in winner.items():
    print(f"The winner is {name} with a bid of ${bid}.")
    