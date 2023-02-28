fhand = open('D:\projects\python-projects\Email_data\mbox-short.txt')
#whole = fhand.read()

for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    sender = line.split()
    print(sender[1])

