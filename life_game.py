print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print("Welcome to the 'story life'")
op1 = input("you are in your teenage and you have met a good girl, who would you give priority God or the Girl? ")
if (op1.lower() == "girl"):
    print("You lost because the girl was God fearing, now you've lost both The God and girl")
elif op1.lower() == "god":
    print("you just levelled up, God blessed you \n Proverbs 16:3 – Commit your work to the Lord, and your plans will be established.")
    op2 = input("God now has put before you two choices either girl or career, what will you choose?")
    if op2.lower() == "girl":
        print("you lost, because she stayed with you for sometime but left you because your focus was her and not your life")
    elif op2.lower() == "career":
        print("Great, God did as he promised, he made you successful and made your goals come true")
        op3 =  input("God finally asked do you praise me in all that i have gave you? Yes or No")
        if op3.lower() == 'yes':
            print("You won!, God blessed you, he gave you the wife that he promised, blessed you with all riches and knowledge and discernment ")
        else:
            print("You lost")       
