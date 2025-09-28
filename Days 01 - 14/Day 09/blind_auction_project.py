# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

auction = True
data = {"Name": [],
        "Bid_Amount": []}
print(data)

while auction:
    name = input("What is your name?")
    bid = int(input("How much would you like to bid?"))

    data["Name"].append(name)
    data["Bid_Amount"].append(bid)
    print(data)

    more_bids = input("Are there other bidders? Yes or No?")
    more_bids = more_bids.lower()
    if more_bids == 'no':
        auction = False
        highest_bid = max(data["Bid_Amount"])
        highest_bidder = max(data["Name"], key=data.get)
        print(f"The highest bid was {highest_bid} from {highest_bidder}")
    else:
        print("\n" * 20)
