import math

num_list = []

for i in range(0, 2):
    num_list.append(int(input(f"Enter number {i+1}:- ")))
print(f"GCD of {num_list[0]} and {num_list[1]} = {math.gcd(num_list[0], num_list[1])}")
