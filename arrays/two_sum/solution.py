"""
# Two Sum

## Problem Description
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

## Approaches
1.  **Brute Force**: Check every pair of numbers.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Two-Pass Hash Table**: Create a map of value->index, then iterate to find complement.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
3.  **One-Pass Hash Table** (Optimal): Iterate once, checking for complement in the map before adding the current number.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
4.  **Sorting + Two Pointers** (Alternative): Sort the array and use two pointers. Note: This requires tracking original indices, which adds complexity/space.
    *   Time Complexity: O(n log n)
    *   Space Complexity: O(n)
"""

from typing import List, Dict, Tuple

class Solution:
    """
    Optimal Solution: One-Pass Hash Table
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two indices such that the numbers at these indices add up to the target.

        Args:
            nums: A list of integers.
            target: The target sum.

        Returns:
            A list containing the two indices [index1, index2]. Returns an empty list if no solution is found.

        Time Complexity: O(n) - We iterate through the list once.
        Space Complexity: O(n) - We store elements in a hash map.
        """
        num_to_index: Dict[int, int] = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_to_index:
                return [num_to_index[complement], i]
            num_to_index[num] = i
        return []

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two indices using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

class SolutionAlternative:
    """
    Alternative Solution: Sorting + Two Pointers
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two indices by sorting first.
        
        Time Complexity: O(n log n) - Sorting dominates.
        Space Complexity: O(n) - To store the original indices.
        """
        # Store original indices: [(val, index), ...]
        indexed_nums: List[Tuple[int, int]] = []
        for i, num in enumerate(nums):
            indexed_nums.append((num, i))
            
        # Sort based on values
        indexed_nums.sort(key=lambda x: x[0])
        
        l, r = 0, len(nums) - 1
        while l < r:
            current_sum = indexed_nums[l][0] + indexed_nums[r][0]
            if current_sum == target:
                return [indexed_nums[l][1], indexed_nums[r][1]]
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        return []