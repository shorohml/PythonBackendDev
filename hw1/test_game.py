"Tests for tic-tac-toe game."
import sys
import unittest
import unittest.mock
from io import StringIO

from parameterized import parameterized

from game import TicTacGame


class ValidateInputTest(unittest.TestCase):

    "Test case for TicTacGame.validate_input."

    def setUp(self):
        self.game = TicTacGame()

    @parameterized.expand([
        ('1 1', (1, 1)),
        ('0 0', (0, 0)),
        ('2 2', (2, 2)),
        ('0 1', (0, 1)),
        ('0 2', (0, 2)),
        ('2 0', (2, 0)),
        ('1 2', (1, 2)),
    ])
    def test_valid_input(self, user_input, correct_result):
        "Test TicTacGame.validate_input when user input is valid."
        result = self.game.validate_input(user_input)
        self.assertEqual(correct_result, result)

    @parameterized.expand([
        '',
        'aaa 1',
        '0, bbbb',
        'asdaf kfjgkfjgk',
        '-1 0',
        '0 100',
        '1, 2',
        '-20 -100',
        '0 1 2'
    ])
    def test_invalid_input(self, user_input):
        "Test TicTacGame.validate_input when user input is invalid."
        self.assertRaises(ValueError, self.game.validate_input, user_input)


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


class CheckWinnerOrTieTest(unittest.TestCase):

    "Test case for TicTacGame.check_winner_or_tie."

    def setUp(self):
        self.game = TicTacGame()

    def test_empty_board(self):
        "Test correct output for empty board."
        self.assertEqual('no', self.game.check_winner_or_tie())


def ignore_stdout(func):

    "Decorator to ignore stuff printed to stdout"

    def wrapper(*argc, **argw):
        sys.stdout = StringIO()
        result = func(*argc, **argw)
        sys.stdout = sys.__stdout__
        return result

    return wrapper


class StartgameTest(unittest.TestCase):

    "Test case for TicTacGame.start_game."

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
            # tie
            (
                '0 0',
                '1 1',
                '0 2',
                '0 1',
                '2 0',
                '1 0',
                '1 2',
                '2 2',
                '2 1',
            ),
        )
        self.results = (
            'x',
            'x',
            'o',
            'x',
            'o',
            'tie',
        )
        self.game = TicTacGame()
        self.game_idx = 0
        self.move_idx = 0

    def get_move(self, *argc):  # pylint: disable=unused-argument
        "Get current move and incriment move_idx."
        move = self.moves_for_games[self.game_idx][self.move_idx]
        self.move_idx += 1
        return move

    @ignore_stdout
    def test_start_game_0(self):
        "Test correct winner selection and correct moves number."
        self.game_idx = 0
        with unittest.mock.patch('builtins.input', self.get_move):
            result = self.game.start_game()
            self.assertEqual(result, self.results[self.game_idx])
            self.assertEqual(self.move_idx, len(self.moves_for_games[self.game_idx]))

    @ignore_stdout
    def test_start_game_1(self):
        "Test correct winner selection and correct moves number"
        self.game_idx = 1
        with unittest.mock.patch('builtins.input', self.get_move):
            result = self.game.start_game()
            self.assertEqual(result, self.results[self.game_idx])
            self.assertEqual(self.move_idx, len(self.moves_for_games[self.game_idx]))

    @ignore_stdout
    def test_start_game_2(self):
        "Test correct winner selection and correct moves number"
        self.game_idx = 2
        with unittest.mock.patch('builtins.input', self.get_move):
            result = self.game.start_game()
            self.assertEqual(result, self.results[self.game_idx])
            self.assertEqual(self.move_idx, len(self.moves_for_games[self.game_idx]))

    @ignore_stdout
    def test_start_game_3(self):
        "Test correct winner selection and correct moves number"
        self.game_idx = 3
        with unittest.mock.patch('builtins.input', self.get_move):
            result = self.game.start_game()
            self.assertEqual(result, self.results[self.game_idx])
            self.assertEqual(self.move_idx, len(self.moves_for_games[self.game_idx]))

    @ignore_stdout
    def test_start_game_4(self):
        "Test correct winner selection and correct moves number"
        self.game_idx = 4
        with unittest.mock.patch('builtins.input', self.get_move):
            result = self.game.start_game()
            self.assertEqual(result, self.results[self.game_idx])
            self.assertEqual(self.move_idx, len(self.moves_for_games[self.game_idx]))

    @ignore_stdout
    def test_start_game_5(self):
        "Test correct winner selection and correct moves number"
        self.game_idx = 5
        with unittest.mock.patch('builtins.input', self.get_move):
            result = self.game.start_game()
            self.assertEqual(result, self.results[self.game_idx])
            self.assertEqual(self.move_idx, len(self.moves_for_games[self.game_idx]))


if __name__ == '__main__':
    unittest.main()
