fhand = open('Email_data\mbox-short.txt')
#whole = fhand.read()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    sender = line.split()
    #print(sender[1])      # prints the entire mail adress
    mail = sender[1] # store the mail adress to mail
    mparts = mail.split('@') # split mail address and stores in mparts
    print(mparts[0]) # prints out name from mail address, whic his in index 0

