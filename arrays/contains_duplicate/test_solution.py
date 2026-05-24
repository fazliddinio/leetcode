import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_containsDuplicate_example1(solution):
    nums = [1, 2, 3, 1]
    assert solution.containsDuplicate(nums) is True
    assert solution.containsDuplicate_sorting(nums) is True

def test_containsDuplicate_example2(solution):
    nums = [1, 2, 3, 4]
    assert solution.containsDuplicate(nums) is False
    assert solution.containsDuplicate_sorting(nums) is False

def test_containsDuplicate_example3(solution):
    nums = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    assert solution.containsDuplicate(nums) is True
    assert solution.containsDuplicate_sorting(nums) is True

def test_containsDuplicate_empty(solution):
    nums = []
    assert solution.containsDuplicate(nums) is False
    assert solution.containsDuplicate_sorting(nums) is False
