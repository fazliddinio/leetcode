import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findSubstring_example1(solution):
    s = "barfoothefoobarman"
    words = ["foo", "bar"]
    expected = [0, 9]
    assert sorted(solution.findSubstring(s, words)) == expected
    assert sorted(solution.findSubstring_brute(s, words)) == expected

def test_findSubstring_example2(solution):
    s = "wordgoodgoodgoodbestword"
    words = ["word", "good", "best", "word"]
    expected = []
    assert sorted(solution.findSubstring(s, words)) == expected
    assert sorted(solution.findSubstring_brute(s, words)) == expected

def test_findSubstring_example3(solution):
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    expected = [6, 9, 12]
    assert sorted(solution.findSubstring(s, words)) == expected
    assert sorted(solution.findSubstring_brute(s, words)) == expected
