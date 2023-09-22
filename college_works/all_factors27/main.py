number = int(input("Enter number you want to find all factors:- "))
print("Factors are:-", end=" ")
for i in range(1, round(number / 2)):
    if number % i == 0:
        print(i, end=",")
print(number)
