# A much more complex cypher than ceasar cypher, just goes front and back consecutively
# like for odd front 1 step, for even back 1 step
import os                                        #for clearing screen
import graphics                                  #for logo
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print(graphics.logo())

while exit != 'exit':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
  if direction == "encode" or direction == "decode": 
    print("\n")
  else:continue  

  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def encrypt (text, shift, direction):
    encrypted = ""                               #empty string for storing output
    for letter in text:
      if letter not in alphabet :                # for charcaters that are not alphabets adds that character and skips the iteration.
        encrypted += letter
        continue
      
      pos = alphabet.index(letter)               # from here the actual stuff begins
      #encoding
      if direction == "encode" : 
        if len(encrypted)%2 == 0:
          pos += shift
        else:
          pos += (-1*shift)    #good that i never stored modified shift in shift "(ie , like shift *= -1") itself else number would've changed sign every iteration.
      #decoding
      elif direction =="decode":
        if len(encrypted)%2 == 0:
          pos += (-1*shift)
        else:
          pos += shift  

      if pos > 25 or pos < -26: pos = pos%26     # there was a chance of out index error if someone entered large number so this  
      encrypted += alphabet[pos]                 # just filling the new letter to string
    
    if direction == "encode": 
      print(f"encoded :- {encrypted}")
    else:
      print(f"Decoded:- {encrypted}")    
  
   
  #if direction == "encode" or direction == "decode": # the problem was what i did was direction == encode or decode, infact what needed was direction == encode or direction == decode  
  encrypt(text, shift, direction)               # calling function
  #else:
  #print("Enter a valid input") , found a much more efficient way just after input encode or decode 

  exit = input("Enter 'exit' to quit the program, for continuing enter 'go on' :- ").lower()
  print("\n\n")
  os.system('CLS')
print("GoodBye!")  