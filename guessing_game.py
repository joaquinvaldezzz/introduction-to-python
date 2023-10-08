import random

# Initialize a number randomizer
number_to_guess = random.randint(1, 100)

# Print a hint
print('Number to guess (hint):', number_to_guess)

while True:
    try:
        user_guess = int(input('Enter your guess: '))

        if user_guess < number_to_guess:
            print('Too low\n')
        elif user_guess > number_to_guess:
            print('Too high\n')
        else:
            print('Correct')
            break
    except ValueError:
        print('Invalid input. Please try again.\n')
