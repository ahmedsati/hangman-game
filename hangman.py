from asciiArt import stages
from wordList import word_list
import random

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6


display = []
for val in range(word_length):
    display += "_"

while not end_of_game:
    guessList = []
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, print the letter and let them know.

    #Check guessed letter
    
    if guess in display:
        print(f"You have already guessed {guess}")
        
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    
        
    if guess not in chosen_word:
        #If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")


    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
    
    attempts = ''
    for i in display:
        attempts+=' '
        attempts+=i
        
    print(f"Your attempt: {attempts}")
    
    