def check_winner(player_name, player_roll, computer_name, computer_roll):
    if player_roll > computer_roll:
        return player_name
    elif computer_roll > player_roll:
        return computer_name
    else:
        return None
