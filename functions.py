#function to determine the winner
def is_winner(auction_bids):
    winning_bid = 0
    for bidder in auction_bids:
        bid_amount = auction_bids[bidder]
        if bid_amount > winning_bid:
            winning_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, with a bid of ${winning_bid}")