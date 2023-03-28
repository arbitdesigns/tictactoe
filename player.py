from abc import ABC, abstractmethod

class Player(ABC):
    def __init__(self, marker, name):
        self.marker = marker
        self.name = name

    @abstractmethod
    def get_move(self, board, ui):
        pass

    def get_marker(self):
        return self.marker


class HumanPlayer(Player):
    def get_move(self, board, ui):
        return ui.get_move(board)


class RandomAI(Player):
    def get_move(self, board, ui=None):
        empty_spots = [i for i in range(9) if board[i] == ' ']
        import random
        return random.choice(empty_spots)
    


def test_player():
    board = ['X', 'O', ' ', 'O', ' ', 'O', ' ', 'X', ' ']
    hp = HumanPlayer('X', 'SM')
    hp.get_marker()
    import ui
    gui = ui.TerminalUI()
    print(hp.get_move(board, gui))

    ap = RandomAI('O', 'PM')
    ap.get_marker()
    print(ap.get_move(board))

if __name__ == '__main__':
    test_player()