def adder():
    nums = [int(num) for num in input("Enter numbers to add separated by commas:-").split(",")]
    result = 0
    print(nums)
    for num in nums:
        result += num
    print(f"Sum = {result}")


def perfect_sq():
    lim = int(input("Enter the limit between 1000 and 9999:-"))
    even_list = []
    p_sq = {}
    for i in range(1000, lim):
        temp = i
        for pos in range(0, 5):
            if (temp % 10) % 2 == 0:
                temp = temp // 10
                if pos == 0:
                    even_list.append(i)
            else:
                continue
    for even in range(30, 99):
        if even ** 2 in even_list:
            pair = {even: even ** 2}
            p_sq.update(pair)
            continue
    print(p_sq)


def pyramid():
    rows = int(input("Enter rows for your pyramid:- "))
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print(i * j, end=" ")
        print("")


choice = int(input("Enter your choice \n1- sum of list \n2 - even squares\n3 - number pyramid\n:-"))

match choice:
    case 1:
        adder()
    case 2:
        perfect_sq()
    case 3:
        pyramid()
    case _:
        print("Enter a valid choice")
