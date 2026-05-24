import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_search_example1(solution):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    assert solution.search(nums, target) == 4
    assert solution.search_recursive(nums, target) == 4

def test_search_example2(solution):
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2
    assert solution.search(nums, target) == -1
    assert solution.search_recursive(nums, target) == -1

def test_search_empty(solution):
    nums = []
    target = 5
    assert solution.search(nums, target) == -1
    assert solution.search_recursive(nums, target) == -1

def test_search_single(solution):
    nums = [5]
    target = 5
    assert solution.search(nums, target) == 0
    assert solution.search_recursive(nums, target) == 0
