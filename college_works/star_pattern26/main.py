max_row = int(input("Enter the patterns maximum width :- "))


def restart(start, end, direction):
    for i in range(start, end, direction):
        print(i * "*")
        if i == max_row:
            restart(start=end, end=0, direction=-1)


if "yes" == input("do you want to do with recursion yes/ no:- ").lower():
    restart(start=1, end=max_row + 1, direction=1)
else:
    direction = 1
    i = 1
    end = max_row
    while i >= 1:
        for j in range(0, i):
            print("*", end="")
        print("")
        if i == max_row:
            direction = -1
        i += direction
