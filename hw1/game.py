"The game of tic-tac-toe."
from typing import Tuple


class TicTacGame:

    "The game of tic-tac-toe."

    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.label = 'x'

    def validate_input(self, user_input: str) -> Tuple[int, int]:
        """Validate input from user.
        Should be in '{row} {column}' format, where row and column are integers in range [0, 2].

        :param use_input: user input
        :raises ValeError: if input is in wrong format
        :return: row and column indexes
        """
        row, col = user_input.split()
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

    def check_winner_or_tie(self) -> str:
        """Check if current player has wone the game.

        :return: winner ('x' or 'o') or 'tie' or 'no'"""
        is_winner = False
        is_board_filled = True
        diag_flags = [True, True]
        for i in range(3):
            row_flag = True
            col_flag = True
            for j in range(3):
                is_board_filled &= self.board[i][j] != ' '
                row_flag &= self.board[i][j] == self.label
                col_flag &= self.board[j][i] == self.label
            is_winner |= row_flag or col_flag
            diag_flags[0] &= self.board[i][i] == self.label
            diag_flags[1] &= self.board[i][2 - i] == self.label
        is_winner |= diag_flags[0] or diag_flags[1]
        if is_winner:
            return self.label
        if is_board_filled:
            return 'tie'
        return 'no'

    def switch_player(self):
        "Switch current player."
        self.label = 'x' if self.label == 'o' else 'o'

    def start_game(self) -> str:
        """Start main loop.

        :return: label of the winner: 'x' or 'o'"""
        while True:
            self.show_board()
            user_input = input('Enter field coordinates: ')
            try:
                row, col = self.validate_input(user_input)
            except ValueError as err:
                print(f'\n{err}\n')
                continue
            self.board[row][col] = self.label
            result = self.check_winner_or_tie()
            if result != 'no':
                break
            self.switch_player()
        self.show_board()
        if result == 'tie':
            print('A tie')
        else:
            print('Player', result, 'has won')
        return result


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
