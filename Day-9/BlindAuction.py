import art
import os

print("Welcome to the Blind Auction Program")
print(art.logo)
bids_dictionary = {}
bid_Finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""

  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bid_Finished:
    name = input("What is your name? ")
    price = int(input("What amount would you like to bid?: $"))
    bids_dictionary[name] = price

    check_bidder = input("Would you like to continue? Type 'yes' or 'no': ")
    if check_bidder.lower() == "no":
        bid_Finished = True
        find_highest_bidder(bids_dictionary)
