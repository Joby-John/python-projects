split_list = [chara for chara in input("Enter a string:-")]
char_freq = {}
for letter in split_list:
    if letter != " ":
        count = split_list.count(letter)
        char_freq.update({letter: count})# when another value comes for same key it just gets replaced so dont worry on repetition
print(char_freq)
