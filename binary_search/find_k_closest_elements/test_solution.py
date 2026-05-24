import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findClosestElements_example1(solution):
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 3
    assert solution.findClosestElements(arr, k, x) == [1, 2, 3, 4]
    assert solution.findClosestElements_sort(arr, k, x) == [1, 2, 3, 4]

def test_findClosestElements_example2(solution):
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = -1
    assert solution.findClosestElements(arr, k, x) == [1, 2, 3, 4]
    assert solution.findClosestElements_sort(arr, k, x) == [1, 2, 3, 4]

def test_findClosestElements_out_of_bounds_right(solution):
    arr = [1, 2, 3, 4, 5]
    k = 4
    x = 6
    assert solution.findClosestElements(arr, k, x) == [2, 3, 4, 5]
    assert solution.findClosestElements_sort(arr, k, x) == [2, 3, 4, 5]
