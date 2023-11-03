from board import Board
from const import *
import pygame
class Game:
    # Regular functions:

    def __init__(self):
        self.turn = 'X'
        self.legal_square = (-1,-1)
        self.winner = ''

    def build_big_board(self):
        self.squares = [[Board(), Board(), Board()],
                        [Board(), Board(), Board()],
                        [Board(), Board(), Board()]]
        self.big_board = [[-300, -300, -300],
                          [-300, -300, -300],
                          [-300, -300, -300]]
    def is_empty(self, square):
        if (self.squares[square[0]][square[1]]).grid[square[2]][square[3]] == -100:
            return True
        return False
    def is_legal(self, square):
        if square[0] == self.legal_square[0] and square[1] == self.legal_square[1]:
            return True
        return False

    def set_next_turn(self):
        self.turn = 'X' if self.turn == 'O' else 'O'

    def check_small_win(self, square):
        tboard = self.squares[square[0]][square[1]].grid
        opt = ['X', 'O']
        for sign in opt:
            for i in [0, 1, 2]:
                if tboard[i][0] + tboard[i][1] + tboard[i][2] == 3:
           #         self.squares[square[0]][square[1]].value = 'X'
                    self.big_board[square[0]][square[1]] = 1
                    return True
                if tboard[0][i] + tboard[1][i] + tboard[2][i] == 3:
           #         self.squares[square[0]][square[1]].value = 'X'
                    self.big_board[square[0]][square[1]] = 1
                    return True

                if tboard[i][0] + tboard[i][1] + tboard[i][2] == 6:
           #         self.squares[square[0]][square[1]].value = 'O'
                    self.big_board[square[0]][square[1]] = 2
                    return True
                if tboard[0][i] + tboard[1][i] + tboard[2][i] == 6:
            #        self.squares[square[0]][square[1]].value = 'O'
                    self.big_board[square[0]][square[1]] = 2
                    return True
            if tboard[0][0] + tboard[1][1] + tboard[2][2] == 3:
           #    self.squares[square[0]][square[1]].value = 'X'
                self.big_board[square[0]][square[1]] = 1
                return True
            if tboard[0][2] + tboard[2][0] + tboard[1][1] == 3:
            #    self.squares[square[0]][square[1]].value = 'X'
                self.big_board[square[0]][square[1]] = 1
                return True

            if tboard[0][0] + tboard[1][1] + tboard[2][2] == 6:
            #    self.squares[square[0]][square[1]].value = 'O'
                self.big_board[square[0]][square[1]] = 2
                return True
            if tboard[0][2] + tboard[2][0] + tboard[1][1] == 6:
            #    self.squares[square[0]][square[1]].value = 'O'
                self.big_board[square[0]][square[1]] = 2
                return True
        return False
    def check_set_big_win(self):
        opt = ['X', 'O']
        for sign in opt:
            for i in [0, 1, 2]:
                if self.big_board[i][0] + self.big_board[i][1] + self.big_board[i][2] == 3:
                    self.winner = 'X'
                    return True
                if self.big_board[0][i] + self.big_board[1][i] + self.big_board[2][i] == 3:
                    self.winner = 'X'
                    return True

                if self.big_board[i][0] + self.big_board[i][1] + self.big_board[i][2] == 6:
                    self.winner = 'O'
                    return True
                if self.big_board[0][i] + self.big_board[1][i] + self.big_board[2][i] == 6:
                    self.winner = 'O'
                    return True
            if self.big_board[0][0] + self.big_board[1][1] + self.big_board[2][2] == 3:
                self.winner = 'X'
                return True
            if self.big_board[0][2] + self.big_board[2][0] + self.big_board[1][1] == 3:
                self.winner = 'X'
                return True

            if self.big_board[0][0] + self.big_board[1][1] + self.big_board[2][2] == 6:
                self.winner = 'O'
                return True
            if self.big_board[0][2] + self.big_board[2][0] + self.big_board[1][1] == 6:
                self.winner = 'O'
                return True
        return False

    def check_tie(self):
        for row in range(BIG_ROWS):
            for col in range(BIG_COLS):
                if self.big_board[row][col] == -300:
                    return False
        return True and self.winner == ''
    # Blit functions:

    def blit_move(self, surface, sign, row, col, type):
        mark = X_IMG if sign == 'X' else O_ING
        size = SMALL_SQ if type == 'Small' else BIG_SQ
        img = pygame.image.load(mark)
        img = pygame.transform.scale(img, (size, size))
        img_center = row * size + size // 2, col * size + size // 2
        img_rect = img.get_rect(center = img_center)
        surface.blit(img, img_rect)
        pygame.display.update()
    def show_board(self, surface):
        for row in range(BIG_ROWS):
            for col in range(BIG_COLS):
                tboard = self.squares[row][col]
                for row2 in range(BIG_ROWS):
                    for col2 in range(BIG_COLS):
                        if tboard.grid[row2][col2] != -100 and tboard.grid[row2][col2] != -87:
                            sign = 'X' if tboard.grid[row2][col2] == 1 else 'O'
                            self.blit_move(surface, sign, row * 3 + row2, col * 3 + col2, 'Small')
        for row in range(BIG_ROWS):
            for col in range(BIG_COLS):
                if self.big_board[row][col] != -300:
                    sign = 'X' if self.big_board[row][col] == 1 else 'O'
                    self.blit_move(surface, sign, row, col, 'Big')
    def show_background(self, surface):
        for row in range(BIG_ROWS * 3):
            for col in range(BIG_COLS * 3):
                color = (255, 255, 255) if (row + col) % 2 == 0 else (224, 224, 224)
                rect = (col * SMALL_SQ, row * SMALL_SQ, SMALL_SQ, SMALL_SQ)
                black = (0,0,0)

                pygame.draw.rect(surface, color, rect)
                if col % 3 == 0 and col != 0:
                    line = (col * SMALL_SQ, row, 5, HEIGHT)
                    pygame.draw.rect(surface, black, line)
                if row % 3 == 0 and row != 0:
                    line2 = (col, row * SMALL_SQ, WIDTH, 5)
                    pygame.draw.rect(surface, black, line2)
                pygame.display.update()

    def set_print_small_win(self, surface, square, sign):
        row = square[0]
        col = square[1]
        self.big_board[row][col] = 1 if sign == 'X' else 2
        # Setting all squares in big square illegal
        for i in range(BIG_ROWS):
            for j in range(BIG_COLS):
                self.squares[row][col].grid[i][j] = -87
        mark = X_IMG if sign == 'X' else O_ING
        img = pygame.image.load(mark)
        img = pygame.transform.scale(img, (BIG_SQ, BIG_SQ))
        img_center = row * BIG_SQ + BIG_SQ // 2, col * BIG_SQ + BIG_SQ // 2
        img_rect = img.get_rect(center=img_center)
        surface.blit(img, img_rect)
        pygame.display.update()
    def print_win(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render('Winner is ' + self.winner, True, 'Green')
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        surface.blit(text, text_rect)
        pygame.display.update()
    def print_tie(self, surface):
        font = pygame.font.Font('freesansbold.ttf', 100)
        text = font.render('TIE', True, 'Red')
        text_rect = text.get_rect()
        text_rect.center = (WIDTH // 2, HEIGHT // 2)
        surface.blit(text, text_rect)
        pygame.display.update()
