import pytest
from .solution import Solution

def test_is_happy():
    s = Solution()
    assert s.isHappy(19) == True
    assert s.isHappy(2) == False
