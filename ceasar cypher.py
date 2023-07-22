alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while exit != 'exit':
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  def encrypt (text, shift):
    encrypted = ""
    for letter in text:
      pos = alphabet.index(letter)
      if direction == "encode" : pos += shift
      elif direction == "decode": pos += (-1*shift)  
      if pos > 25 or pos < -26: pos = pos%26  
      encrypted += alphabet[pos]
    print(f"encoded = {encrypted}")  
  
  encrypt(text, shift)
  
  exit = input("Enter 'exit' to quit the program, for continuing enter 'go on' :- ").lower()
  print("\n\n")