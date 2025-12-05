import pytest
from .solution import Solution

def test_longest_palindrome():
    s = Solution()
    assert s.longestPalindrome("babad") in ["bab", "aba"]
    assert s.longestPalindrome("cbbd") == "bb"
