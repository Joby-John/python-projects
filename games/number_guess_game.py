import random
import os
import time

def game():
    while True:
        os.system('CLS')
        print("Welcome to Number Guessing Game!")
        num = random.randint(1,100)
        print("I'm thinking of a number between 1 to 100")
        level = input("Enter the difficulty of the game \n type hard or easy or any other key to quit:- ").lower()
        if level == 'hard': level = 5
        elif level =='easy': level = 10
        else:
            print("Game ends in 3s")
            sleep = 4
            while(sleep != 1):
                time.sleep(1)
                print(sleep -1)
                sleep -= 1
            return

        while (level != 0):
            guess = int(input("Enter your guess:- "))
            if guess > num: print("Too high")
            elif guess < num: print("Too low") 
            else: 
                print("You won! You guessed it correct")
                time.sleep(3)
                break
            level -= 1
            print(f"You have {level} chances left")
        if guess == num: 
            os.system('CLS')
            print(f"Yes the number is {guess},You won with {level-1} chance left! congrats")
        else: 
            os.system('CLS')
            print(f"Sorry You lose\nMy guess was :{num}")


        if "no" == input("Do you want to play again yes / no:- ").lower(): break
       