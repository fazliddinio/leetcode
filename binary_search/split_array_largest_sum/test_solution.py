import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_splitArray_example1(solution):
    nums = [7, 2, 5, 10, 8]
    k = 2
    assert solution.splitArray(nums, k) == 18
    assert solution.splitArray_dp(nums, k) == 18

def test_splitArray_example2(solution):
    nums = [1, 2, 3, 4, 5]
    k = 2
    assert solution.splitArray(nums, k) == 9
    assert solution.splitArray_dp(nums, k) == 9

def test_splitArray_example3(solution):
    nums = [1, 4, 4]
    k = 3
    assert solution.splitArray(nums, k) == 4
    assert solution.splitArray_dp(nums, k) == 4

def test_splitArray_single_split(solution):
    nums = [1, 2, 3]
    k = 1
    assert solution.splitArray(nums, k) == 6
    assert solution.splitArray_dp(nums, k) == 6
