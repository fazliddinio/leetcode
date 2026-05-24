import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_min_knight_moves_example1(solution):
    assert solution.minKnightMoves(2, 1) == 1

def test_min_knight_moves_example2(solution):
    assert solution.minKnightMoves(5, 5) == 4

def test_min_knight_moves_origin(solution):
    assert solution.minKnightMoves(0, 0) == 0

def test_min_knight_moves_one_one(solution):
    assert solution.minKnightMoves(1, 1) == 2

def test_min_knight_moves_negative(solution):
    assert solution.minKnightMoves(-2, -1) == 1

def test_min_knight_moves_bidirectional_example1(solution):
    assert solution.minKnightMoves_bidirectional(2, 1) == 1

def test_min_knight_moves_bidirectional_example2(solution):
    assert solution.minKnightMoves_bidirectional(5, 5) == 4

def test_min_knight_moves_bidirectional_origin(solution):
    assert solution.minKnightMoves_bidirectional(0, 0) == 0
