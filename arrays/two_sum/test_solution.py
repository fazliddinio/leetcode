import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_twoSum_example1(solution):
    nums = [2, 7, 11, 15]
    target = 9
    assert sorted(solution.twoSum(nums, target)) == [0, 1]
    assert sorted(solution.twoSum_brute(nums, target)) == [0, 1]

def test_twoSum_example2(solution):
    nums = [3, 2, 4]
    target = 6
    assert sorted(solution.twoSum(nums, target)) == [1, 2]
    assert sorted(solution.twoSum_brute(nums, target)) == [1, 2]

def test_twoSum_example3(solution):
    nums = [3, 3]
    target = 6
    assert sorted(solution.twoSum(nums, target)) == [0, 1]
    assert sorted(solution.twoSum_brute(nums, target)) == [0, 1]

def test_twoSum_not_found(solution):
    nums = [1, 2, 3]
    target = 10
    assert solution.twoSum(nums, target) == []
    assert solution.twoSum_brute(nums, target) == []
