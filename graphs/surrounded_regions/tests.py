import unittest
from solution import Solution

class TestSurroundedRegions(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        """Tests the standard case with a region to capture."""
        board = [
            ["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]
        ]
        expected = [
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","X","X","X"],
            ["X","O","X","X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_example_2(self):
        """Tests a case with only one cell, which cannot be captured."""
        board = [["X"]]
        expected = [["X"]]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_all_o(self):
        """Tests a board with all 'O's, none should be captured as they touch the border."""
        board = [
            ["O","O","O"],
            ["O","O","O"],
            ["O","O","O"]
        ]
        expected = [
            ["O","O","O"],
            ["O","O","O"],
            ["O","O","O"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)

    def test_inner_o_capture(self):
        """Tests a case where only inner 'O's should be captured."""
        board = [
            ["X","X","X"],
            ["X","O","X"],
            ["X","X","X"]
        ]
        expected = [
            ["X","X","X"],
            ["X","X","X"],
            ["X","X","X"]
        ]
        self.solution.solve(board)
        self.assertEqual(board, expected)
        
    def test_empty_board(self):
        """Tests an empty board."""
        board = []
        expected = []
        self.solution.solve(board)
        self.assertEqual(board, expected)

if __name__ == '__main__':
    unittest.main()
