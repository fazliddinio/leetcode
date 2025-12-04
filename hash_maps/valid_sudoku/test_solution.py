import pytest
from .solution import Solution, SolutionMultiPass

@pytest.fixture
def valid_board():
    return [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

@pytest.fixture
def invalid_board_row():
    return [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionMultiPass])
def test_valid_sudoku(SolutionClass, valid_board):
    solution = SolutionClass()
    assert solution.isValidSudoku(valid_board) == True

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionMultiPass])
def test_invalid_sudoku(SolutionClass, invalid_board_row):
    solution = SolutionClass()
    assert solution.isValidSudoku(invalid_board_row) == False
