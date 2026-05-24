import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_trap_example1(solution):
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    assert solution.trap(height) == 6
    assert solution.trap_dp(height) == 6

def test_trap_example2(solution):
    height = [4,2,0,3,2,5]
    assert solution.trap(height) == 9
    assert solution.trap_dp(height) == 9

def test_trap_empty(solution):
    assert solution.trap([]) == 0
    assert solution.trap_dp([]) == 0

def test_trap_no_trapping(solution):
    height = [3, 2, 1, 2, 3]
    assert solution.trap(height) == 4
    assert solution.trap_dp(height) == 4
