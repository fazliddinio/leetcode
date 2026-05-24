import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_searchMatrix_example1(solution):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 3
    assert solution.searchMatrix(matrix, target) is True
    assert solution.searchMatrix_step(matrix, target) is True

def test_searchMatrix_example2(solution):
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 13
    assert solution.searchMatrix(matrix, target) is False
    assert solution.searchMatrix_step(matrix, target) is False

def test_searchMatrix_single(solution):
    matrix = [[5]]
    target = 5
    assert solution.searchMatrix(matrix, target) is True
    assert solution.searchMatrix_step(matrix, target) is True

def test_searchMatrix_empty(solution):
    matrix = []
    target = 1
    assert solution.searchMatrix(matrix, target) is False
    assert solution.searchMatrix_step(matrix, target) is False
