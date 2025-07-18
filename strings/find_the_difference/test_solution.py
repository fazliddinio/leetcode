import pytest
from .solution import Solution

def test_find_the_difference():
    s = Solution()
    assert s.findTheDifference("abcd", "abcde") == "e"
    assert s.findTheDifference("", "y") == "y"
