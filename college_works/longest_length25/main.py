words = input("Enter a list of word of which you want to find characters separated by ,:- ").split(",")
biggest = words[0].strip(" ")
len_list = []
for word in words:
    word = word.strip(" ")
    len_list.append(len(word))
    if len(biggest) < len(word):
        biggest = word
if len_list.count(len(biggest)) > 1:
    bigs = [word for word in words if len(word.strip(" ")) == len(biggest)]
    print(f"some words entered are of equal length they are:-{bigs} with {len(biggest)} letters")
else:
    print(f"The biggest word is:- {biggest} with {len(biggest)} characters")
