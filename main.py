#imports
from ASCII_art import logo
from functions import is_winner

#program variables
auction_bids = {}
additional_bidders = False

while additional_bidders != True:
    print(logo)
    name = input("Please enter your name: ")
    amount = int(input("Please enter your bid amount: $"))
    auction_bids[name] = amount
    bid_continue = input("Are there any additional bidders? Type 'yes' or 'no'. ")
    if bid_continue == "no":
        additional_bidders = True
        is_winner(auction_bids)        
    elif bid_continue == "yes":
        print("\033c", end='')  # used to clear the console for the next bid
    