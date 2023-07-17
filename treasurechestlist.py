row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = int(input("Where do you want to put the treasure? "))

# could be do like this

# horizontal = int(position/10)
# vertical = int(position%10)
# map[vertical-1][horizontal-1] = 'X'

      #OR
pos = []
pos.append(int(position/10))
pos.append(int(position%10))
map[pos[1]-1][pos[0]-1] = 'X'



print(f"{row1}\n{row2}\n{row3}")

