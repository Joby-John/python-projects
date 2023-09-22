number = int(input("Enter a number to print n sequence :- "))
result = 0
lim = number+1
for i in range(1, lim):
    result += number**i
print(f"The result of operation is :- {result}")
