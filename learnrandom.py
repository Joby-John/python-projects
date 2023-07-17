#learning random module, btw learned never to name your file the same name as of the module itll cause ann error
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")

num = len(names)
payer = random.randint(0, num)
print(f"{names[payer]} is going to buy the meal today!")