# Hangman Project
import random
from hangman_words import word_list
from hangman_art import stages, logo2, logo3

word_to_guess = random.choice(word_list)
len_word_to_guess = len(word_to_guess)
lives = 6
displays = []

for _ in range(len_word_to_guess):
    displays += '_'

print(logo3)
print("\nTo win, guess the word before the person is hung.\n")

while True:
    print(f"Word to guess: {''.join(displays)}")
    guess_word = input("Guess a letter: ")

    if guess_word in word_to_guess:
        for i in range(len_word_to_guess):
            if word_to_guess[i] == guess_word:
                displays[i] = guess_word
        print(f"{''.join(displays)}")
        print(stages[lives])

        if ''.join(displays) == word_to_guess:
            print(logo2)
            break
    else:
        lives -= 1
        print(f"You guessed {guess_word}, that's not in the word. You lose a life.")
        print(stages[lives])

        if lives == 0:
            print(f"***********************IT WAS gazebo! YOU LOSE**********************")
            break
    print(f"****************************{lives}/6 LIVES LEFT****************************")


