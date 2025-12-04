"""
# Contains Duplicate

## Problem Description
Given an integer array `nums`, return `true` if any value appears at least twice in the array, and return `false` if every element is distinct.

## Approaches
1.  **Brute Force**: Check every pair of elements for duplicates.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1)
2.  **Sorting** (Alternative): Sort the array, then check adjacent elements.
    *   Time Complexity: O(n log n)
    *   Space Complexity: O(1) (ignoring sort implementation stack) or O(n) depending on sort.
3.  **Hash Set** (Optimal): Use a hash set to track seen elements.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Hash Set
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks if the array contains any duplicate values.

        Args:
            nums: A list of integers.

        Returns:
            True if any value appears at least twice, False otherwise.

        Time Complexity: O(n) - We iterate through the list, and set lookups are O(1) on average.
        Space Complexity: O(n) - We store unique elements in a hash set.
        """
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

class SolutionBruteForce:
    """
    Naive Solution: Nested Loops
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks for duplicates using brute force.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    return True
        return False

class SolutionAlternative:
    """
    Alternative Solution: Sorting
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        Checks for duplicates by sorting first.
        
        Time Complexity: O(n log n)
        Space Complexity: O(1) or O(n) depending on sort.
        """
        # We perform a sort. Note: This modifies the input array or we copy it.
        # Here we sort in place for O(1) extra space assumption, or sorted() for O(n).
        # To be safe and purely functional, let's use sorted() which is O(n) space.
        # But for the sake of "different approach", let's assume mutable or copy.
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums) - 1):
            if sorted_nums[i] == sorted_nums[i+1]:
                return True
        return False
