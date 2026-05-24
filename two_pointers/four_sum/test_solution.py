import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_fourSum_example1(solution):
    nums = [1,0,-1,0,-2,2]
    target = 0
    expected = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    
    assert sorted([sorted(x) for x in solution.fourSum(nums.copy(), target)]) == sorted([sorted(x) for x in expected])
    assert sorted([sorted(x) for x in solution.fourSum_iterative(nums.copy(), target)]) == sorted([sorted(x) for x in expected])

def test_fourSum_example2(solution):
    nums = [2,2,2,2,2]
    target = 8
    expected = [[2,2,2,2]]
    
    assert sorted([sorted(x) for x in solution.fourSum(nums.copy(), target)]) == sorted([sorted(x) for x in expected])
    assert sorted([sorted(x) for x in solution.fourSum_iterative(nums.copy(), target)]) == sorted([sorted(x) for x in expected])

def test_fourSum_empty(solution):
    nums = []
    target = 0
    assert solution.fourSum(nums.copy(), target) == []
    assert solution.fourSum_iterative(nums.copy(), target) == []
