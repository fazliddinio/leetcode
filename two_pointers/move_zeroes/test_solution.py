import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_moveZeroes_example1(solution):
    nums = [0, 1, 0, 3, 12]
    nums_copy = nums.copy()
    
    solution.moveZeroes(nums)
    solution.moveZeroes_two_passes(nums_copy)
    
    assert nums == [1, 3, 12, 0, 0]
    assert nums_copy == [1, 3, 12, 0, 0]

def test_moveZeroes_example2(solution):
    nums = [0]
    nums_copy = nums.copy()
    
    solution.moveZeroes(nums)
    solution.moveZeroes_two_passes(nums_copy)
    
    assert nums == [0]
    assert nums_copy == [0]

def test_moveZeroes_no_zeros(solution):
    nums = [1, 2, 3]
    nums_copy = nums.copy()
    
    solution.moveZeroes(nums)
    solution.moveZeroes_two_passes(nums_copy)
    
    assert nums == [1, 2, 3]
    assert nums_copy == [1, 2, 3]

def test_moveZeroes_all_zeros(solution):
    nums = [0, 0, 0]
    nums_copy = nums.copy()
    
    solution.moveZeroes(nums)
    solution.moveZeroes_two_passes(nums_copy)
    
    assert nums == [0, 0, 0]
    assert nums_copy == [0, 0, 0]
