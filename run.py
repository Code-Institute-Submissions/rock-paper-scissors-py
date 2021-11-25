from random import randint

# Stores a list of game options
game_options = ["Rock", "Paper", "Scissors"]

# Assign a random option of the game_options list
cpu = game_options[randint(0,2)]

# Checks if the player is playing
player = False