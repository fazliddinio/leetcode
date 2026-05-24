import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_shortest_path_example1(solution):
    grid = [[0, 1], [1, 0]]
    assert solution.shortestPathBinaryMatrix(grid) == 2

def test_shortest_path_example2(solution):
    grid = [[0, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert solution.shortestPathBinaryMatrix(grid) == 4

def test_shortest_path_blocked_start(solution):
    grid = [[1, 0, 0], [1, 1, 0], [1, 1, 0]]
    assert solution.shortestPathBinaryMatrix(grid) == -1

def test_shortest_path_single_cell(solution):
    grid = [[0]]
    assert solution.shortestPathBinaryMatrix(grid) == 1

def test_shortest_path_no_path(solution):
    grid = [[0, 1, 1], [1, 1, 1], [1, 1, 0]]
    assert solution.shortestPathBinaryMatrix(grid) == -1

def test_shortest_path_straight_diagonal(solution):
    grid = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    assert solution.shortestPathBinaryMatrix(grid) == 3
