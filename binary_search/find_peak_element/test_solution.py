import pytest
from solution import Solution

@pytest.fixture
def solution():
    return Solution()

def test_findPeakElement_example1(solution):
    nums = [1, 2, 3, 1]
    # Any peak is valid. At index 2, nums[2] == 3.
    assert solution.findPeakElement(nums) == 2
    assert solution.findPeakElement_linear(nums) == 2

def test_findPeakElement_example2(solution):
    nums = [1, 2, 1, 3, 5, 6, 4]
    ans1 = solution.findPeakElement(nums)
    ans2 = solution.findPeakElement_linear(nums)
    valid_peaks = {1, 5}
    assert ans1 in valid_peaks
    assert ans2 in valid_peaks

def test_findPeakElement_increasing(solution):
    nums = [1, 2, 3]
    assert solution.findPeakElement(nums) == 2
    assert solution.findPeakElement_linear(nums) == 2

def test_findPeakElement_single(solution):
    nums = [4]
    assert solution.findPeakElement(nums) == 0
    assert solution.findPeakElement_linear(nums) == 0
