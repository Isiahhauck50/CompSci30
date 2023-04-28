#=========================
#Isiah Hauck
#Libraries Summative
#Comp Sci 30
#=========================

# Modules
from time import sleep
import random
from dice_game import dice, game

# Set up the game
player_name = input("Enter your name: ")
computer_name = "Computer"
player_score = 0
computer_score = 0
round_num = 1

print(f"Welcome to the dice game, {player_name}!")
print("You will be playing against the computer.")
sleep(2)

# Play the game for 3 rounds
while round_num <= 3:
    print(f"\nRound {round_num}:")

    # Roll the dice for the player and computer
    player_roll = dice.roll_dice()
    computer_roll = dice.roll_dice()

    print(f"{player_name} rolled a {player_roll}!")
    print(f"{computer_name} rolled a {computer_roll}!")

    # Check who wins the round and update the score
    round_winner = game.check_winner(player_name, player_roll, computer_name, computer_roll)
    if round_winner == player_name:
        player_score += 1
        print(f"{player_name} wins the round!")
    elif round_winner == computer_name:
        computer_score += 1
        print(f"{computer_name} wins the round!")
    else:
        print("The round is a tie!")

    round_num += 1
    sleep(2)
    
# Determine the final winner of the game
if player_score > computer_score:
    print(f"\nCongratulations, {player_name}! You won the game!")
elif computer_score > player_score:
    print(f"\nSorry, {player_name}. The computer won the game.")
else:
    print("\nThe game is a tie!")

sleep(2)

print(f"\nFinal scores:\n{player_name}: {player_score}\n{computer_name}: {computer_score}")
