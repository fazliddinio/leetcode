import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_removeDuplicates_example1(solution):
    nums = [1, 1, 2]
    nums_copy = nums.copy()
    
    k = solution.removeDuplicates(nums)
    k_copy = solution.removeDuplicates_set(nums_copy)
    
    assert k == 2
    assert nums[:k] == [1, 2]
    assert k_copy == 2
    assert nums_copy[:k_copy] == [1, 2]

def test_removeDuplicates_example2(solution):
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    nums_copy = nums.copy()
    
    k = solution.removeDuplicates(nums)
    k_copy = solution.removeDuplicates_set(nums_copy)
    
    assert k == 5
    assert nums[:k] == [0, 1, 2, 3, 4]
    assert k_copy == 5
    assert nums_copy[:k_copy] == [0, 1, 2, 3, 4]

def test_removeDuplicates_empty(solution):
    assert solution.removeDuplicates([]) == 0
    assert solution.removeDuplicates_set([]) == 0

def test_removeDuplicates_no_duplicates(solution):
    nums = [1, 2, 3]
    nums_copy = nums.copy()
    
    k = solution.removeDuplicates(nums)
    k_copy = solution.removeDuplicates_set(nums_copy)
    
    assert k == 3
    assert nums[:k] == [1, 2, 3]
    assert k_copy == 3
    assert nums_copy[:k_copy] == [1, 2, 3]
