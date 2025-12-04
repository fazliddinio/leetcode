import pytest
from .solution import Solution, SolutionSorting, SolutionHeap

@pytest.mark.parametrize("SolutionClass", [Solution, SolutionSorting, SolutionHeap])
@pytest.mark.parametrize(
    "nums, k, expected",
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([-1, -1], 1, [-1]),
    ],
)
def test_top_k_frequent(SolutionClass, nums, k, expected):
    solution = SolutionClass()
    result = solution.topKFrequent(nums, k)
    # Order doesn't matter
    assert sorted(result) == sorted(expected)
