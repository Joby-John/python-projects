import random
import hang                                  #the module that i made containing graphics and word list
import os                                    # to clear screen

word_list = hang.words                       #word_list feeds on words from hang
chosen_word = random.choice(word_list)       #chooses a random word from wordlist


print(hang.logo)                              #the logo
print("\n\n")

#initialising list and printing the dashes
display = []
for alph in chosen_word:
  display += "_"
print(display)  

#game loop
lives = 6                                     # max number of wrong attempts, 6 bc, only 6 hangman figures more will result in index err
end_of_game = False                           # just initialisation

while not end_of_game:

  guess = input("Guess a letter: ").lower()   #receives input
  os.system('CLS')                            #clearing screen

  if guess in display :                       #checks whether this letter(alrady correct was inserted already)
    print(f"You already tried letter '{guess}', try some other letter ") #placement of this is imp.    
  
  for count in range(len(chosen_word)):
    if chosen_word[count] == guess:
      display[count] = guess   
  print("".join(display))

  if guess not in chosen_word:                #keeps track of wrong attempts
    lives -= 1
    print(f"\nYou guessed {guess}, its not in the word. You just lost a life")
    print(hang.stages[lives])                 #prints the hangman graphics from the other module hang 
  
  # condition for ending games, either win or lose
  if "_" not in display:
    end_of_game = True
    print("You win!")                         #keeping track of blanks and winning
  if lives < 1:
    end_of_game = True
    print(f"You lose\nThe word was {chosen_word}")  

  