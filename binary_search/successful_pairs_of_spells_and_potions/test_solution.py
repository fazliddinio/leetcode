import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_successfulPairs_example1(solution):
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    expected = [4, 0, 3]
    assert solution.successfulPairs(spells, potions, success) == expected
    assert solution.successfulPairs_two_pointers(spells, potions, success) == expected

def test_successfulPairs_example2(solution):
    spells = [3, 1, 2]
    potions = [8, 5, 8]
    success = 16
    expected = [2, 0, 2]
    assert solution.successfulPairs(spells, potions, success) == expected
    assert solution.successfulPairs_two_pointers(spells, potions, success) == expected

def test_successfulPairs_all_success(solution):
    spells = [10, 20]
    potions = [1, 2, 3]
    success = 5
    expected = [3, 3]
    assert solution.successfulPairs(spells, potions, success) == expected
    assert solution.successfulPairs_two_pointers(spells, potions, success) == expected

def test_successfulPairs_none_success(solution):
    spells = [1, 2]
    potions = [1, 2]
    success = 10
    expected = [0, 0]
    assert solution.successfulPairs(spells, potions, success) == expected
    assert solution.successfulPairs_two_pointers(spells, potions, success) == expected
