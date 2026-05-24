import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_lengthOfLongestSubstringKDistinct_example1(solution):
    s = "eceba"
    k = 2
    assert solution.lengthOfLongestSubstringKDistinct(s, k) == 3
    assert solution.lengthOfLongestSubstringKDistinct_ordered(s, k) == 3

def test_lengthOfLongestSubstringKDistinct_example2(solution):
    s = "aa"
    k = 1
    assert solution.lengthOfLongestSubstringKDistinct(s, k) == 2
    assert solution.lengthOfLongestSubstringKDistinct_ordered(s, k) == 2

def test_lengthOfLongestSubstringKDistinct_k_zero(solution):
    s = "eceba"
    k = 0
    assert solution.lengthOfLongestSubstringKDistinct(s, k) == 0
    assert solution.lengthOfLongestSubstringKDistinct_ordered(s, k) == 0

def test_lengthOfLongestSubstringKDistinct_long(solution):
    s = "abaccc"
    k = 2
    assert solution.lengthOfLongestSubstringKDistinct(s, k) == 4
    assert solution.lengthOfLongestSubstringKDistinct_ordered(s, k) == 4
