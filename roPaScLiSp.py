import random

choices = ["rock", "paper", "scissors", "spock", "lizard"]
userChoice = input("Choose rock, paper, spock, lizard, or scissors: ").lower()
computerChoice = random.choice(choices)

if userChoice in choices:
    if userChoice == computerChoice:
        print("It's a tie!")
    elif (
        (userChoice == "rock" and computerChoice == "scissors")
        or (userChoice == "paper" and computerChoice == "rock")
        or (userChoice == "scissors" and computerChoice == "paper")
        or (userChoice == "lizard" and computerChoice == "spock")
        or (userChoice == "rock" and computerChoice == "lizard")
        or (userChoice == "scissors" and computerChoice == "lizard")
        or (userChoice == "spock" and computerChoice == "scissors")


    ):
        print("You win! fatality! flawless victory!")
    else:
        print("Computer wins! flawless victory!")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")
