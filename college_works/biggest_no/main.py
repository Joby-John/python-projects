numbers = input("Enter 3 numbers separated by space:- ").split(" ")
for n in range(0, len(numbers)):
    numbers[n] = int(numbers[n])
numbers = sorted(numbers, reverse=True)
print(f"The greatest = {numbers[0]}")
