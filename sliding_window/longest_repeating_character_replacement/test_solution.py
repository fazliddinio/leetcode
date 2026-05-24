import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_characterReplacement_example1(solution):
    s = "ABAB"
    k = 2
    assert solution.characterReplacement(s, k) == 4
    assert solution.characterReplacement_strict(s, k) == 4

def test_characterReplacement_example2(solution):
    s = "AABABBA"
    k = 1
    assert solution.characterReplacement(s, k) == 4
    assert solution.characterReplacement_strict(s, k) == 4

def test_characterReplacement_k_zero(solution):
    s = "AABBAABAB"
    k = 0
    assert solution.characterReplacement(s, k) == 2
    assert solution.characterReplacement_strict(s, k) == 2

def test_characterReplacement_all_same(solution):
    s = "AAAA"
    k = 2
    assert solution.characterReplacement(s, k) == 4
    assert solution.characterReplacement_strict(s, k) == 4
