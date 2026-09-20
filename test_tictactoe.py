import io
import unittest
from contextlib import redirect_stdout
from unittest import mock
from tictactoe import check_winner, print_board, get_row_column, tic_tac_toe, get_player_move, get_comp_move

class TestGetRowColumn(unittest.TestCase):
    def test_get_row_column(self):
        cases = {1: (0, 0), 2: (0, 1), 3: (0, 2), 4: (1, 0), 5: (1,1), 6: (1, 2)}
        for number, expected in cases.items():
            with self.subTest(number=number):
                self.assertEqual(get_row_column(number), expected)


class TestCheckWinner(unittest.TestCase):

    def setUp(self):
        self.board = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

    def test_row_win_o(self):
        self.board[1] = ['O', 'O', 'O']
        self.assertFalse(check_winner(self.board))

    def test_row_win_x(self):
        self.board[1] = ['X', 'X', 'X']
        self.assertTrue(check_winner(self.board))

    def test_column_win_o(self):
        self.board[0][0] = 'O'
        self.board[1][0] = 'O'
        self.board[2][0] = 'O'
        self.assertFalse(check_winner(self.board))

    def test_column_win_x(self):
        self.board[0][0] = 'X'
        self.board[1][0] = 'X'
        self.board[2][0] = 'X'
        self.assertTrue(check_winner(self.board))

    def test_diagonal_win_o(self):
        self.board[0][0] = 'O'
        self.board[1][1] = 'O'
        self.board[2][2] = 'O'
        self.assertFalse(check_winner(self.board))

    def test_diagonal_win_x(self):
        self.board[0][0] = 'X'
        self.board[1][1] = 'X'
        self.board[2][2] = 'X'
        self.assertTrue(check_winner(self.board))

    def test_anti_diagonal_win_o(self):
        self.board[0][2] = 'O'
        self.board[1][1] = 'O'
        self.board[2][0] = 'O'
        self.assertFalse(check_winner(self.board))

    def test_anti_diagonal_win_x(self):
        self.board[0][2] = 'X'
        self.board[1][1] = 'X'
        self.board[2][0] = 'X'
        self.assertTrue(check_winner(self.board))

    def test_equal(self):
        self.board = self.board = [['O', 'X', 'X'], ['X', 'X', 'O'], ['O', 'O', 'X']]
        self.assertEqual(check_winner(self.board), 'equal')


class TestPrintBoard(unittest.TestCase):
    def test_output_format(self):
        self.board = [['1', '2', 'X'], ['4', 'O', '6'], ['X', '8', '9']]
        buf = io.StringIO()
        with redirect_stdout(buf):
            print_board(self.board)
        output = buf.getvalue()
        print(output)
        self.assertEqual(
            output,
            '1 | 2 | X\n--------\n4 | O | 6\n--------\nX | 8 | 9\n'
        )


class TestPlayerMove(unittest.TestCase):

    def setUp(self):
        self.board = [['1', '2', 'X'], ['4', 'O', '6'], ['X', '8', '9']]

    @mock.patch('builtins.input', side_effect=['1'])
    def test_valid_input(self, mock_input):
        get_player_move(self.board)
        self.assertEqual(self.board[0][0], 'X')

    @mock.patch('builtins.input', side_effect= ['10', '1'])
    def test_out_of_range_input(self, mock_input):
        get_player_move(self.board)
        self.assertEqual(self.board[0][0], 'X')

    @mock.patch('builtins.input', side_effect=['sdd', '1'])
    def test_string_input(self, mock_input):
        get_player_move(self.board)
        self.assertEqual(self.board[0][0], 'X')

    @mock.patch('builtins.input', side_effect=['3', '2'])
    def test_occupied_cell_by_x(self, mock_input):
        get_player_move(self.board)
        self.assertEqual(self.board[0][2], 'X')
        self.assertEqual(self.board[0][1], 'X')

    @mock.patch('builtins.input', side_effect=['5', '9'])
    def test_occupied_cell_by_o(self, mock_input):
        get_player_move(self.board)
        self.assertEqual(self.board[1][1], 'O')
        self.assertEqual(self.board[2][2], 'X')

    @mock.patch('builtins.input', side_effect=['5', '7', '9'])
    def test_occupied_cell_by_o_and_x_input(self, mock_input):
        get_player_move(self.board)
        self.assertEqual(self.board[1][1], 'O')
        self.assertEqual(self.board[2][0], 'X')
        self.assertEqual(self.board[2][2], 'X')

class TestCompMove(unittest.TestCase):

    def setUp(self):
        self.board = [['1', '2', 'X'], ['4', 'O', '6'], ['X', '8', 'O']]

    @mock.patch('random.randint', return_value = 1)
    def test_places_o_on_empty_cell(self, mock_random):
        get_comp_move(self.board)
        self.assertEqual(self.board[0][0], 'O')

    @mock.patch('random.randint', side_effect = [3, 1])
    def test_places_o_on_occupied_cell(self, mock_random):
        get_comp_move(self.board)
        self.assertEqual(self.board[0][2], 'X')
        self.assertEqual(self.board[0][0], 'O')
