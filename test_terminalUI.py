

from ui import TerminalUI
import player as pl

   

ui = TerminalUI()

# Tests that display_board method displays an empty board correctly
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
ui.display_board(board)

# Tests that display_board method displays a Full board correctly
board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
ui.display_board(board)

# Tests that display_board method displays a Partial board correctly
board = ['X', 'O', ' ', 'O', ' ', ' ', 'O', 'X', 'O']
ui.display_board(board)

# Test proper handling when player not defined
player = None
try:
    ui.display_turn(player)
except:
    print("Test Pass")

player = None
try:
    ui.display_winner(player)
except:
    print("Test Pass")

# Test standard cases
player = pl.HumanPlayer('X', 'Saurabh')
ui.display_turn(player)
ui.display_winner(player)
ui.display_tie()


board = ['X', ' ', 'X', ' ', 'X', 'O', ' ', 'X', 'O']
ui.display_board(board)
print(ui.get_move(board))