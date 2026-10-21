import random

while True:
    secret_number = random.randint(1, 50)
    print("Guess the Number!\n")
    guess = int(input(""))

    if guess < secret_number:
        print("Too Low! Try again.")
        continue
    elif guess > secret_number:
        print("Too High! Try again.")
        continue
    else:
        print("Congratulations! You guessed the number.")
    break

    