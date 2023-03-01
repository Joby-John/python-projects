#thought i should just create a new program withh all ive learned instead of editing the old one
names = list()

with open ('Email_data\mbox-short.txt') as file: # new thing
    file_contnt = file.read()

#The splitlines() method is a built-in Python method that splits a string into a list of lines, based on the newline character ('\n').
for line in file_contnt.splitlines():
    #line = file_contnt.rstrip() # dont need rstrip as splitlines automatically strips unwanted spaces
    if not line.startswith('From'):
        continue
    sender = line.split()
    mail = sender[1]
    mail_part = mail.split('@')
    names.append(mail_part[0]) # adding the names to list with append method

    
count = {}
for name in names :
    count[name] = count.get(name,0)+1 # get is used to retrieve value, in this case if there is no value it returns the default 0 and the line then adds 1 to it and assigns that to name

print(count.items())


for (key,value) in count.items(): #Using (key, value) or key, value syntaxes equivalent. because both unpacks tuple and assign value to key and value 
    print(key +":"+ str(value))
