import random

# Stores wins for the player and computer
player_wins = 0
cpu_wins = 0


def player_option():
    """
    Provides input for the player to enter their play option and then checks if
    the entered input key is valid and then return the choice of the player
    """
    player_choice = input("Choose Rock, Paper, or Scissors: ")
    if player_choice in ["Rock", "rock", "r", "R"]:
        player_choice = "r"
    elif player_choice in ["Paper", "paper", "p", "P"]:
        player_choice = "p"
    elif player_choice in ["Scissors", "scissors", "s", "S"]:
        player_choice = "p"
    else:
        print("Invalid input, try using r = Rock, p = Paper, s = Scissors")
        player_option()
    return player_choice

player_option()


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

cpu_option()