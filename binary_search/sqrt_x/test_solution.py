import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_mySqrt_example1(solution):
    x = 4
    assert solution.mySqrt(x) == 2
    assert solution.mySqrt_newton(x) == 2

def test_mySqrt_example2(solution):
    x = 8
    assert solution.mySqrt(x) == 2
    assert solution.mySqrt_newton(x) == 2

def test_mySqrt_zero(solution):
    x = 0
    assert solution.mySqrt(x) == 0
    assert solution.mySqrt_newton(x) == 0

def test_mySqrt_one(solution):
    x = 1
    assert solution.mySqrt(x) == 1
    assert solution.mySqrt_newton(x) == 1

def test_mySqrt_large(solution):
    x = 1000000
    assert solution.mySqrt(x) == 1000
    assert solution.mySqrt_newton(x) == 1000
