from abc import ABC, abstractmethod

class UI(ABC):

    @abstractmethod
    def display_board(self, board):
        pass

    @abstractmethod
    def display_turn(self, player):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass

    @abstractmethod
    def display_tie(self):
        pass

    @abstractmethod
    def get_move(self, board):
        # The function MUST return only a valid Move
        pass



class TerminalUI(UI):
    
    def display_board(self, board):
        print('''
        {} | {} | {}
        ---------
        {} | {} | {}
        ---------
        {} | {} | {}
        '''.format(*board))
    
    def display_turn(self, player):
        if player == None:
            raise Exception("Player not initialised")
        print("It's {}'s turn".format(player.name))
    
    def display_winner(self, player):
        if player == None:
            raise Exception("Player not initialised")
        print("{} wins!".format(player.name))
    
    def display_tie(self):
        print("It's a tie!")

    def get_move(self, board):
        while True:
            move = input("Enter your move (0-8): ")
            if move.isdigit() and int(move) in range(9) and board[int(move)] == ' ':
                return int(move)
            else:
                print("Invalid move. Please enter a number between 0-8 and make sure the space is empty.")




import pygame

class PygameUI(UI):
    def __init__(self):
        self.width = 600
        self.top_margin = 100
        self.height = 600+self.top_margin

        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Tic Tac Toe")

    def display_board(self, board):
        self.screen.fill((255, 255, 255)) # fill screen with white color

        # draw board lines
        pygame.draw.line(self.screen, (0, 0, 0), (200, self.top_margin), (200, 600+self.top_margin), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (400, self.top_margin), (400, 600+self.top_margin), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.top_margin), (600, self.top_margin), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 200 + self.top_margin), (600, 200+self.top_margin), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, 400 + self.top_margin), (600, 400+self.top_margin), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (0, self.height-4), (600, self.height-4), 5)

        # draw X's and O's on board
        for i, marker in enumerate(board):
            if marker == 'X':
                pygame.draw.line(self.screen, (255, 0, 0), 
                                 (i % 3 * 200 + 50,  i // 3 * 200 + 50 + self.top_margin), 
                                 (i % 3 * 200 + 150, i // 3 * 200 + 150 + self.top_margin), 
                                 10)
                pygame.draw.line(self.screen, (255, 0, 0), 
                                 (i % 3 * 200 + 150, i // 3 * 200 + 50 + self.top_margin), 
                                 (i % 3 * 200 + 50,  i // 3 * 200 + 150 + self.top_margin), 
                                 10)
            elif marker == 'O':
                pygame.draw.circle(self.screen, (0, 0, 255), 
                                   (i % 3 * 200 + 100, i // 3 * 200 + 100 + self.top_margin), 
                                   75, 10)

        pygame.display.update()

    def display(self, text):
        font = pygame.font.Font(None, 72)
        text_surface = font.render(text, True, (0, 0, 0))
        self.screen.blit(text_surface, (self.width // 2 - text_surface.get_width() // 2, 10))
        pygame.display.update()        

    def display_turn(self, player):
        if player == None:
            raise Exception("Player not initialised")
        text = f"{player.name}'s turn"
        self.display(text)

    def display_winner(self, player):
        if player == None:
            raise Exception("Player not initialised")
        text = f"{player.name} wins!"
        self.display(text)

    def display_tie(self):
        text = "It's a tie!"
        self.display(text)

    def get_move(self, board):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    if pos[1] < 100:
                        continue
                    row = (pos[1] - 100) // 200
                    col = pos[0] // 200
                    move = row * 3 + col

                    if board[int(move)] == ' ':
                        return move

