import pytest
from .solution import Solution, SolutionBruteForce, SolutionMap

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionMap])
@pytest.mark.parametrize(
    "s, expected",
    [
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        ("", 0),
        (" ", 1),
    ],
)
def test_length_of_longest_substring(SolutionClass, s, expected):
    solution = SolutionClass()
    assert solution.lengthOfLongestSubstring(s) == expected
