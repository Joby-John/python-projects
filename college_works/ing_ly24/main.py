word = input("Enter any word:- ").lower()
if word[-3:] != "ing":
    word += "ing"
else:
    word += "ly"
print(f"The modified word is :- {word}")
