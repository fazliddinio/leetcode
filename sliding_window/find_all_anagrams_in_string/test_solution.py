import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findAnagrams_example1(solution):
    s = "cbaebabacd"
    p = "abc"
    expected = [0, 6]
    assert solution.findAnagrams(s, p) == expected
    assert solution.findAnagrams_hash(s, p) == expected

def test_findAnagrams_example2(solution):
    s = "abab"
    p = "ab"
    expected = [0, 1, 2]
    assert solution.findAnagrams(s, p) == expected
    assert solution.findAnagrams_hash(s, p) == expected

def test_findAnagrams_p_longer(solution):
    s = "a"
    p = "ab"
    assert solution.findAnagrams(s, p) == []
    assert solution.findAnagrams_hash(s, p) == []
    
def test_findAnagrams_empty(solution):
    s = ""
    p = "a"
    assert solution.findAnagrams(s, p) == []
    assert solution.findAnagrams_hash(s, p) == []
