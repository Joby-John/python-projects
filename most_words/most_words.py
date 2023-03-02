print("There are two files, 'clowns.txt' and words.txt")
inp = input("Enter a file name : ") 
with open(inp) as file:
    print(file) 