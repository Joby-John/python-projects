import random
import hang

word_list = hang.words #word_list feeds on words from hang
chosen_word = random.choice(word_list) #chooses a random word from wordlist

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#initialising list and printing the dashes
display = []
for alph in chosen_word:
  display += "_"
print(display)  

#game loop
lives = len(display) # max number of wrong attempts
end_of_game = False # just initialisation

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  
  for count in range(len(chosen_word)):
    if chosen_word[count] == guess:
      display[count] = guess   
  print("".join(display))

  if guess not in chosen_word: #keeps track of wrong attempts
    lives -= 1
    print(hang.stages[lives]) #prints the hangman graphics from other module hang 
  
  # condition for ending games, either win or lose
  if "_" not in display:
    end_of_game = True
    print("You win!") #keeping track of blanks and winning
  if lives < 1:
    end_of_game = True
    print(f"You lose\nThe word was {chosen_word}")  

  