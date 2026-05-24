import unittest
from solution import Solution

class TestNQueens(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_4(self):
        """Tests the 4-Queens problem, which has 2 distinct solutions."""
        n = 4
        expected = [
            [".Q..", "...Q", "Q...", "..Q."],
            ["..Q.", "Q...", "...Q", ".Q.."]
        ]
        result = self.solution.solveNQueens(n)
        # Sort results to ensure order doesn't matter for comparison
        self.assertEqual(sorted(result), sorted(expected))

    def test_n_1(self):
        """Tests the 1-Queen problem, which has 1 trivial solution."""
        n = 1
        expected = [["Q"]]
        self.assertEqual(self.solution.solveNQueens(n), expected)

    def test_n_2(self):
        """Tests the 2-Queens problem, which has no solution."""
        n = 2
        expected = []
        self.assertEqual(self.solution.solveNQueens(n), expected)

    def test_n_3(self):
        """Tests the 3-Queens problem, which has no solution."""
        n = 3
        expected = []
        self.assertEqual(self.solution.solveNQueens(n), expected)

if __name__ == '__main__':
    unittest.main()
