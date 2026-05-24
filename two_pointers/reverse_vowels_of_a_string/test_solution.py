import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_reverseVowels_example1(solution):
    s = "hello"
    assert solution.reverseVowels(s) == "holle"
    assert solution.reverseVowels_stack(s) == "holle"

def test_reverseVowels_example2(solution):
    s = "leetcode"
    assert solution.reverseVowels(s) == "leotcede"
    assert solution.reverseVowels_stack(s) == "leotcede"

def test_reverseVowels_no_vowels(solution):
    s = "xyz"
    assert solution.reverseVowels(s) == "xyz"
    assert solution.reverseVowels_stack(s) == "xyz"

def test_reverseVowels_all_vowels(solution):
    s = "aeiou"
    assert solution.reverseVowels(s) == "uoiea"
    assert solution.reverseVowels_stack(s) == "uoiea"

def test_reverseVowels_empty(solution):
    s = ""
    assert solution.reverseVowels(s) == ""
    assert solution.reverseVowels_stack(s) == ""
