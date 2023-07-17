import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
scoreu = 0
scoreb = 0
while True:
    user = int(input("Welcome to rock papper scissors.\n To start playing select either of three\n 1- for rock, 2- for paper, 3- for scissors and 4- To quit the game :- "))
    if (user > 4 or user <1) :
        print("!! Sorry you exited the game, either you quitted or entered an invalid number!!")
        print(f"Your score is : you - {scoreu} to Bot- {scoreb} ")
        break
    comp = random.randint(1, 3)

    #the graphics
    #user
    if user == 1:
        print(f"User ={rock}")
    elif user == 2:
        print(f"User ={paper}")
    elif user == 3:
        print(f"User ={scissors}")    

    #pc
    if comp == 1:
        print(f"Bot ={rock}")
    elif comp == 2:
        print(f"Bot ={paper}")
    elif comp == 3:
        print(f"Bot ={scissors}")
                 
    #logic
    if (comp == user):
        print("its a draw")
    elif (user==1 and comp==3):
        print("you won the game")
        scoreu += 1
    elif(user == 2 and comp == 1):
        print("You won the game")
        scoreu += 1
    elif(user == 3 and comp == 2):
        print("You won the game!")
        scoreu += 1
    else:
        print("You lost the game!")
        scoreb += 1                
