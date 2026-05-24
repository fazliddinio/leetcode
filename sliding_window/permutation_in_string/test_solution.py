import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_checkInclusion_example1(solution):
    s1 = "ab"
    s2 = "eidbaooo"
    assert solution.checkInclusion(s1, s2) is True
    assert solution.checkInclusion_hash(s1, s2) is True

def test_checkInclusion_example2(solution):
    s1 = "ab"
    s2 = "eidboaoo"
    assert solution.checkInclusion(s1, s2) is False
    assert solution.checkInclusion_hash(s1, s2) is False

def test_checkInclusion_exact_match(solution):
    s1 = "abc"
    s2 = "bca"
    assert solution.checkInclusion(s1, s2) is True
    assert solution.checkInclusion_hash(s1, s2) is True

def test_checkInclusion_longer_s1(solution):
    s1 = "abcd"
    s2 = "abc"
    assert solution.checkInclusion(s1, s2) is False
    assert solution.checkInclusion_hash(s1, s2) is False
