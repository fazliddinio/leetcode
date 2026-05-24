import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_isHappy_example1(solution):
    n = 19
    assert solution.isHappy(n) is True
    assert solution.isHappy_set(n) is True

def test_isHappy_example2(solution):
    n = 2
    assert solution.isHappy(n) is False
    assert solution.isHappy_set(n) is False

def test_isHappy_one(solution):
    n = 1
    assert solution.isHappy(n) is True
    assert solution.isHappy_set(n) is True

def test_isHappy_seven(solution):
    n = 7
    assert solution.isHappy(n) is True
    assert solution.isHappy_set(n) is True
