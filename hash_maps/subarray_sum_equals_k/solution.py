"""
# Subarray Sum Equals K

## Problem Description
Given an array of integers `nums` and an integer `k`, return the total number of subarrays whose sum equals to `k`.
A subarray is a contiguous non-empty sequence of elements within an array.

## Approaches
1.  **Brute Force** / **Cumulative Sum array**: Calculate all subarray sums.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1) or O(n) used for cumulative sum array.
2.  **Hash Map** (Optimal): Use a hash table to store the frequency of prefix sums.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import List, Dict

class Solution:
    """
    Optimal Solution: Prefix Sum Hash Map
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Finds the total number of continuous subarrays whose sum equals to k.
        
        Args:
            nums: A list of integers.
            k: The target sum.
        
        Returns:
            The number of subarrays that sum to k.
        
        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(n) - Hash map to store prefix sums.
        """
        count = 0
        current_sum = 0
        prefix_sums: Dict[int, int] = {0: 1}
        
        for num in nums:
            current_sum += num
            diff = current_sum - k
            
            count += prefix_sums.get(diff, 0)
            prefix_sums[current_sum] = 1 + prefix_sums.get(current_sum, 0)
            
        return count

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Finds subarray sum using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        count = 0
        n = len(nums)
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]
                if current_sum == k:
                    count += 1
        return count