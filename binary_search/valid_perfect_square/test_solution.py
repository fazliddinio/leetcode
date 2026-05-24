import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_isPerfectSquare_example1(solution):
    num = 16
    assert solution.isPerfectSquare(num) is True
    assert solution.isPerfectSquare_math(num) is True

def test_isPerfectSquare_example2(solution):
    num = 14
    assert solution.isPerfectSquare(num) is False
    assert solution.isPerfectSquare_math(num) is False

def test_isPerfectSquare_one(solution):
    num = 1
    assert solution.isPerfectSquare(num) is True
    assert solution.isPerfectSquare_math(num) is True

def test_isPerfectSquare_zero(solution):
    num = 0
    assert solution.isPerfectSquare(num) is True
    assert solution.isPerfectSquare_math(num) is True

def test_isPerfectSquare_large(solution):
    num = 2147483647
    assert solution.isPerfectSquare(num) is False
    assert solution.isPerfectSquare_math(num) is False
