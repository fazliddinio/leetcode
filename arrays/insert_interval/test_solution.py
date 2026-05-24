import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_insert_example1(solution):
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    assert solution.insert(intervals, newInterval) == [[1, 5], [6, 9]]

def test_insert_example2(solution):
    intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    newInterval = [4, 8]
    assert solution.insert(intervals, newInterval) == [[1, 2], [3, 10], [12, 16]]

def test_insert_no_overlap_before(solution):
    intervals = [[3, 5], [6, 9]]
    newInterval = [1, 2]
    assert solution.insert(intervals, newInterval) == [[1, 2], [3, 5], [6, 9]]

def test_insert_no_overlap_after(solution):
    intervals = [[1, 2], [3, 5]]
    newInterval = [6, 8]
    assert solution.insert(intervals, newInterval) == [[1, 2], [3, 5], [6, 8]]

def test_insert_empty_intervals(solution):
    intervals = []
    newInterval = [5, 7]
    assert solution.insert(intervals, newInterval) == [[5, 7]]

def test_insert_brute_example1(solution):
    intervals = [[1, 3], [6, 9]]
    newInterval = [2, 5]
    assert solution.insert_brute(intervals, newInterval) == [[1, 5], [6, 9]]
