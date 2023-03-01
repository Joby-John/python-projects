#fhand = open('Email_data\mbox-short.txt') # old way 
names = list()
with open('Email_data\mbox-short.txt', 'r') as fhand: # new way which i just learned, both are same but using with automatically closes the file
#whole = fhand.read()


    for line in fhand:
        line = line.rstrip()

        if not line.startswith ('From'):
            continue
        sender = line.split()
        #print(sender[1])      # prints the entire mail adress
        mail = sender[1] # store the mail adress to mail
        mparts = mail.split('@') # split mail address and stores in mparts
        print(mparts[0]) # prints out name from mail address, which is in index 0

        names.append(mparts[0]) # includes all the name to a single list
print(names)


# experimental section sneak peak on dictionary

# Count the occurrences of each name using a dictionary
counts = {}
for name in names:
    counts[name] = counts.get(name, 0) + 1

# Print the histogram of names and counts
for name, count in counts.items():
    print(name + ' - ' + str(count))
    #fhand.close()
