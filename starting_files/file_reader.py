name = input('Enter the file name: ')
try:
    fhand = open(name)
except:
    print('file not found: ', name)
    quit() # quits the program

whole = fhand.read()# reading the file as a whole 

count = 0
for lines in fhand: # reading line by line
    print(lines)
    count = count +1
print('Number of lines:', count)
fhand.seek(0) # sets the fhand pointer back to 0 ie, starting of the file else the next loop wont work

c = 0
for line in fhand: 
    c = c+1
    if line.startswith('F'): # searching for lines that starts with f
        print('Lines starting with F: ', line)
        print('line no:', c)
        # during the final iteration the fhand will be having the last index of the file

print("\n reading the file as a whole output : ", whole)    
print('Total characters: ', len(whole))    

fhand.close() # releases the resource in fhand and saves changes made        