"""
Create a hangman game that will do the following:
1. Generate a random word
2. Print a line for every letter of the word like _ _ _ _ _ _
3. Ask user to guess a letter
4. Tell user the letter is incorrect or if correct add the letter to the lines _ _ _ a _ _
5. At the end if the head, body, two arms and two legs are created then tell the player they lost
Your game will add a character below every time the user guesses wrong
   +---+
   0   |
  /|\  |
  / \  |
       |
=========
"""
'''
# Step 1


#import random
word_list = ["aardvark", "baboon", "camel"]

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = random.choice(word_list)

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input('Guess a letter in the word.\n').lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word, use a for loop.
# check FOR and IN part of this link https://developers.google.com/edu/python/lists#for-and-in

for letter in chosen_word:
    if letter == guess:
        print('right')
    else:
        print('wrong')
'''
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
chosen_word_length = len(chosen_word)

# Testing code
print(f'Chosen word is {chosen_word}.')

# TODO-1PART2: - Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
guess = input('Guess a letter in the word.\n').lower()
display = []
for letter in range(chosen_word_length):
    display.append('_')
print(display)


# TODO-2PART2: - Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
for position in range(chosen_word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter
print(display)

# TODO-3PART2: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.