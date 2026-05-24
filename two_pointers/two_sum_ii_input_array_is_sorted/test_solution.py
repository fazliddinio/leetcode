import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_twoSum_example1(solution):
    numbers = [2, 7, 11, 15]
    target = 9
    assert solution.twoSum(numbers, target) == [1, 2]
    assert solution.twoSum_binary_search(numbers, target) == [1, 2]

def test_twoSum_example2(solution):
    numbers = [2, 3, 4]
    target = 6
    assert solution.twoSum(numbers, target) == [1, 3]
    assert solution.twoSum_binary_search(numbers, target) == [1, 3]

def test_twoSum_example3(solution):
    numbers = [-1, 0]
    target = -1
    assert solution.twoSum(numbers, target) == [1, 2]
    assert solution.twoSum_binary_search(numbers, target) == [1, 2]
    
def test_twoSum_not_found(solution):
    numbers = [1, 2, 3]
    target = 10
    assert solution.twoSum(numbers, target) == []
    assert solution.twoSum_binary_search(numbers, target) == []
