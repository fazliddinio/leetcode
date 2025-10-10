import pytest
from .solution import Solution

def test_is_valid():
    s = Solution()
    assert s.isValid("()") == True
    assert s.isValid("()[]{}") == True
    assert s.isValid("(]") == False
    assert s.isValid("([)]") == False
