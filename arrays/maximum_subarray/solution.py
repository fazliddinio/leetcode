"""
# Maximum Subarray

## Problem Description
Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

## Approaches
1.  **Brute Force**: Calculate sum of every possible subarray.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Divide and Conquer** (Alternative): Divide the array into two halves, recursively find the max subarray sum in left, right, and crossing mid.
    *   Time Complexity: O(n log n)
    *   Space Complexity: O(log n) stack space.
3.  **Kadane's Algorithm** (Optimal): Iterate through the array keeping track of max sum ending at current position.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Kadane's Algorithm
    """
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds the contiguous subarray which has the largest sum.

        Args:
            nums: A list of integers.

        Returns:
            The sum of the maximum subarray.

        Time Complexity: O(n) - We iterate through the array once.
        Space Complexity: O(1) - Constant extra space used.
        """
        max_subarray_sum = nums[0]
        current_sum = 0
        
        for num in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += num
            max_subarray_sum = max(max_subarray_sum, current_sum)
            
        return max_subarray_sum

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds max subarray sum using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        max_sum = float('-inf')
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                max_sum = max(max_sum, current_sum)
        return int(max_sum)

class SolutionAlternative:
    """
    Alternative Solution: Divide and Conquer
    """
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Finds max subarray sum using divide and conquer.
        
        Time Complexity: O(n log n)
        Space Complexity: O(log n) recursive stack
        """
        def solve(l, r):
            if l > r:
                return float('-inf')
            mid = (l + r) // 2
            
            curr = 0
            left_max = 0
            for i in range(mid - 1, l - 1, -1):
                curr += nums[i]
                left_max = max(left_max, curr)
                
            curr = 0
            right_max = 0
            for i in range(mid + 1, r + 1):
                curr += nums[i]
                right_max = max(right_max, curr)
                
            res = left_max + nums[mid] + right_max
            
            left_res = solve(l, mid - 1)
            right_res = solve(mid + 1, r)
            
            return max(res, left_res, right_res)
            
        return int(solve(0, len(nums) - 1))