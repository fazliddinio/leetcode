import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_search_example1(solution):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    assert solution.search(nums, target) == 4
    assert solution.search_linear(nums, target) == 4

def test_search_example2(solution):
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    assert solution.search(nums, target) == -1
    assert solution.search_linear(nums, target) == -1

def test_search_single_match(solution):
    nums = [1]
    target = 1
    assert solution.search(nums, target) == 0
    assert solution.search_linear(nums, target) == 0

def test_search_single_nomatch(solution):
    nums = [1]
    target = 0
    assert solution.search(nums, target) == -1
    assert solution.search_linear(nums, target) == -1
