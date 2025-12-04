import pytest
from .solution import Solution, SolutionSorting

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionSorting])
@pytest.mark.parametrize(
    "s1, s2, expected",
    [
        ("ab", "eidbaooo", True),
        ("ab", "eidboaoo", False),
        ("adc", "dcda", True),
    ],
)
def test_check_inclusion(SolutionClass, s1, s2, expected):
    solution = SolutionClass()
    assert solution.checkInclusion(s1, s2) == expected
