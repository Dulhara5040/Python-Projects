import random
import string
from words import words

def get_valid_word(words_list):
    word = random.choice(words_list)
    while '-' in word or ' ' in word:
        word = random.choice(words_list)
    return word

def hangman():
    word = get_valid_word(words)
    word_letters = set(word.upper())  # Convert word to uppercase for case-insensitivity
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what user has guessed

    lives = 6

# getting user inputs

    while len(word_letters) > 0 and lives > 0:
        # letters used
        # '',join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives,' lives left and You have used these letters: ', ' '.join(used_letters))
        word_list = [letter if letter.upper() in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1 # takes away a life if wrong
                print('Letter is not in word.')

        elif user_letter in used_letters:
            print('You have already used that character. Please try again.')
        else:
            print('Invalid character. Please try again.')

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was ', word)
    else:
        print('Congratulations! You guessed the word:', word)

hangman()
