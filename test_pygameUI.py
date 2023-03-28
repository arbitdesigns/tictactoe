
import pygame
from ui import PygameUI
import player as pl


# define a function to wrap the UI calls in event loop
def event_loop(func,  *args, **kwargs):
    ui = PygameUI()
    ui.display_board(board)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        res = func(*args, **kwargs)
    return res

   

ui = PygameUI()

# Tests that display_board method displays an empty board correctly
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
event_loop(ui.display_board, board)

# Tests that display_board method displays a Full board correctly
board = ['X', 'O', 'X', 'O', 'X', 'O', 'O', 'X', 'O']
event_loop(ui.display_board, board)

# Tests that display_board method displays a Partial board correctly
board = ['X', 'O', ' ', 'O', ' ', ' ', 'O', 'X', 'O']
event_loop(ui.display_board, board)

# Test proper handling when player not defined
player = None
try:
    event_loop(ui.display_turn, player)
except:
    print("Test Pass")

player = None
try:
    event_loop(ui.display_winner, player)
except:
    print("Test Pass")

# Test standard cases
player = pl.HumanPlayer('X', 'Saurabh')
event_loop(ui.display_turn, player)
event_loop(ui.display_winner, player)
event_loop(ui.display_tie)


# Tests that get_move method waits for mouse click input.
ui = PygameUI()
board = ['X', 'O', ' ', 'O', ' ', 'O', ' ', 'X', ' ']
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    ui.display_board(board)
    print(ui.get_move(board))