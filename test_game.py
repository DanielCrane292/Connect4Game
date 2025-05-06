# File: test_game.py
# Name: Xingzuo Li
# Student ID: 2295275

import unittest
from game import Game

class TestGame(unittest.TestCase):

    def test_initial_board_is_empty(self):
        game = Game()
        for row in range(6):
            for col in range(7):
                self.assertEqual(' ', game.get_board_cell(row, col))

    def test_make_valid_move(self):
        game = Game()
        self.assertTrue(game.make_move(3))
        self.assertEqual('X', game.get_board_cell(5, 3))

    def test_repeated_move_on_same_column(self):
        game = Game()
        for i in range(6):
            self.assertTrue(game.make_move(0))
        self.assertFalse(game.make_move(0))  # The 7th move should fail (column is full)

    def test_make_invalid_move(self):
        game = Game()
        self.assertFalse(game.make_move(7))  # Column index too high
        self.assertFalse(game.make_move(-1))  # Column index too low

    def test_make_move_in_full_column(self):
        game = Game()
        for _ in range(6):
            game.make_move(0)
        self.assertFalse(game.make_move(0))  # Column should be full now

    def test_switch_player(self):
        game = Game()
        self.assertEqual('X', game.get_current_player())
        game.switch_player()
        self.assertEqual('O', game.get_current_player())
        game.switch_player()
        self.assertEqual('X', game.get_current_player())

    def test_check_win_horizontal(self):
        game = Game()
        for col in range(4):
            game.make_move(col)
            if col < 3:
                game.switch_player()
                game.make_move(col)
                game.switch_player()
        self.assertTrue(game.check_win())

    def test_check_win_vertical(self):
        game = Game()
        for _ in range(4):
            game.make_move(0)
            if _ < 3:
                game.switch_player()
                game.make_move(1)
                game.switch_player()
        self.assertTrue(game.check_win())

    def test_check_win_diagonal_ascending(self):
        game = Game()
        moves = [(0, 'X'), (1, 'O'), (1, 'X'), (2, 'O'), (2, 'X'), (3, 'O'), (2, 'X'),
                 (3, 'O'), (3, 'X'), (0, 'O'), (3, 'X')]
        for col, player in moves:
            game.current_player = player
            game.make_move(col)
        self.assertTrue(game.check_win())

    def test_check_win_diagonal_descending(self):
        game = Game()
        moves = [(3, 'X'), (2, 'O'), (2, 'X'), (1, 'O'), (1, 'X'), (0, 'O'), (1, 'X'),
                 (0, 'O'), (0, 'X'), (3, 'O'), (0, 'X')]
        for col, player in moves:
            game.current_player = player
            game.make_move(col)
        self.assertTrue(game.check_win())

    def test_no_win_yet(self):
        game = Game()
        game.make_move(0)
        game.switch_player()
        game.make_move(1)
        game.switch_player()
        game.make_move(2)
        game.switch_player()
        game.make_move(3)
        self.assertFalse(game.check_win())

    def test_is_board_full_when_full(self):
        game = Game()
        for col in range(7):
            for _ in range(6):
                game.make_move(col)
        self.assertTrue(game.is_board_full())

    def test_is_board_full_when_not_full(self):
        game = Game()
        game.make_move(0)
        game.switch_player()
        game.make_move(1)
        self.assertFalse(game.is_board_full())

if __name__ == '__main__':
    unittest.main()
