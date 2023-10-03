import random
import time


print("Welcome to GTN!")
game_over = False
time.sleep(2)

secret_num = random.randint(1,100)
while not game_over:
    user_guess = int(input("Guess a number! "))
    if user_guess > secret_num:
        print("Your guess is too high! go lower...")
    elif user_guess < secret_num:
        print("Your guess is too low! go higher...")
    elif user_guess == secret_num:
        print(f"Your guess is right! you win! the number is {secret_num}")
        game_over = True
