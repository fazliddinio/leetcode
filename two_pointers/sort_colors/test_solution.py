import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_sortColors_example1(solution):
    nums = [2, 0, 2, 1, 1, 0]
    nums_copy = nums.copy()
    
    solution.sortColors(nums)
    solution.sortColors_counting(nums_copy)
    
    assert nums == [0, 0, 1, 1, 2, 2]
    assert nums_copy == [0, 0, 1, 1, 2, 2]

def test_sortColors_example2(solution):
    nums = [2, 0, 1]
    nums_copy = nums.copy()
    
    solution.sortColors(nums)
    solution.sortColors_counting(nums_copy)
    
    assert nums == [0, 1, 2]
    assert nums_copy == [0, 1, 2]

def test_sortColors_all_same(solution):
    nums = [1, 1, 1]
    nums_copy = nums.copy()
    
    solution.sortColors(nums)
    solution.sortColors_counting(nums_copy)
    
    assert nums == [1, 1, 1]
    assert nums_copy == [1, 1, 1]

def test_sortColors_empty(solution):
    nums = []
    nums_copy = nums.copy()
    
    solution.sortColors(nums)
    solution.sortColors_counting(nums_copy)
    
    assert nums == []
    assert nums_copy == []
