import random

# Set difficulty levels
level = input("Choose a difficulty level (Easy, Medium, Hard, Legendary): ")
if level == "easy":
   highest_value = 10
   lowest_value = 1
elif level == "medium":
   highest_value = 100
   lowest_value = 1
elif level == "hard":
    highest_value = 500
    lowest_value = 1
elif level == "legendary":
    highest_value = 1000
    lowest_value = 1
else:
    print("you did not choose  the right level,try again.")


random_number = random.randint(lowest_value, highest_value)
# Allow user to guess the number
num_guesses = 0
user_guess = 0
while user_guess != random_number:
    user_guess = int(input("Guess a number between {} and {}: ".format(lowest_value,highest_value)))
    num_guesses += 1

    if user_guess < random_number:
        print("guess lower!")
    elif _user_guess > random_number:
        print("guess higher!")
    else:
        print(f"great! You guessed the number correctly in {num_guesses} guesses.")
