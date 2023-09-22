try:
    num_list = input("Enter a list of random numbers separated by commas:-")
    num_list = [int(num) for num in num_list.split(",")]
    even_list = [num for num in num_list if num % 2 == 0]
    for even in even_list:
        num_list.remove(even)
    print(f"The numbers other than in the list is :- {num_list}")
except ValueError as e:
    print(e)
