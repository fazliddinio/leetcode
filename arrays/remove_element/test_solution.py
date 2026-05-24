import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_removeElement_example1(solution):
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement(nums, val)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]

def test_removeElement_swap_example1(solution):
    nums = [3, 2, 2, 3]
    val = 3
    k = solution.removeElement_swap(nums, val)
    assert k == 2
    assert sorted(nums[:k]) == [2, 2]

def test_removeElement_example2(solution):
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = solution.removeElement(nums, val)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

def test_removeElement_swap_example2(solution):
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    k = solution.removeElement_swap(nums, val)
    assert k == 5
    assert sorted(nums[:k]) == [0, 0, 1, 3, 4]

def test_removeElement_empty(solution):
    nums = []
    val = 0
    k = solution.removeElement(nums, val)
    assert k == 0
    assert nums[:k] == []

def test_removeElement_swap_empty(solution):
    nums = []
    val = 0
    k = solution.removeElement_swap(nums, val)
    assert k == 0
    assert nums[:k] == []
