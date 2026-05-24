import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_totalFruit_example1(solution):
    fruits = [1, 2, 1]
    assert solution.totalFruit(fruits) == 3
    assert solution.totalFruit_brute(fruits) == 3

def test_totalFruit_example2(solution):
    fruits = [0, 1, 2, 2]
    assert solution.totalFruit(fruits) == 3
    assert solution.totalFruit_brute(fruits) == 3

def test_totalFruit_example3(solution):
    fruits = [1, 2, 3, 2, 2]
    assert solution.totalFruit(fruits) == 4
    assert solution.totalFruit_brute(fruits) == 4

def test_totalFruit_example4(solution):
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    assert solution.totalFruit(fruits) == 5
    assert solution.totalFruit_brute(fruits) == 5
