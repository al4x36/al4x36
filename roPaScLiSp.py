import random
score1 = score2 = 0
isPlaying = True
print("Let's play Rock, Paper, Scissors, Lizard, Spock!")
choices = ["rock", "paper", "scissors", "spock", "lizard"]
userChoice = input("Choose rock, paper, spock, lizard, or scissors: ").lower()
computerChoice = random.choice(choices)
while isPlaying:
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
        
    ask = input("Do you want to play again? (yes/no): ").lower()
    choices = ["rock", "paper", "scissors", "spock", "lizard"]
    userChoice = input("Choose rock, paper, spock, lizard, or scissors: ").lower()
    computerChoice = random.choice(choices)
    if ask != "yes":
        isPlaying = False

