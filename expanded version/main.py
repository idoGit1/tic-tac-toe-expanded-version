import pygame
import sys
from const import *
from game import Game

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Tic Tac Toe- Expended version')
        self.game = Game()
        self.game.build_big_board()

    def mainloop(self):
        game = self.game
        game.show_background(self.screen)
        while True:
            if game.check_set_big_win():
                game.print_win(self.screen)
            if game.check_tie():
                game.print_tie(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and not game.check_set_big_win() and not game.check_tie():
                    clicked_x = event.pos[0] // SMALL_SQ
                    clicked_y = event.pos[1] // SMALL_SQ
                    # Checking if square is free & legal
                    square = (clicked_x // 3, clicked_y // 3, clicked_x - 3 * (clicked_x // 3),
                              clicked_y - 3 * (clicked_y // 3))
                    if game.legal_square == (-1, -1):
                        print('first move: ')
                    if game.is_empty(square) and (game.is_legal(square) or game.legal_square == (-1, -1)):
                        # Placing sign
                        # print(square)
                        game.squares[square[0]][square[1]].grid[square[2]][square[3]] = 1 if game.turn == 'X' else 2

                        # Checking if there is a "little" win
                        game.show_board(self.screen)
                        if game.check_small_win((clicked_x // 3, clicked_y // 3)):
                            game.set_print_small_win(self.screen, (clicked_x // 3, clicked_y // 3), game.turn)

                        # Checking win tie
                        if game.check_set_big_win():
                            game.print_win(self.screen)
                        if game.check_tie():
                            game.print_tie(self.screen)
                        # Saving the next legal square
                        game.legal_square = (square[2], square[3]) if game.big_board[square[2]][square[3]] == -300 else (-1, -1)
                        game.set_next_turn()

                    if game.check_set_big_win():
                        game.print_win(self.screen)
                    if game.check_tie():
                        game.print_tie(self.screen)

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


main = Main()
main.mainloop()