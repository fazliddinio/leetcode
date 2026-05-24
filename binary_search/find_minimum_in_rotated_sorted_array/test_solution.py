import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findMin_example1(solution):
    nums = [3, 4, 5, 1, 2]
    assert solution.findMin(nums) == 1
    assert solution.findMin_linear(nums) == 1

def test_findMin_example2(solution):
    nums = [4, 5, 6, 7, 0, 1, 2]
    assert solution.findMin(nums) == 0
    assert solution.findMin_linear(nums) == 0

def test_findMin_example3(solution):
    nums = [11, 13, 15, 17]
    assert solution.findMin(nums) == 11
    assert solution.findMin_linear(nums) == 11

def test_findMin_single(solution):
    nums = [5]
    assert solution.findMin(nums) == 5
    assert solution.findMin_linear(nums) == 5
