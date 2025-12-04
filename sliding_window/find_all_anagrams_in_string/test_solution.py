import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "s, p, expected",
    [
        ("cbaebabacd", "abc", [0, 6]),
        ("abab", "ab", [0, 1, 2]),
        ("a", "b", []),
    ],
)
def test_find_anagrams(SolutionClass, s, p, expected):
    solution = SolutionClass()
    assert solution.findAnagrams(s, p) == expected
