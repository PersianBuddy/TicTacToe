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

# function that get a value from 1-9 (player choice) and update game panel based on that
def update_panel(player_choice, player_indicator):
    if  player_choice % 3 == 0:
        row = int(player_choice) -1
        col =2
    else:
        row = int(player_choice)
        col = 2 - (player_choice % 3)

    if  player_indicator == 'X':
        game_panel[row][col] = 1
    else:
        game_panel[row][col] =2

# variable that check if the game is ended
is_ended = False

# Create a variable that count number of moves
moves_count = 0

while is_ended == False or moves_count < 9:
    player_choice = input(f'Player {turn_indicator} please select an number in panel that is not being chased: ')
    #TODO: check the input to be an intiger
    #TODO: check the number to be between 1-9
    #TODO: check that position is not chosed before
    player_choice = int(player_choice)
    update_panel(player_choice,turn_indicator)
    print_panel()
    is_ended = check_winner()
    switch_turn()
    moves_count += 1

if  winner_indicator =='Draw':
    print('Good game for both player, It\'s finised as a draw')
else:
    print(f'Congratulation to player {winner_indicator} your the Winner :)')