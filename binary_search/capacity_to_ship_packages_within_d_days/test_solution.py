import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_shipWithinDays_example1(solution):
    weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    days = 5
    assert solution.shipWithinDays(weights, days) == 15
    assert solution.shipWithinDays_linear(weights, days) == 15

def test_shipWithinDays_example2(solution):
    weights = [3, 2, 2, 4, 1, 4]
    days = 3
    assert solution.shipWithinDays(weights, days) == 6
    assert solution.shipWithinDays_linear(weights, days) == 6
