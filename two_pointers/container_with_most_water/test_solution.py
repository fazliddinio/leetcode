import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_maxArea_example1(solution):
    height = [1,8,6,2,5,4,8,3,7]
    assert solution.maxArea(height) == 49
    assert solution.maxArea_brute(height) == 49

def test_maxArea_example2(solution):
    height = [1,1]
    assert solution.maxArea(height) == 1
    assert solution.maxArea_brute(height) == 1

def test_maxArea_decreasing(solution):
    height = [5,4,3,2,1]
    assert solution.maxArea(height) == 6
    assert solution.maxArea_brute(height) == 6

def test_maxArea_increasing(solution):
    height = [1,2,3,4,5]
    assert solution.maxArea(height) == 6
    assert solution.maxArea_brute(height) == 6
