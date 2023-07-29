import random
import os

def balckjack():
    os.system('CLS')
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    your_cards = []
    pc_cards = []
    scores = [0, 0] #0th place for your score 1st for computers score
    comp_visibility = False

    your_cards = random.choices(cards, k = 2)
    pc_cards = random.choices(cards, k = 2)

    def start(your_cards, pc_cards): # starting two draw
        for c in range(0, 2):
            scores[0] += your_cards[c]
            scores[1] += pc_cards[c]
            comp_visibility = False

        print_func(your_cards, pc_cards, scores,comp_visibility)    
        return scores  

    def next(your_cards, pc_cards, scores):                       #all next moves 
        your_cards.append(random.choice(cards))
        print(f"Your cards:{your_cards}")
        scores[0] += your_cards[-1]
        comp_visibility = True
        print_func(your_cards, pc_cards, scores, comp_visibility)
        return scores

    def print_func(your_cards, pc_cards, scores, comp_visibility):
        print(f"Your cards : {your_cards}, Your Total Score : {scores[0]} ")
        if comp_visibility == False:
            print(f"Computers  cards is : {pc_cards[0]}")
        else:
            print(f"computers cards is: {pc_cards}")    


    #all function calling
    scores = start(your_cards, pc_cards)

    go_on = input("Type 'y' to get another card or 'n' to pass:- ").lower()
    if go_on == 'y':
        scores = next(your_cards, pc_cards, scores)
        if scores[0] < scores[1] or scores[0] > 21:
            print("YOU LOSE\n")
            if 'yes' == input("Do you wanna play again enter 'yes' or 'no':- "):
                balckjack()
        elif scores[0] == scores[1]:
            print("ITS A DRAW\n") 
            if 'yes' == input("Do you wanna play again enter 'yes' or 'no':- "):
                balckjack()
        else:
            print("YOU WIN\n") 
            if 'yes' == input("Do you wanna play again enter 'yes' or 'no':- "):
                balckjack()

    else:
        comp_visibility = True
        if scores[0] < scores[1]:
            print("YOU LOSE\n")
            print_func(your_cards, pc_cards, scores, comp_visibility)
            if 'yes' == input("Do you wanna play again enter 'yes' or 'no':- "):
                balckjack()
        elif scores[0] > scores[1]:
            print("YOU WIN\n")
            print_func(your_cards, pc_cards, scores, comp_visibility)
            if 'yes' == input("Do you wanna play again enter 'yes' or 'no':- "):
                balckjack()
        else:
            print("ITS A DRAW\n")
            print_func(your_cards, pc_cards, scores, comp_visibility)
            if 'yes' == input("Do you wanna play again enter 'yes' or 'no':- "):
                balckjack()                

start = input("Do you wanna play black jack type 'yes' or 'no'").lower()

if start == 'yes':
    balckjack()   

     





