
import player
import ui as gui

class TicTacToeGame:

    def __init__(self, player1, player2, ui):
        self.board = [' '] * 9 # Initialize board with empty spaces
        self.players = [player1, player2]
        self.current_player = player1 # Starting player
        self.ui = ui

    def play(self):
        self.ui.display_board(self.board)
        while True:
            self.ui.display_turn(self.current_player)
            move = self.current_player.get_move(self.board, self.ui) #bad design. board should also validate if move is correct

            self.board[move] = self.current_player.get_marker()
            
            self.ui.display_board(self.board)
            if self.is_winner():
                self.ui.display_winner(self.current_player)
                break
            elif self.is_tie():
                self.ui.display_tie()
                break
            self.current_player = self.switch_player()

    def is_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8), # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8), # Columns
            (0, 4, 8), (2, 4, 6) # Diagonals
        ]
        for combo in winning_combinations:
            if (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]) and (self.board[combo[0]] != ' '):
                return True
        return False
    

    def is_tie(self):
        return all(marker != ' ' for marker in self.board)
    

    def switch_player(self):
        return self.players[1] if self.current_player == self.players[0] else self.players[0]
    

p1 = player.HumanPlayer('X', 'Saurabh')
p2 = player.RandomAI('O', 'Steve')
ui = gui.TerminalUI()
game = TicTacToeGame(p1, p2, ui)
game.play()