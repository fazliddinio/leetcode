import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_maxSatisfied_example1(solution):
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    assert solution.maxSatisfied(customers, grumpy, minutes) == 16
    assert solution.maxSatisfied_brute(customers, grumpy, minutes) == 16

def test_maxSatisfied_example2(solution):
    customers = [1]
    grumpy = [0]
    minutes = 1
    assert solution.maxSatisfied(customers, grumpy, minutes) == 1
    assert solution.maxSatisfied_brute(customers, grumpy, minutes) == 1

def test_maxSatisfied_all_grumpy(solution):
    customers = [4, 1, 2, 3]
    grumpy = [1, 1, 1, 1]
    minutes = 2
    assert solution.maxSatisfied(customers, grumpy, minutes) == 5
    assert solution.maxSatisfied_brute(customers, grumpy, minutes) == 5

def test_maxSatisfied_no_grumpy(solution):
    customers = [4, 1, 2, 3]
    grumpy = [0, 0, 0, 0]
    minutes = 2
    assert solution.maxSatisfied(customers, grumpy, minutes) == 10
    assert solution.maxSatisfied_brute(customers, grumpy, minutes) == 10
