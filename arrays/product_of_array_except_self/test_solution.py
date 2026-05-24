import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_productExceptSelf_example1(solution):
    nums = [1, 2, 3, 4]
    assert solution.productExceptSelf(nums) == [24, 12, 8, 6]
    assert solution.productExceptSelf_arrays(nums) == [24, 12, 8, 6]

def test_productExceptSelf_example2(solution):
    nums = [-1, 1, 0, -3, 3]
    assert solution.productExceptSelf(nums) == [0, 0, 9, 0, 0]
    assert solution.productExceptSelf_arrays(nums) == [0, 0, 9, 0, 0]

def test_productExceptSelf_two_elements(solution):
    nums = [5, 6]
    assert solution.productExceptSelf(nums) == [6, 5]
    assert solution.productExceptSelf_arrays(nums) == [6, 5]

def test_productExceptSelf_all_zeros(solution):
    nums = [0, 0, 0]
    assert solution.productExceptSelf(nums) == [0, 0, 0]
    assert solution.productExceptSelf_arrays(nums) == [0, 0, 0]
