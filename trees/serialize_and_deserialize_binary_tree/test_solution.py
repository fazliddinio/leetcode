import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_dummy(solution):
    pass
