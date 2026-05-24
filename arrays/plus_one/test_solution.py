import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_plusOne_example1(solution):
    digits = [1, 2, 3]
    assert solution.plusOne(digits.copy()) == [1, 2, 4]
    assert solution.plusOne_string(digits.copy()) == [1, 2, 4]

def test_plusOne_example2(solution):
    digits = [4, 3, 2, 1]
    assert solution.plusOne(digits.copy()) == [4, 3, 2, 2]
    assert solution.plusOne_string(digits.copy()) == [4, 3, 2, 2]

def test_plusOne_example3(solution):
    digits = [9]
    assert solution.plusOne(digits.copy()) == [1, 0]
    assert solution.plusOne_string(digits.copy()) == [1, 0]

def test_plusOne_all_nines(solution):
    digits = [9, 9, 9]
    assert solution.plusOne(digits.copy()) == [1, 0, 0, 0]
    assert solution.plusOne_string(digits.copy()) == [1, 0, 0, 0]
