import os
import graphics
import time

print(graphics.logo)

bid_list = {}
while True:
    name_entry = input("Please enter your name :- ")
    if name_entry in bid_list:   #to prevent others from modifying previously entered dictionary value
        print("fraudulent duplicate entry detected and terminated, \n screen will be reactivated in 5s")
        time.sleep(5) #used to freeze screen for 5seconds
        print("The program continues now")
        time.sleep(1)
        continue
        
    amount = input("Please enter the bid amount:- ")
    bid_list[name_entry] = int(amount) # this line stores amount in key name_entry variable which keeps changing in each iteration
    more = input("Is there more persons, Type 'yes' if yes else type 'no' :- " ).lower()
    if more == "no":
        os.system('CLS')
        break    
    os.system('CLS')
    print(graphics.logo)

def bid_finder(bidlist):
    highest = 0
    for name in bidlist:
        if bid_list[name] > highest:
            highest = bidlist[name]
            high_bidder = name

    print(f"Highest bidder {high_bidder}, with a bid of {highest}$")    

bid_finder(bid_list)        