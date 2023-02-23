name = input('Enter the file name: ')
try:
    fhand = open(name)
except:
    print('file not found: ', name)
    quit() # quits the program


count = 0
for lines in fhand:
    print(lines)
    count = count +1
print('Number of lines:', count)
fhand.seek(0) # sets the fhand pointer back to 0 ie, starting of the file else the next loop wont work

c = 0
for line in fhand:
    c = c+1
    if line.startswith('F'):
        print('Lines starting with F: ', line)
        print('line no:', c)

fhand.close() # releases the resource in fhand and saves changes made        