import random
import os

def balckjack(): #entire program in this function bc i want to reset all variables when ever the game restarts
    os.system('CLS')
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    your_cards = []
    pc_cards = []
    scores = [0, 0] #0th place for your score 1st for computers score, stored scores in list inorder to return 2scores from each function
    comp_visibility = False # bc only using one print function and no need to show comp cards in firstt round

    your_cards = random.choices(cards, k = 2) #first draw
    pc_cards = random.choices(cards, k = 2) #first draw

    #first round
    def start(your_cards, pc_cards, comp_visibility):
        if not comp_visibility: # in first round comp visisbility is false
            for c in range(0, 2):
                scores[0] += your_cards[c]
                scores[1] += pc_cards[c]
            if 21 in scores: # game ends in 1st round itself bc of blackjack
                comp_visibility = True
                print("BLACK JACK")    
        print_func(your_cards, pc_cards, scores,comp_visibility) # passing to print function     

    #2nd round
    def next(your_cards, pc_cards, scores):         
        your_cards.append(random.choice(cards))
        print(f"Your cards:{your_cards}")
        scores[0] += your_cards[-1]
        comp_visibility = True  #bc its neccessary to show bc after this the game ends
        if scores[1] < 17:  # <17 rule if comp score is less 17 comp can pick another card
            pc_cards.append(random.choice(cards))
            scores[1] += pc_cards[-1] #adding the last picked card to score
        print_func(your_cards, pc_cards, scores, comp_visibility) #passing to print

    #printing and score evaluation
    def print_func(your_cards, pc_cards, scores, comp_visibility):
        print(f"Your cards : {your_cards}, Your Total Score : {scores[0]} ")
        if comp_visibility == False:
            print(f"Computers  cards is : {pc_cards[0]}") #displaying only first level
            go_on = input("Type 'y' to get another card or 'n' to pass:- ").lower() #more cards checker
            if go_on == 'y':
                next(your_cards, pc_cards, scores) # calling 2nd round
            else:
                comp_visibility = True #sets as true bc decided not to get other card and game needs to end
                print_func(your_cards, pc_cards,scores, comp_visibility) #recursion with only one change comp_visibility as true
        else:
            print(f"computers cards is: {pc_cards}")    #displaying all comp cards
        
        #all the score valuations
            if scores[0] < scores[1] or scores[0] > 21:
                print("YOU LOSE\n")
            elif scores[0] == scores[1]:
                print("ITS A DRAW\n") 
            else:
                print("YOU WIN\n")
            if 'yes' == input("DO YOU WANT TO PLAY AGAIN 'yes' or 'no':- ").lower():
                balckjack()     

    #starting the first round after this its all like chain reaction
    start(your_cards, pc_cards, comp_visibility)
                

play = input("Do you wanna play black jack type 'yes' or 'no':- ").lower()
if play == 'yes':
    balckjack()   

     





