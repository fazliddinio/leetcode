import pytest
from .solution import Solution, SolutionBruteForce, SolutionAlternative

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionBruteForce, SolutionAlternative])
@pytest.mark.parametrize(
    "s, expected",
    [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("", -1),
        ("z", 0),
    ],
)
def test_first_uniq_char(SolutionClass, s, expected):
    solution = SolutionClass()
    assert solution.firstUniqChar(s) == expected
