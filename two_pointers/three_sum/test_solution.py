import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_threeSum_example1(solution):
    nums = [-1, 0, 1, 2, -1, -4]
    expected = [[-1, -1, 2], [-1, 0, 1]]
    
    assert sorted([sorted(x) for x in solution.threeSum(nums.copy())]) == sorted([sorted(x) for x in expected])
    assert sorted([sorted(x) for x in solution.threeSum_hash(nums.copy())]) == sorted([sorted(x) for x in expected])

def test_threeSum_example2(solution):
    nums = [0, 1, 1]
    expected = []
    
    assert solution.threeSum(nums.copy()) == expected
    assert solution.threeSum_hash(nums.copy()) == expected

def test_threeSum_example3(solution):
    nums = [0, 0, 0]
    expected = [[0, 0, 0]]
    
    assert sorted([sorted(x) for x in solution.threeSum(nums.copy())]) == sorted([sorted(x) for x in expected])
    assert sorted([sorted(x) for x in solution.threeSum_hash(nums.copy())]) == sorted([sorted(x) for x in expected])
