import unittest
from best_time_to_buy_and_sell_stock import Solution


class TestMaxProfit(unittest.TestCase):
    def setUp(self):
        solution = Solution

    def test_normal_case_with_profit(self):
        result = self.solution.maxProfit([2, 3, 1, 4, 8, 7])
        self.assertEqual(result, 7)

    def test_decreasing_prices(self):
        self.assertEqual(self.solution.maxProfit([7, 6, 5, 4, 3]), 0)

    def test_single_transaction_best(self):
        result = self.solution.maxProfit([2, 4, 1, 7])
        self.assertEqual(result, 6)

    def 