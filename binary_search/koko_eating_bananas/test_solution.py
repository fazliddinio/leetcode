import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_minEatingSpeed_example1(solution):
    piles = [3, 6, 7, 11]
    h = 8
    assert solution.minEatingSpeed(piles, h) == 4
    assert solution.minEatingSpeed_linear(piles, h) == 4

def test_minEatingSpeed_example2(solution):
    piles = [30, 11, 23, 4, 20]
    h = 5
    assert solution.minEatingSpeed(piles, h) == 30
    assert solution.minEatingSpeed_linear(piles, h) == 30

def test_minEatingSpeed_example3(solution):
    piles = [30, 11, 23, 4, 20]
    h = 6
    assert solution.minEatingSpeed(piles, h) == 23
    assert solution.minEatingSpeed_linear(piles, h) == 23
    
def test_minEatingSpeed_single(solution):
    piles = [10]
    h = 9
    assert solution.minEatingSpeed(piles, h) == 2
    assert solution.minEatingSpeed_linear(piles, h) == 2
