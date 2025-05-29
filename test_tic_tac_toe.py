import unittest
from tic_tac_toe import initialize_board, make_move, check_win, is_board_full, is_valid_move

class TestTicTacToe(unittest.TestCase):

    def test_check_win_row(self):
        # Test row win for X
        board = initialize_board()
        make_move(board, 0, 0, 'X')
        make_move(board, 0, 1, 'X')
        make_move(board, 0, 2, 'X')
        self.assertTrue(check_win(board, 'X'))

        # Test row win for O
        board = initialize_board()
        make_move(board, 1, 0, 'O')
        make_move(board, 1, 1, 'O')
        make_move(board, 1, 2, 'O')
        self.assertTrue(check_win(board, 'O'))

    def test_check_win_column(self):
        # Test column win for X
        board = initialize_board()
        make_move(board, 0, 0, 'X')
        make_move(board, 1, 0, 'X')
        make_move(board, 2, 0, 'X')
        self.assertTrue(check_win(board, 'X'))

        # Test column win for O
        board = initialize_board()
        make_move(board, 0, 1, 'O')
        make_move(board, 1, 1, 'O')
        make_move(board, 2, 1, 'O')
        self.assertTrue(check_win(board, 'O'))

    def test_check_win_diagonal(self):
        # Test principal diagonal win for X
        board = initialize_board()
        make_move(board, 0, 0, 'X')
        make_move(board, 1, 1, 'X')
        make_move(board, 2, 2, 'X')
        self.assertTrue(check_win(board, 'X'))

        # Test anti-diagonal win for O
        board = initialize_board()
        make_move(board, 0, 2, 'O')
        make_move(board, 1, 1, 'O')
        make_move(board, 2, 0, 'O')
        self.assertTrue(check_win(board, 'O'))

    def test_no_win(self):
        board = initialize_board()
        make_move(board, 0, 0, 'X')
        make_move(board, 0, 1, 'O')
        make_move(board, 1, 0, 'X')
        self.assertFalse(check_win(board, 'X'))
        self.assertFalse(check_win(board, 'O'))

    def test_draw(self):
        board = initialize_board()
        # X, O, X
        # O, X, O
        # O, X, O
        make_move(board, 0, 0, 'X')
        make_move(board, 0, 1, 'O')
        make_move(board, 0, 2, 'X')
        make_move(board, 1, 0, 'O')
        make_move(board, 1, 1, 'X')
        make_move(board, 1, 2, 'O')
        make_move(board, 2, 0, 'O')
        make_move(board, 2, 1, 'X')
        make_move(board, 2, 2, 'O')
        self.assertFalse(check_win(board, 'X'))
        self.assertFalse(check_win(board, 'O'))
        self.assertTrue(is_board_full(board))

    def test_board_not_full(self):
        board = initialize_board()
        make_move(board, 0, 0, 'X')
        make_move(board, 0, 1, 'O')
        self.assertFalse(is_board_full(board))

    def test_is_valid_move(self):
        board = initialize_board()
        make_move(board, 0, 0, 'X')
        self.assertFalse(is_valid_move(board, 0, 0)) # Already taken
        self.assertTrue(is_valid_move(board, 0, 1)) # Empty
        self.assertFalse(is_valid_move(board, 3, 0)) # Out of bounds
        self.assertFalse(is_valid_move(board, 0, 3)) # Out of bounds
        self.assertFalse(is_valid_move(board, -1, 0))# Out of bounds


if __name__ == '__main__':
    unittest.main()
