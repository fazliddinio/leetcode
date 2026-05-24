import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_maxSlidingWindow_example1(solution):
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    expected = [3, 3, 5, 5, 6, 7]
    assert solution.maxSlidingWindow(nums, k) == expected
    assert solution.maxSlidingWindow_dp(nums, k) == expected

def test_maxSlidingWindow_example2(solution):
    nums = [1]
    k = 1
    expected = [1]
    assert solution.maxSlidingWindow(nums, k) == expected
    assert solution.maxSlidingWindow_dp(nums, k) == expected

def test_maxSlidingWindow_k_is_two(solution):
    nums = [7, 2, 4]
    k = 2
    expected = [7, 4]
    assert solution.maxSlidingWindow(nums, k) == expected
    assert solution.maxSlidingWindow_dp(nums, k) == expected
