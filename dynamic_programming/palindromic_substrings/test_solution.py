import pytest
from .solution import Solution

def test_count_substrings():
    s = Solution()
    assert s.countSubstrings("abc") == 3
    assert s.countSubstrings("aaa") == 6
