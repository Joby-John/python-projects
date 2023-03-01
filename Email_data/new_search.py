#thought i should just create a new program withh all ive learned instead of editing the old one
names = list()
with open ('Email_data\mbox-short.txt') as file:
    file_contnt = file.read()
    #print(file_contnt)

#The splitlines() method is a built-in Python method that splits a string into a list of lines, based on the newline character ('\n').
for line in file_contnt.splitlines():
    #line = file_contnt.rstrip()
    if not line.startswith('From'):
        continue
    sender = line.split()
    mail = sender[1]
    mail_part = mail.split('@')
    
    names.append(mail_part[0])

    


count = {}
for name in names :
    count[name] = count.get(name,0)+1

print(count)
