import math

num_list = []
try:
    for i in range(0, 2):
        num_list.append(int(input(f"Enter number {i + 1}:- ")))
    if "yes" == input("Find GCD using inbuilt function yes/no:- ").lower():
        print(f"GCD of {num_list[0]} and {num_list[1]} = {math.gcd(num_list[0], num_list[1])}")
    else:
        if num_list[0] < num_list[1]:
            limiter = num_list[0] / 2
        else:
            limiter = num_list[1] / 2
        gcd = 1
        for i in range(2, int(limiter)):
            if num_list[0] % i == 0 and num_list[1] % i == 0:
                gcd = i
        print(f"GCD of {num_list[0]} and {num_list[1]}:-{gcd} ,;) ")
except ValueError as e:
    print(e)

