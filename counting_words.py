inp = input("Enter Text: ") # dont enter large text, if you want to use file instead of input

words = inp.split()

count = {}
for word in words:
    count[word] = count.get(word, 0) + 1
print(count)    

for word,num in count.items():
    print(word +' - ' + str(num) )

for word in count:
    print(word + ':' + str(count[word])) # just as same as the upper loop