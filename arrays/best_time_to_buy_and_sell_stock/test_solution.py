import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_maxProfit_example1(solution):
    prices = [7, 1, 5, 3, 6, 4]
    assert solution.maxProfit(prices) == 5
    assert solution.maxProfit_brute(prices) == 5

def test_maxProfit_example2(solution):
    prices = [7, 6, 4, 3, 1]
    assert solution.maxProfit(prices) == 0
    assert solution.maxProfit_brute(prices) == 0

def test_maxProfit_empty(solution):
    prices = []
    assert solution.maxProfit(prices) == 0
    assert solution.maxProfit_brute(prices) == 0

def test_maxProfit_one_element(solution):
    prices = [5]
    assert solution.maxProfit(prices) == 0
    assert solution.maxProfit_brute(prices) == 0
