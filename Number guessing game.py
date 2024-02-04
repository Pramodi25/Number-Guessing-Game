import random
import math

# Taking inputs
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

# Generating a random number between lower and upper
number = random.randint(lower, upper)

# Calculating the number of guesses based on the range
num_guesses = round(math.log(upper - lower + 1, 2))

# Initializing the number of guesses
guess_count = 0

# Creating a for loop to limit the number of guesses
for _ in range(num_guesses):
    guess_count += 1
    guess = int(input("Guess a number: "))

    # Checking if the guess is correct
    if guess == number:
        print(f"Congratulations! You guessed the number in {guess_count} tries!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

# If the user didn't guess the number within the given number of guesses
if guess_count > num_guesses:
    print(f"\nThe number was {number}")
    print("Better luck next time!")
