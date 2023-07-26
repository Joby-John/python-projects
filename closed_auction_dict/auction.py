import os
import graphics

print(graphics.logo)

bid_list = {}
while True:
    name_entry = input("Please enter your name :- ")
    amount = input("Please enter the bid amount:- ")
    bid_list[name_entry] = int(amount)
    more = input("Is there more persons, Type 'yes' if yes else type 'no' :- " ).lower()
    if more == "no":
        os.system('CLS')
        break    
    os.system('CLS')

def bid_finder(bidlist):
    highest = 0
    for name in bidlist:
        if bid_list[name] > highest:
            highest = bidlist[name]
            high_bidder = name

    print(f"Highest bidder {high_bidder}, with a bid of {highest}$")    

bid_finder(bid_list)        