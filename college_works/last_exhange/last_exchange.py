# create a string from the given string where the first and last characters exchanged

sentence = input("Enter any word or sentence:-")
list_made = [letter for letter in sentence]
temp = list_made[0]
list_made[0] = list_made[-1]
list_made[-1] = temp

sentence_new = "".join(list_made)
print(sentence_new)

