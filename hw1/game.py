"The game of tic-tac-toe."
from typing import Tuple


class TicTacGame:

    "The game of tic-tac-toe."

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.label = 'x'

    def validate_input(self) -> Tuple[int, int]:
        """Validate input from user.
        Should be in '{row} {column}' format, where row and column are integers in range [0, 2].

        :raises ValeError: if input is in wrong format
        :return: row and column indexes
        """
        row_col = input('Enter field coordinates: ')
        row, col = row_col.split()
        row, col = int(row), int(col)
        if row < 0 or row > 2:
            raise ValueError('row index less then 0 or more then 2')
        if col < 0 or col > 2:
            raise ValueError('column index less then 0 or more then 2')
        if self.board[row][col] != ' ':
            raise ValueError(f'field {row} {col} is occupied')
        return row, col

    def show_board(self):
        "Print current board state to stdout."
        print()
        for i, line in enumerate(self.board):
            print('|'.join(line))
            if i < 2:
                print('_' * 5)
        print()

    def check_winner(self) -> bool:
        """Check if current player has wone the game.

        :return: True if currrent player has won, False otherwise"""
        # check rows
        for i in range(3):
            winner = True
            for j in range(3):
                winner &= self.board[i][j] == self.label
            if winner:
                return True
        # check columns
        for j in range(3):
            winner = True
            for i in range(3):
                winner &= self.board[i][j] == self.label
            if winner:
                return True
        # check main diagonal
        winner = True
        for i in range(3):
            winner &= self.board[i][i] == self.label
        if winner:
            return True
        # check side diagonal
        winner = True
        for i in range(3):
            winner &= self.board[i][2 - i] == self.label
        return winner

    def start_game(self) -> str:
        """Start main loop.

        :return: label of the winner: 'x' or 'o'"""
        while True:
            self.show_board()
            try:
                row, col = self.validate_input()
            except ValueError as err:
                print()
                print(err)
                print()
                continue
            self.board[row][col] = self.label
            if self.check_winner():
                break
            self.label = 'x' if self.label == 'o' else 'o'
        self.show_board()
        print('Player', self.label, 'has won')
        return self.label


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
