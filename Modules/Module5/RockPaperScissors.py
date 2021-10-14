import random
def main():
    print("Welcome to Rock, Paper, Scissors: The Game!!!")
    RPS = ["Rock", "Paper", "Scissors"]
    play_again = "y"

    while play_again == "y":
        playerChoice = input("Lets play. Chooese one: Rock, Paper or Scissors. \n")
        computerChoice = random.choice(RPS)

        print(f"Computer selected: {computerChoice}")
        print(f"Player selected: {playerChoice}")

        if(playerChoice == computerChoice):
            print("You tied :/ ")
        elif(playerChoice == "Rock" and computerChoice == "Paper"):
            print("Paper covers Rock. You lose :( ")
        elif(playerChoice == "Rock" and computerChoice == "Scissors"):
            print("Rock smashes Scissors. You Win :) ")
        elif(playerChoice == "Paper" and computerChoice == "Scissors"):
            print("Scissors shred Paper. You Lose :( ")
        elif(playerChoice == "Paper" and computerChoice == "Rock"):
            print("Paper covers Rock. You Win :) ")
        elif(playerChoice == "Scissors" and computerChoice == "Rock"):
            print("Rock smashes Scissors. You Lose :( ")
        elif(playerChoice == "Scissors" and computerChoice == "Paper"):
            print("Scissors shred Papers. You Win :) ")
        else:
            print("something isn't right. Maybe try again")
        play_again = input("Play again? Enter 'y' for yes or 'n' for no ")
    print("Game Over.")
main()