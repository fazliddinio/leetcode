import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findMaxAverage_example1(solution):
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    assert abs(solution.findMaxAverage(nums, k) - 12.75) < 1e-5
    assert abs(solution.findMaxAverage_prefix(nums, k) - 12.75) < 1e-5

def test_findMaxAverage_example2(solution):
    nums = [5]
    k = 1
    assert abs(solution.findMaxAverage(nums, k) - 5.0) < 1e-5
    assert abs(solution.findMaxAverage_prefix(nums, k) - 5.0) < 1e-5

def test_findMaxAverage_all_negative(solution):
    nums = [-1, -3, -5, -6, -2, -4]
    k = 2
    assert abs(solution.findMaxAverage(nums, k) - (-2.0)) < 1e-5
    assert abs(solution.findMaxAverage_prefix(nums, k) - (-2.0)) < 1e-5
