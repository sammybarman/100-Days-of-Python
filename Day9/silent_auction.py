# create a program to silumalte a silent auction.
'''
Silent Auction - No one knows each other's bids.
The bidder with the highest bid wins.
The program should ask for the bidder's name and the bid.
Keep asking until the user types 'done'.
At the end of the auction, the program should tell the highest bidder.
'''

import os
bidders = {}
while True:
    print("Welcome to the Silent Auction")
    name = input("What is your name?: ")
    bid = input("What is your bid?: $")
    bidders[name] = bid
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    if other_bidders == "no":
        print("The auction is over.")
        os.system("clear")
        break
    elif other_bidders == "yes":
        os.system("clear")
        continue
    else:
        print("Please type 'yes' or 'no'.")
        continue

highest_bid = max(bidders)
print(f"The highest bidder is {highest_bid} with a bid of ${bidders[highest_bid]}.")

