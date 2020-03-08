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

print_panel()