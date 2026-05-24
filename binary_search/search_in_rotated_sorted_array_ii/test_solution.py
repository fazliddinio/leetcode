import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_search_example1(solution):
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 0
    assert solution.search(nums, target) is True
    assert solution.search_linear(nums, target) is True

def test_search_example2(solution):
    nums = [2, 5, 6, 0, 0, 1, 2]
    target = 3
    assert solution.search(nums, target) is False
    assert solution.search_linear(nums, target) is False

def test_search_duplicates(solution):
    nums = [1, 0, 1, 1, 1]
    target = 0
    assert solution.search(nums, target) is True
    assert solution.search_linear(nums, target) is True

def test_search_all_same(solution):
    nums = [1, 1, 1, 1, 1]
    target = 2
    assert solution.search(nums, target) is False
    assert solution.search_linear(nums, target) is False
