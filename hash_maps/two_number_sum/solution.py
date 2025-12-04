"""
# Two Number Sum

## Problem Description
Finds two numbers in the input array that sum up to the target value.

## Approaches
1.  **Brute Force**: Check every pair.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Sorting** (Alternative): Sort and use two pointers.
    *   Time Complexity: O(n log n)
    *   Space Complexity: O(n) (to store indices or sort overhead)
3.  **Hash Table** (Optimal): Use a hash map to store seen numbers.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import List, Dict, Tuple

class Solution:
    """
    Optimal Solution: Hash Table
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two numbers in the input array that sum up to the target value.
        
        Args:
            nums: A list of integers.
            target: The target integer sum.
            
        Returns:
            A list containing the indices of the two numbers.
            Returns an empty list if no such pair exists.
            
        Time Complexity: O(n) - Single pass through the array.
        Space Complexity: O(n) - Hash map to store seen numbers and their indices.
        """
        seen: Dict[int, int] = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two sum using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

class SolutionSorting:
    """
    Alternative Solution: Sorting
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds two sum by sorting first.
        
        Time Complexity: O(n log n)
        Space Complexity: O(n)
        """
        indexed_nums = []
        for i, num in enumerate(nums):
            indexed_nums.append((num, i))
        
        indexed_nums.sort(key=lambda x: x[0])
        
        l, r = 0, len(nums) - 1
        while l < r:
            current_sum = indexed_nums[l][0] + indexed_nums[r][0]
            if current_sum == target:
                return sorted([indexed_nums[l][1], indexed_nums[r][1]])
            elif current_sum < target:
                l += 1
            else:
                r -= 1
        return []