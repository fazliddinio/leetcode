import pytest
import solution
from solution import Solution

@pytest.fixture
def test_solution():
    return Solution()

def set_bad_version(bad):
    solution._BAD_VERSION = bad

def test_firstBadVersion_example1(test_solution):
    set_bad_version(4)
    n = 5
    assert test_solution.firstBadVersion(n) == 4
    assert test_solution.firstBadVersion_linear(n) == 4

def test_firstBadVersion_example2(test_solution):
    set_bad_version(1)
    n = 1
    assert test_solution.firstBadVersion(n) == 1
    assert test_solution.firstBadVersion_linear(n) == 1

def test_firstBadVersion_last(test_solution):
    set_bad_version(10)
    n = 10
    assert test_solution.firstBadVersion(n) == 10
    assert test_solution.firstBadVersion_linear(n) == 10
