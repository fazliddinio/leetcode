import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_generate_example1(solution):
    numRows = 5
    expected = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    assert solution.generate(numRows) == expected
    assert solution.generate_recursive(numRows) == expected

def test_generate_example2(solution):
    numRows = 1
    expected = [[1]]
    assert solution.generate(numRows) == expected
    assert solution.generate_recursive(numRows) == expected

def test_generate_zero(solution):
    assert solution.generate(0) == []
    assert solution.generate_recursive(0) == []

def test_generate_three(solution):
    numRows = 3
    expected = [[1], [1, 1], [1, 2, 1]]
    assert solution.generate(numRows) == expected
    assert solution.generate_recursive(numRows) == expected
