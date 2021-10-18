"Tests for tic-tac-toe game."
import sys
import unittest
import unittest.mock
from io import StringIO

from game import TicTacGame


class ValidateInputTest(unittest.TestCase):

    "Test case for TicTacGame.validate_input."

    def setUp(self):
        self.game = TicTacGame()
        self.valid_inputs = (
            ('1 1', (1, 1)),
            ('0 0', (0, 0)),
            ('2 2', (2, 2)),
            ('0 1', (0, 1)),
            ('0 2', (0, 2)),
            ('2 0', (2, 0)),
            ('1 2', (1, 2)),
        )
        self.invalid_inputs = (
            '',
            'aaa 1',
            '0, bbbb',
            'asdaf kfjgkfjgk',
            '-1 0',
            '0 100',
            '1, 2',
            '-20 -100',
            '0 1 2'
        )

    def test_valid_input(self):
        "Test TicTacGame.validate_input when user input is valid"
        for user_input, correct_result in self.valid_inputs:
            with unittest.mock.patch('builtins.input', return_value=user_input):
                result = self.game.validate_input()
                self.assertEqual(correct_result, result)

    def test_invalid_input(self):
        "Test TicTacGame.validate_input when user input is invalid"
        for user_input in self.invalid_inputs:
            with unittest.mock.patch('builtins.input', return_value=user_input):
                self.assertRaises(ValueError, self.game.validate_input)


class ShowBoardTest(unittest.TestCase):

    "Test case for TicTacGame.show_board."

    def setUp(self):
        self.game = TicTacGame()
        self.empty_board_out = (
            '',
            ' | | ',
            '_____',
            ' | | ',
            '_____',
            ' | | ',
            '',
            ''
        )
        self.empty_board_out = '\n'.join(self.empty_board_out)

    def test_empty_board_out(self):
        "Test correct output for empty board."
        captured_out = StringIO()
        sys.stdout = captured_out
        self.game.show_board()
        sys.stdout = sys.__stdout__
        self.assertEqual(self.empty_board_out, captured_out.getvalue())


class CheckWinnerTest(unittest.TestCase):

    "Test case for TicTacGame.chek_winner."

    def setUp(self):
        self.game = TicTacGame()

    def test_empty_board(self):
        "Test correct output for empty board."
        self.assertEqual(False, self.game.check_winner())


class StartgameTest(unittest.TestCase):

    "Test case for TicTacGame.start_game"

    def setUp(self):
        self.moves_for_games = (
            # winnning row
            (
                '1 1',
                '0 0',
                '2 2',
                '0 1',
                '0 2',
                '2 0',
                '1 2',
            ),
            # same as previous, but with duplicated inputs
            (
                '1 1',
                '0 0',
                '0 0',
                '2 2',
                '2 2',
                '2 2',
                '2 2',
                '2 2',
                '2 2',
                '0 1',
                '0 1',
                '0 1',
                '0 1',
                '0 1',
                '0 2',
                '2 0',
                '2 0',
                '2 0',
                '2 0',
                '1 2',
            ),
            # winning column
            (
                '0 0',
                '1 0',
                '0 1',
                '1 1',
                '2 0',
                '1 2',
            ),
            # winning main diagonal
            (
                '0 0',
                '0 1',
                '1 1',
                '0 2',
                '2 2',
            ),
            # winning side diagonal
            (
                '1 0',
                '0 2',
                '0 0',
                '1 1',
                '2 2',
                '2 0',
            ),
        )
        self.winners = (
            'x',
            'x',
            'o',
            'x',
            'o',
        )
        self.games = [TicTacGame() for _ in range(len(self.moves_for_games))]
        self.game_idx = 0
        self.move_idx = 0

    def set_game(self, game_idx):
        "Set game_idx as current game"
        self.game_idx = game_idx
        self.move_idx = 0

    def get_move(self, *argc):  # pylint: disable=unused-argument
        "Get current move and incriment move_idx."
        move = self.moves_for_games[self.game_idx][self.move_idx]
        self.move_idx += 1
        return move

    def test_start_game(self):
        """
        Test correct winner selection and correct moves number
        (for each game scenario in self.moves_for_games).
        """
        sys.stdout = StringIO()
        for game_idx, moves in enumerate(self.moves_for_games):
            self.set_game(game_idx)
            with unittest.mock.patch('builtins.input', self.get_move):
                winner = self.games[game_idx].start_game()
                self.assertEqual(winner, self.winners[game_idx])
                self.assertEqual(self.move_idx, len(moves))
        sys.stdout = sys.__stdout__


if __name__ == '__main__':
    unittest.main()
