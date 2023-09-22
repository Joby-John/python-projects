from prettytable import PrettyTable
import os
on = 1
while on == 1:
    zoo_register = {}
    table = PrettyTable()
    table_visibility = "yes"
    try:
        for i in range(0, int(input("How many items do you want to enter:-"))):
            animal = input("Enter the animal name:- ")
            number = int(input("Enter total number of animals in the zoo:-"))
            zoo_register.update({animal: number})
        numerical_sorted = dict(sorted(zoo_register.items(), key=lambda item: item[1]))  # sorts based on value ie in index 1
        print(f"Animal list in ascending order :- {numerical_sorted}")
        print(f"Animal list in descending order :- {dict(reversed(numerical_sorted.items()))}")
        if table_visibility == input("Do you want to view data in a table form yes/no:- ").lower():
            os.system("cls")
            table.add_column("ANIMALS", list(numerical_sorted))
            table.add_column("COUNT", list(numerical_sorted.values()))
            print(table)
        on = input("Enter 1 to go again:- ")
    except ValueError as e:
        print(f"error occurred ,err code:{e}")
        on = input("Enter 1 to try again:- ")
