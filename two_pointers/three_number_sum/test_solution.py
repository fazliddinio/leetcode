import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_threeNumberSum_example1(solution):
    arr = [12, 3, 1, 2, -6, 5, -8, 6]
    target = 0
    expected = [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]
    
    assert sorted([sorted(x) for x in solution.threeNumberSum(arr.copy(), target)]) == sorted([sorted(x) for x in expected])
    assert sorted([sorted(x) for x in solution.threeNumberSum_hash(arr.copy(), target)]) == sorted([sorted(x) for x in expected])

def test_threeNumberSum_example2(solution):
    arr = [1, 2, 3]
    target = 6
    expected = [[1, 2, 3]]
    
    assert sorted([sorted(x) for x in solution.threeNumberSum(arr.copy(), target)]) == sorted([sorted(x) for x in expected])
    assert sorted([sorted(x) for x in solution.threeNumberSum_hash(arr.copy(), target)]) == sorted([sorted(x) for x in expected])

def test_threeNumberSum_no_sum(solution):
    arr = [1, 2, 3]
    target = 7
    expected = []
    
    assert solution.threeNumberSum(arr.copy(), target) == expected
    assert solution.threeNumberSum_hash(arr.copy(), target) == expected
