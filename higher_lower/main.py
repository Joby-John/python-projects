import graphics
import os
import game_data
import random
import time

data = game_data.data
score = 0
os.system('CLS')

def first_comp():
    """Getting first input"""
    comp_a = random.choice(data)
    print(f"Compare A: {comp_a['name']}, {comp_a['description']}, from {comp_a['country']}")
    return comp_a

def second_comp():
    """Getting second input"""
    comp_b = random.choice(data)
    print(f"Compare B: {comp_b['name']}, {comp_b['description']}, from {comp_b['country']}")
    return comp_b

def logic(first_comp, second_comp):
    """same as the name suggests"""
    if first_comp['follower_count'] > second_comp['follower_count']: right = 'a'
    elif second_comp['follower_count'] > first_comp['follower_count']: right = 'b'
    else: right = "equal"

    choice = input("\nWho has more followers A/B:- ")
    if choice == right :
        print("You are right!")
        global score # because the score is defined globally else it'll get rest in every iteration
        score += 1
    else :
        print(f"Sorry that's wrong, your total score :{score}")
        return 0    

while True:
    print(graphics.logo)
    comp_a = first_comp()
    print(graphics.vs)
    comp_b = second_comp()
    cont = logic(comp_a, comp_b)
    if cont == 0:
        time.sleep(5) 
        break
    else: 
        time.sleep(3)
        os.system('CLS')           

    

