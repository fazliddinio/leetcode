import pytest
from .solution import Solution

def test_reverse_string():
    s = Solution()
    chars = ["h","e","l","l","o"]
    s.reverseString(chars)
    assert chars == ["o","l","l","e","h"]
    
    chars = ["H","a","n","n","a","h"]
    s.reverseString(chars)
    assert chars == ["h","a","n","n","a","H"]
