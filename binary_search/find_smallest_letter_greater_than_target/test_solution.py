import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_nextGreatestLetter_example1(solution):
    letters = ["c", "f", "j"]
    target = "a"
    assert solution.nextGreatestLetter(letters, target) == "c"
    assert solution.nextGreatestLetter_linear(letters, target) == "c"

def test_nextGreatestLetter_example2(solution):
    letters = ["c", "f", "j"]
    target = "c"
    assert solution.nextGreatestLetter(letters, target) == "f"
    assert solution.nextGreatestLetter_linear(letters, target) == "f"

def test_nextGreatestLetter_example3(solution):
    letters = ["x", "x", "y", "y"]
    target = "z"
    assert solution.nextGreatestLetter(letters, target) == "x"
    assert solution.nextGreatestLetter_linear(letters, target) == "x"

def test_nextGreatestLetter_wrap(solution):
    letters = ["c", "f", "j"]
    target = "j"
    assert solution.nextGreatestLetter(letters, target) == "c"
    assert solution.nextGreatestLetter_linear(letters, target) == "c"
