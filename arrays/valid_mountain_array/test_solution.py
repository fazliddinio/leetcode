import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_validMountainArray_example1(solution):
    arr = [2, 1]
    assert solution.validMountainArray(arr) is False
    assert solution.validMountainArray_two_pointers(arr) is False

def test_validMountainArray_example2(solution):
    arr = [3, 5, 5]
    assert solution.validMountainArray(arr) is False
    assert solution.validMountainArray_two_pointers(arr) is False

def test_validMountainArray_example3(solution):
    arr = [0, 3, 2, 1]
    assert solution.validMountainArray(arr) is True
    assert solution.validMountainArray_two_pointers(arr) is True

def test_validMountainArray_only_up(solution):
    arr = [1, 2, 3, 4]
    assert solution.validMountainArray(arr) is False
    assert solution.validMountainArray_two_pointers(arr) is False

def test_validMountainArray_only_down(solution):
    arr = [4, 3, 2, 1]
    assert solution.validMountainArray(arr) is False
    assert solution.validMountainArray_two_pointers(arr) is False

def test_validMountainArray_plateau(solution):
    arr = [0, 3, 3, 2, 1]
    assert solution.validMountainArray(arr) is False
    assert solution.validMountainArray_two_pointers(arr) is False
