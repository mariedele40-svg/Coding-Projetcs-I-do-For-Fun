import random

def play_game():
    choices = ["rock", "paper", "scissors"]

    print("Welcome to Rock, Paper, Scissors.")

    while True:
        print("Enter rock, paper, or scissors:\n")
        player_choice = input("\n").lower()

        if player_choice == "quit":
            print("Thank's for playing.")
            break
        if player_choice not in choices:
            print("Invalid output.")
            continue

        computer_choice = random.choice(choices)
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        if player_choice == computer_choice:
            print("It's a tie.")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
            (player_choice == "paper" and computer_choice == "rock") or \
            (player_choice == "scissors" and computer_choice == "paper"):
            print("You win.")
        else:
            print("Computer wins.\n")

if __name__ == "__main__":
    play_game()
            