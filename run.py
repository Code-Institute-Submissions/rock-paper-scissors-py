import random

# Stores wins for the player and computer
player_wins = 0
cpu_wins = 0


def player_option():
    """
    Provides input for the player to enter their play option and then checks if
    the entered input key is valid and then return the choice of the player
    """
    player_choice = input("Choose Rock, Paper, or Scissors: (r/p/s)")
    if player_choice in ["Rock", "rock", "r", "R"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "s"
    else:
        print("Invalid input, try using r = Rock, p = Paper, s = Scissors")
        player_option()
    return player_choice


def cpu_option():
    """
    Randomly picks a number of 1 - 3 and then represet the numbers with valid input
    keys to let us know what the computer picked
    """
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        cpu_choice = "r"
    elif cpu_choice == 2:
        cpu_choice = "p"
    elif cpu_choice == 3:
        cpu_choice = "s"
    return cpu_choice


while True:
    print("")
    # Calls players option functions and stores the returned value in these variables
    player_choice = player_option()
    cpu_choice = cpu_option()
    print("")

    # Checks every valid winning condition to determine the winner
    if player_choice == "r":
        if cpu_choice == "r":
            print("You chose Rock and the computer chose Rock, you tie!")
        elif cpu_choice == "p":
            print("You chose Rock and the computer chose Paper, you lose!")
            cpu_wins += 1
        elif cpu_choice == "s":
            print("You chose Rock and the computer chose Scissors, you win!")
            player_wins += 1

    elif player_choice == "p":
        if cpu_choice == "r":
            print("You chose Paper and the computer chose Rock, you win!")
            player_wins += 1
        elif cpu_choice == "p":
            print("You chose Paper and the computer chose Paper, you tie!")
        elif cpu_choice == "s":
            print("You chose Paper and the computer chose Scissors, you lose!")
            cpu_wins += 1
            
    elif player_choice == "s":
        if cpu_choice == "r":
            print("You chose Scissors and the computer chose Rock, you lose!")
            cpu_wins += 1
        elif cpu_choice == "p":
            print("You chose Scissors and the computer chose Paper, you win!")
            player_wins += 1
        elif cpu_choice == "s":
            print("You chose Scissors and the computer chose Scissors, you tie!")
    
    # Prints the latest scores
    print("")
    print(f"Player wins: {player_wins}")
    print(f"Computer wins: {cpu_wins}")
    print("")

    # Checks if the player wants to continue playing another round
    player_choice = input("Do you want to play again? (y/n)")
    if player_choice in ["Yes", "yes", "y", "Y"]:
        pass
    elif player_choice in ["No", "no", "n", "N"]:
        break
    else:
        break