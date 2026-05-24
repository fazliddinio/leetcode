import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_max_profit_example1(solution):
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5
    assert solution.maxProfit_mintrack(prices) == 5

def test_max_profit_no_profit(solution):
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0
    assert solution.maxProfit_mintrack(prices) == 0

def test_max_profit_single_day(solution):
    prices = [5]
    assert solution.maxProfit(prices) == 0
    assert solution.maxProfit_mintrack(prices) == 0

def test_max_profit_two_days_profit(solution):
    prices = [1, 2]
    assert solution.maxProfit(prices) == 1
    assert solution.maxProfit_mintrack(prices) == 1

def test_max_profit_constant_prices(solution):
    prices = [3, 3, 3, 3]
    assert solution.maxProfit(prices) == 0
    assert solution.maxProfit_mintrack(prices) == 0
