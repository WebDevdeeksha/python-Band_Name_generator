end_of_game = True
auction_data = {}

def auction(bidding_records):
    highest_bid = 0
    winner = ""
    for bidder in bidding_records:
        bidder_amount = bidding_records[bidder]
        if(bidder_amount > highest_bid):
            highest_bid = bidder_amount
            winner = bidder
    print(f"Auction is won by {winner} with ${highest_bid}")


while end_of_game:
    user = input("Enter your name: ")
    amount = int(input("Enter money: "))
    auction_data[user] = amount
    choice = input("Anyone else want to say type 'y' or 'n'. \n")
    if(choice=='n'):
        end_of_game = False
        print(auction_data)
        auction(auction_data)
