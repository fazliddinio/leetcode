import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_minWindow_example1(solution):
    s = "ADOBECODEBANC"
    t = "ABC"
    assert solution.minWindow(s, t) == "BANC"
    assert solution.minWindow_filtered(s, t) == "BANC"

def test_minWindow_example2(solution):
    s = "a"
    t = "a"
    assert solution.minWindow(s, t) == "a"
    assert solution.minWindow_filtered(s, t) == "a"

def test_minWindow_example3(solution):
    s = "a"
    t = "aa"
    assert solution.minWindow(s, t) == ""
    assert solution.minWindow_filtered(s, t) == ""

def test_minWindow_empty(solution):
    assert solution.minWindow("", "A") == ""
    assert solution.minWindow_filtered("", "A") == ""
    
def test_minWindow_notFound(solution):
    assert solution.minWindow("ABC", "Z") == ""
    assert solution.minWindow_filtered("ABC", "Z") == ""
