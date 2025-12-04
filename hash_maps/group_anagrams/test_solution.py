import pytest
from .solution import Solution, SolutionSorting

def sort_result(result):
    """Helper to sort the result (list of lists) deeply for comparison."""
    # First sort each inner list
    inner_sorted = [sorted(group) for group in result]
    # Then sort the outer list based on the first element of each inner list (or some canonical representation)
    # Since inputs are strings, we can join them or sort by length then content.
    # Easiest: sort by the sorted tuple of the group
    inner_sorted.sort(key=lambda x: (len(x), x))
    return inner_sorted

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionSorting])
@pytest.mark.parametrize(
    "strs, expected",
    [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
    ],
)
def test_group_anagrams(SolutionClass, strs, expected):
    solution = SolutionClass()
    result = solution.groupAnagrams(strs)
    assert sort_result(result) == sort_result(expected)
