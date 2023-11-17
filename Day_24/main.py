with open("text_file.txt", mode="w") as file1:
    file1.write("The new text")

with open("text_file.txt", mode="a") as file1:
    file1.write(", The appended text is here")

with open("text_file.txt") as file1:  # using with we doesn't have to remember to close the file, file1 is the var name
    contents = file1.read()
    print(contents)

with open("new_file.txt", mode="w") as file2:
    file2.write("The new text for new file, actually if i try to open a non existing file\n"
                "in write mode, it actually gets created and we can write in it as normal.")
