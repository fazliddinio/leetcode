import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_circularArrayLoop_example1(solution):
    nums = [2, -1, 1, 2, 2]
    assert solution.circularArrayLoop_dfs(nums.copy()) is True
    assert solution.circularArrayLoop(nums.copy()) is True

def test_circularArrayLoop_example2(solution):
    nums = [-1, 2]
    assert solution.circularArrayLoop_dfs(nums.copy()) is False
    assert solution.circularArrayLoop(nums.copy()) is False

def test_circularArrayLoop_example3(solution):
    nums = [-2, 1, -1, -2, -2]
    assert solution.circularArrayLoop_dfs(nums.copy()) is False
    assert solution.circularArrayLoop(nums.copy()) is False

def test_circularArrayLoop_cycle_length_one(solution):
    nums = [1, 1, 1, 1]
    assert solution.circularArrayLoop_dfs(nums.copy()) is True
    assert solution.circularArrayLoop(nums.copy()) is True
