from black_jack.main import startjack as start_black
from hangman.hangman import start as start_hang
from R_P_S import start as start_rock
import sys
import os
game = 0

while game != 4:
    os.system('CLS')
    print("Welcome to Game Hub")
    print("Choices:")
    print("1. Blackjack\n2. Hangman\n3. Rock Paper scissors\n4. Quit")
    game = input("Enter the option you want to cntinue with:- ")

    if game == "1": start_black()
    elif game == "2": start_hang()
    elif game == "3": start_rock()
    elif game == "4": sys.exit()
    else: print("Enter a valid option")