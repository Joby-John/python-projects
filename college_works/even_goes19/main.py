try:
    num_list = input("Enter a list of random numbers separated by commas:-")
    num_list = [int(num) for num in num_list.split(",")]
    numbers = num_list[:]
    even_list = [num for num in num_list if num % 2 == 0]
    for even in even_list:
        num_list.remove(even)
    print(f"The numbers other than even in the list is :- {num_list}")
except ValueError as e:
    print(e)


def is_even(x):
    return x % 2 == 0


even_nos = list(filter(is_even, numbers))
print(f"Even numbers = {even_nos}")
