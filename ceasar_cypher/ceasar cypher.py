import os                                        #for clearing screen
import graphics                                  #for logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(graphics.logo)

while exit != 'exit':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def encrypt (text, shift, direction):
    encrypted = ""                               #empty string for storing output
    for letter in text:
      if letter not in alphabet :                # for charcaters that are not alphabets adds that character and skips the iteration.
        encrypted += letter
        continue
      pos = alphabet.index(letter)               # from here the actual stuff begins
      if direction == "encode" : pos += shift
      elif direction == "decode": pos += (-1*shift)    #good that i never stored modified shift in shift "(ie , like shift *= -1") itself else number would've changed sign every iteration.
      if pos > 25 or pos < -26: pos = pos%26     # there was a chance of out index error if someone entered large number so this  
      encrypted += alphabet[pos]                 # just filling the new letter to string
    
    if direction == "encode": 
      print(f"encoded :- {encrypted}")
    else:
      print(f"Decoded:- {encrypted}")    
  
   
  # tried all possible ways to put function call in if else check whether user inputed 
  # encode or decode else to prevent from running but its not working dont know why
  # if direction != "encode" or "decode": continue , this is the code i used but it cant distinguish b/w decode and encode an other strings. 
  encrypt(text, shift, direction)               # calling function

  exit = input("Enter 'exit' to quit the program, for continuing enter 'go on' :- ").lower()
  print("\n\n")
  os.system('CLS')