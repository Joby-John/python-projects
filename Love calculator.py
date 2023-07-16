#Love calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1.lower() + name2.lower()
key1 = "true"
key2 = "love"
x = 0
val1 = 0
val2 = 0
for n in key1:
    x = name.count(n)
    val1 = val1+x
for n in key2:
    x = name.count(n)
    val2 = val2+x  

score = str(val1)+str(val2)
score = int(score)
if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")    
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")    