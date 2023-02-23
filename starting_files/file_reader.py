name = input('Enter the file name: ')
try:
    fhand = open(name)
except:
    print('file not found: ', name)
    quit() # quits the program


count = 1
for lines in fhand:
    print(lines)