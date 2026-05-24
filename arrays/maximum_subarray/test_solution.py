import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_maxSubArray_example1(solution):
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert solution.maxSubArray(nums) == 6
    assert solution.maxSubArray_brute(nums) == 6

def test_maxSubArray_example2(solution):
    nums = [1]
    assert solution.maxSubArray(nums) == 1
    assert solution.maxSubArray_brute(nums) == 1

def test_maxSubArray_example3(solution):
    nums = [5, 4, -1, 7, 8]
    assert solution.maxSubArray(nums) == 23
    assert solution.maxSubArray_brute(nums) == 23

def test_maxSubArray_all_negative(solution):
    nums = [-3, -5, -2, -9]
    assert solution.maxSubArray(nums) == -2
    assert solution.maxSubArray_brute(nums) == -2
