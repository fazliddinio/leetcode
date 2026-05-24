import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_lengthOfLongestSubstring_example1(solution):
    s = "abcabcbb"
    assert solution.lengthOfLongestSubstring(s) == 3
    assert solution.lengthOfLongestSubstring_set(s) == 3

def test_lengthOfLongestSubstring_example2(solution):
    s = "bbbbb"
    assert solution.lengthOfLongestSubstring(s) == 1
    assert solution.lengthOfLongestSubstring_set(s) == 1

def test_lengthOfLongestSubstring_example3(solution):
    s = "pwwkew"
    assert solution.lengthOfLongestSubstring(s) == 3
    assert solution.lengthOfLongestSubstring_set(s) == 3

def test_lengthOfLongestSubstring_empty(solution):
    s = ""
    assert solution.lengthOfLongestSubstring(s) == 0
    assert solution.lengthOfLongestSubstring_set(s) == 0
