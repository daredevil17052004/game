import random
targetNumber = random.randint(0,10)
print(targetNumber)
max_attempts = 5
user_guess = 0

while max_attempts>0:
    guess = int(input('Enter your Guess: '))

    if guess == targetNumber:
        print("Congratulations. You have guessed the right number.")
        break
    else:
        max_attempts -= 1
        if max_attempts == 0:
            print("Sorry, you have used all your guesses. Thanks for playing.")
        else:
            if guess < targetNumber:
                print("Guess Higher")
                print('Attempts Left:',max_attempts)
            else:
                print("Guess Lower")
                print('Attempts Left:',max_attempts)
