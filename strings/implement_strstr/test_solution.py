import pytest
from .solution import Solution

def test_str_str():
    s = Solution()
    assert s.strStr("sadbutsad", "sad") == 0
    assert s.strStr("leetcode", "leeto") == -1
    assert s.strStr("hello", "") == 0
