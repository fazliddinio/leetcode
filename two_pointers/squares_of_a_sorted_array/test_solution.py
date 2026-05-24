import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_sortedSquares_example1(solution):
    nums = [-4, -1, 0, 3, 10]
    expected = [0, 1, 9, 16, 100]
    assert solution.sortedSquares(nums) == expected
    assert solution.sortedSquares_sort(nums) == expected

def test_sortedSquares_example2(solution):
    nums = [-7, -3, 2, 3, 11]
    expected = [4, 9, 9, 49, 121]
    assert solution.sortedSquares(nums) == expected
    assert solution.sortedSquares_sort(nums) == expected

def test_sortedSquares_all_negative(solution):
    nums = [-5, -3, -1]
    expected = [1, 9, 25]
    assert solution.sortedSquares(nums) == expected
    assert solution.sortedSquares_sort(nums) == expected

def test_sortedSquares_all_positive(solution):
    nums = [1, 2, 3]
    expected = [1, 4, 9]
    assert solution.sortedSquares(nums) == expected
    assert solution.sortedSquares_sort(nums) == expected
