import pytest
from .solution import Solution, SolutionBruteForce

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce])
@pytest.mark.parametrize(
    "s, k, expected",
    [
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("A", 0, 1),
    ],
)
def test_character_replacement(SolutionClass, s, k, expected):
    solution = SolutionClass()
    assert solution.characterReplacement(s, k) == expected
