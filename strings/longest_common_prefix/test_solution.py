import pytest
from .solution import Solution, SolutionVertical, SolutionSorting

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionVertical, SolutionSorting])
@pytest.mark.parametrize(
    "strs, expected",
    [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["ab", "a"], "a"),
        (["a"], "a"),
        ([], ""),
    ],
)
def test_longest_common_prefix(SolutionClass, strs, expected):
    solution = SolutionClass()
    # SolutionSorting modifies the input list with sort(), so we should copy
    strs_copy = list(strs)
    assert solution.longestCommonPrefix(strs_copy) == expected
