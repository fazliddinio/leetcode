import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_searchRange_example1(solution):
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    assert solution.searchRange(nums, target) == [3, 4]
    assert solution.searchRange_bisect(nums, target) == [3, 4]

def test_searchRange_example2(solution):
    nums = [5, 7, 7, 8, 8, 10]
    target = 6
    assert solution.searchRange(nums, target) == [-1, -1]
    assert solution.searchRange_bisect(nums, target) == [-1, -1]

def test_searchRange_empty(solution):
    nums = []
    target = 0
    assert solution.searchRange(nums, target) == [-1, -1]
    assert solution.searchRange_bisect(nums, target) == [-1, -1]

def test_searchRange_single(solution):
    nums = [1]
    target = 1
    assert solution.searchRange(nums, target) == [0, 0]
    assert solution.searchRange_bisect(nums, target) == [0, 0]
