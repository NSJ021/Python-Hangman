#imports
import random    
import hangman_art
import hangman_word
from replit import clear


end_game = False # bool for ending the game and while loop
chosen_word = random.choice(hangman_word.word_list)    #choosing a random word
word_length = len(chosen_word)    #word length
lives = 6    #setting player lives

#print(f"The solution is {chosen_word}")


#creating the dispaly list for blanks
display = []    
for _ in range(word_length):    #loop through chosen word and add "_"to display when there is a mathc
    display += "_"
print(f"{hangman_art.logo} \n")
print(f"{display} \n")


while not end_game:
    guess = input("Guess a letter? ").lower()    #creating the users guess

    clear()
    
    if guess in display:
        print(f"You've already guessed this {guess}")
    
    #loop for checking letter against the word
    for position in range(word_length):    
        char = chosen_word[position]
        
        if char == guess:
            display[position] = char
            
    if guess not in chosen_word:    #Removing a life with each abd guess
        print(f"You guessed {guess}, it is not in the word, you lose a life")
        lives -= 1
        if lives == 0:
            end_game = True
            print("You lose")

    #Joins elements of the lsit into a string
    
    print(f"{' '.join(display)}")

    #Checks if user has found all letters
    print(display)
    if "_" not in display:    
        end_game = True
        print("You Win")

    print(hangman_art.stages[lives])
