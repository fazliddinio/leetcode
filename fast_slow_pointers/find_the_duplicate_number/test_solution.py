import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findDuplicate_example1(solution):
    nums = [1, 3, 4, 2, 2]
    assert solution.findDuplicate(nums) == 2
    assert solution.findDuplicate_binary_search(nums) == 2

def test_findDuplicate_example2(solution):
    nums = [3, 1, 3, 4, 2]
    assert solution.findDuplicate(nums) == 3
    assert solution.findDuplicate_binary_search(nums) == 3

def test_findDuplicate_example3(solution):
    nums = [1, 1]
    assert solution.findDuplicate(nums) == 1
    assert solution.findDuplicate_binary_search(nums) == 1

def test_findDuplicate_multiple_duplicates(solution):
    nums = [2, 2, 2, 2, 2]
    assert solution.findDuplicate(nums) == 2
    assert solution.findDuplicate_binary_search(nums) == 2
