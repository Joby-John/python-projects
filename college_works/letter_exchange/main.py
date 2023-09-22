# get a string from an input string where all occurances of first character is replaced with $ except first charcater

sentence = input("Enter any sentence:- ")
converted = ""
first = sentence[0]
converted += first
for i in sentence[1:]:
    if i == first:
        converted += '$'
    else:
        converted += i
print(converted)
