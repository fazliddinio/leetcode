import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_searchInsert_example1(solution):
    nums = [1, 3, 5, 6]
    target = 5
    assert solution.searchInsert(nums, target) == 2
    assert solution.searchInsert_linear(nums, target) == 2

def test_searchInsert_example2(solution):
    nums = [1, 3, 5, 6]
    target = 2
    assert solution.searchInsert(nums, target) == 1
    assert solution.searchInsert_linear(nums, target) == 1

def test_searchInsert_example3(solution):
    nums = [1, 3, 5, 6]
    target = 7
    assert solution.searchInsert(nums, target) == 4
    assert solution.searchInsert_linear(nums, target) == 4

def test_searchInsert_example4(solution):
    nums = [1, 3, 5, 6]
    target = 0
    assert solution.searchInsert(nums, target) == 0
    assert solution.searchInsert_linear(nums, target) == 0
