import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_minSubArrayLen_example1(solution):
    target = 7
    nums = [2, 3, 1, 2, 4, 3]
    assert solution.minSubArrayLen(target, nums) == 2
    assert solution.minSubArrayLen_binary_search(target, nums) == 2

def test_minSubArrayLen_example2(solution):
    target = 4
    nums = [1, 4, 4]
    assert solution.minSubArrayLen(target, nums) == 1
    assert solution.minSubArrayLen_binary_search(target, nums) == 1

def test_minSubArrayLen_example3(solution):
    target = 11
    nums = [1, 1, 1, 1, 1, 1, 1, 1]
    assert solution.minSubArrayLen(target, nums) == 0
    assert solution.minSubArrayLen_binary_search(target, nums) == 0

def test_minSubArrayLen_exact_sum(solution):
    target = 15
    nums = [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]
    assert solution.minSubArrayLen(target, nums) == 2
    assert solution.minSubArrayLen_binary_search(target, nums) == 2
