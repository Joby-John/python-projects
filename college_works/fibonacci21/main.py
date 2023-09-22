try:
    lim = int(input("Enter the number of elements you want fibonacci series:- "))
    if lim > 0:
        fib = [0, 1]
        for i in range(2, lim + 1):
            next_num = fib[-1] + fib[-2]
            fib.append(next_num)
        print(fib)
    elif lim == 0:
        print([0])
    else:
        print("Fibonacci for negative numbers are not defined")
except ValueError as e:
    print(e)
