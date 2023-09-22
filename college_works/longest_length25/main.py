words = input("Enter a list of word of which you want to find characters separated by ,:- ").split(",")
biggest = words[0]
for word in words:
    if len(biggest) < len(word):
        biggest = word
print(f"The biggest word is:- {biggest} with {len(biggest)} characters")
