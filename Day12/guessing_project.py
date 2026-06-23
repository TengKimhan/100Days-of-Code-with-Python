import random

def guess(attempts, random_num):
    for att in range(attempts):
        print(f"You have {attempts - att} attempts remaining to guess the number.")
        num_guess = int(input("Make a guess: "))
        if num_guess < random_num:
            print("Too low.")
            print("Guess again.")
        elif num_guess > random_num:
            print("Too high.")
            print("Guess again.")
        else:
            print("You win!")
            return
    print("You lose!")
        
        
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
check = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
attempts = 10

if check == "hard":
    attempts = 5

guess(attempts, random.randint(1, 100))
    