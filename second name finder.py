# second name finder 

name = input('Enter your full name: ')
name = name.strip() # to strip off accidental spaces either at front or back
count = name.count(" ")# To count number of occurances of the space
if count == 0:
    print("Please enter two or more words")
    print("Note: If you have entered your correct name, you might not have a second name")
else:
        
    start = name.find(" ")# to find the first occurance of space

    if count<2:
        sec_name = name[start+1 : ]
    else:
        end = name.find(" ", start+1)# to find the next occurance of space
        sec_name = name[start+1 : end]


    print('Your second name is: ', sec_name)