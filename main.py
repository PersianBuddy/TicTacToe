# Create a game panel
# 0 for not played location, 1 for player 'X' and 2 for 'O' player
game_panel = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# function to print game panel
def print_panel():
    game_panel_print = ""
    for i in range(0, 3):
        for j in range(0, 3):
            if game_panel[i][j] == 0:
                game_panel_print += " - "
            elif game_panel[i][j] == 1:
                game_panel_print += ' X '
            else:
                game_panel_print += ' O '
        game_panel_print += '\n'
    print(game_panel_print)


# create a turn indicator
# it's value can be either 'X' or 'O'
turn_indicator ='X'
# function that change turns
def switch_turn():
    global turn_indicator
    if  turn_indicator == 'X':
        turn_indicator = 'O'
    else:
        turn_indicator = 'O'


# Create winner indicator
# it's value can be 'X' or 'Y' or 'Draw'
winner_indicator = 'Draw'

# function to check if there is a winner at the end of each move
def check_winner():
    winner = 0
    global game_panel
    global winner_indicator
    if game_panel[0][0] != 0 and game_panel[0][0]==game_panel[0][1] == game_panel[0][2] :
        winner = game_panel[0][0]
    elif game_panel[1][0] != 0 and game_panel[1][0]==game_panel[1][1] == game_panel[1][2] :
        winner = game_panel[1][0]
    elif game_panel[2][0] != 0 and game_panel[2][0]==game_panel[2][1] == game_panel[2][2] :
        winner = game_panel[2][0]
    elif game_panel[0][0] != 0 and game_panel[0][0]==game_panel[1][0] == game_panel[2][0] :
        winner = game_panel[0][0]
    elif game_panel[0][1] != 0 and game_panel[0][1] == game_panel[1][1] == game_panel[2][1]:
       winner = game_panel[0][1]
    elif game_panel[0][2] != 0 and game_panel[0][2] == game_panel[1][2] == game_panel[2][2]:
        winner = game_panel[0][2]
    elif game_panel[1][1] != 0 and game_panel[1][1] == game_panel[0][0] == game_panel[2][2]:
        winner = game_panel[1][1]
    elif game_panel[1][1] != 0 and game_panel[1][1] == game_panel[0][2] == game_panel[2][0]:
        winner = game_panel[1][1]

    # Check the winner and return True if there is a winner
    if winner == 0 :
        return False
    elif winner == 1 :
        winner_indicator = 'X'
        return True
    else:
        winner_indicator = 'O'
        return True

check_winner()