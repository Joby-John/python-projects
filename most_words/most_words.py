print("There are two files, 'clown.txt' and words.txt")
words = list()
inp = input("Enter a file name : ")

try: # to avoid getting error for invalid file name
    with open(inp) as file:
            f_cont = file.read()

    for line in f_cont.splitlines(): # splitting the entire text to lines
        for word in line.split(): # splitting lines to words
                words.append(word) # storing those words as list

    count = {}
    for word in words:
        count[word] = count.get(word, 0)+1

    maximum = max(count, key = count.get)# max function to find the greatest value in dictionary

    print("most occuring word :  "+ maximum + ", " + str(count[maximum]) + " times")      
            

except:
     print("ERR! Enter a file that is present in the directory")        