import time
import random

print("Welcome to Hangman!")
time.sleep(2)

word_list = ["red", "white", "black", "blue", "purple", "orange"]

secret_word = random.choice(word_list)
display_word = []
for letter in secret_word:
    display_word += "_"
print(display_word)

game_over = False
tries = 0

while not game_over:
    user_guess = input("Guess the first letter of the word! ").lower()
    for index in range(len(secret_word)):
        letter = secret_word[index]
        if user_guess == letter:
            display_word[index] = letter
    if user_guess not in display_word:
        tries += 1
        tries_left = 5 - tries
        print(f"you have {tries_left} attempts!")
        if tries >= 5:
            print("You lose!")
            game_over = True
    print(display_word)
    if "_" not in display_word:
        print("You win!")
        game_over = True
