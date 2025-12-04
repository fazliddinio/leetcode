"""
# Maximum Average Subarray I

## Problem Description
You are given an integer array `nums` consisting of `n` elements, and an integer `k`.
Find a contiguous subarray whose length is equal to `k` that has the maximum average value and return this value.

## Approaches
1.  **Brute Force**: Calculate the sum of every subarray of length `k`.
    *   Time Complexity: O(n * k)
    *   Space Complexity: O(1)
2.  **Sliding Window** (Optimal): Maintain a running sum of the current window.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Sliding Window
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Finds maximum average subarray of length k.
        
        Args:
            nums: List of integers.
            k: Length of subarray.
            
        Returns:
            Max average value.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
            
        return max_sum / k

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Finds max average using brute force.
        
        Time Complexity: O(n * k)
        Space Complexity: O(1)
        """
        max_sum = float('-inf')
        n = len(nums)
        # Scan all windows of size k
        for i in range(n - k + 1):
            current_sum = 0
            for j in range(i, i + k):
                current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
        return max_sum / k
