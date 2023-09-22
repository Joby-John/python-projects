try:
    num = int(input("Enter the number you want factorial for:- "))
    if num >= 0:
        factorial = 1
        for i in range(1, num + 1):
            factorial *= i

        print(f"Factorial of {num} :- {factorial}")
    else:
        print("Factorial not defined for negative numbers")

except ValueError as e:
    print(e)
