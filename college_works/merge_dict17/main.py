dict_list = []
try:
    for i in range(0, 2):
        dict_list.append({})
        lim = int(input(f"how many elements you want to enter in dictionary {i + 1}:-"))
        for j in range(0, lim):
            key = input(f"Enter key no .{i + 1}:- ")
            value = input(f"Enter value of {key}:- ")
            data = {key: value}
            dict_list[i].update(data)
        print(f"Dictionary no.{i + 1}:- {dict_list[i]}")
    dict_list[0].update(dict_list[1])
    print(f"The merged dictionary:- {dict_list[0]}")
except ValueError as e:
    print(f"Error occurred :- {e}")
