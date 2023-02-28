# First program with lists
#2 programs to do the same thing while one uses list


# without list
total = 0
count = 0

while True:
    print("Enter the numbers(one at a time) to get the average, enter done after entering all the numbers")
    inp = input("Enter the first input: ")
    if inp == "done":
        break
    val = float(inp)
    total = total + val
    count = count + 1

try:
    print("Average: ", total/count)
except:
    print("Enter atleast one number!")
