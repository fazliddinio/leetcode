import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_longestOnes_example1(solution):
    nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    k = 2
    assert solution.longestOnes(nums, k) == 6
    assert solution.longestOnes_strict(nums, k) == 6

def test_longestOnes_example2(solution):
    nums = [0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]
    k = 3
    assert solution.longestOnes(nums, k) == 10
    assert solution.longestOnes_strict(nums, k) == 10

def test_longestOnes_k_zero(solution):
    nums = [1, 1, 0, 1, 1]
    k = 0
    assert solution.longestOnes(nums, k) == 2
    assert solution.longestOnes_strict(nums, k) == 2

def test_longestOnes_all_zeros_k_larger(solution):
    nums = [0, 0, 0]
    k = 5
    assert solution.longestOnes(nums, k) == 3
    assert solution.longestOnes_strict(nums, k) == 3
