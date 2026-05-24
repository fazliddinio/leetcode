import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_maxTurbulenceSize_example1(solution):
    arr = [9, 4, 2, 10, 7, 8, 8, 1, 9]
    assert solution.maxTurbulenceSize(arr) == 5
    assert solution.maxTurbulenceSize_dp(arr) == 5

def test_maxTurbulenceSize_example2(solution):
    arr = [4, 8, 12, 16]
    assert solution.maxTurbulenceSize(arr) == 2
    assert solution.maxTurbulenceSize_dp(arr) == 2

def test_maxTurbulenceSize_example3(solution):
    arr = [100]
    assert solution.maxTurbulenceSize(arr) == 1
    assert solution.maxTurbulenceSize_dp(arr) == 1

def test_maxTurbulenceSize_all_same(solution):
    arr = [9, 9, 9, 9]
    assert solution.maxTurbulenceSize(arr) == 1
    assert solution.maxTurbulenceSize_dp(arr) == 1
