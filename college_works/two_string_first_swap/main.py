strs = []

for i in range(0, 2):
    strs.append(input(f"Enter {i + 1} string:- "))

temp = strs[0][:1]
strs[0] = strs[1][:1]+strs[0][1:]
strs[1] = temp + strs[1][1:]

print(" ".join(strs))
