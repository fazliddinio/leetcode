"""
# Merge Sorted Array

## Problem Description
You are given two integer arrays `nums1` and `nums2`, sorted in non-decreasing order, and two integers `m` and `n`, representing the number of elements in `nums1` and `nums2` respectively.
Merge `nums1` and `nums2` into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array `nums1`. To accommodate this, `nums1` has a length of `m + n`.

## Approaches
1.  **Brute Force/Merge and Sort**: Copy `nums2` into `nums1` and sort `nums1`.
    *   Time Complexity: O((m+n) log(m+n))
    *   Space Complexity: O(1) or O(log(m+n)) depending on sort.
2.  **Three Pointers** (Optimal): Start from the end of `nums1` and merge backwards. This avoids overwriting elements in `nums1` that haven't been processed yet.
    *   Time Complexity: O(m + n)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Three Pointers (Reverse)
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges two sorted integer arrays nums1 and nums2 into nums1 as one sorted array.

        Args:
            nums1: The first sorted array, which has a length of m + n.
            m: The number of initialized elements in nums1.
            nums2: The second sorted array.
            n: The number of initialized elements in nums2.

        Returns:
            None. Modifies nums1 in-place.

        Time Complexity: O(m + n) - We iterate through both arrays once.
        Space Complexity: O(1) - We modify nums1 in-place.
        """
        last_index = m + n - 1
        
        # Merge starting from the end
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last_index] = nums1[m - 1]
                m -= 1
            else:
                nums1[last_index] = nums2[n - 1]
                n -= 1
            last_index -= 1
            
        # Fill nums1 with remaining elements of nums2 if any
        while n > 0:
            nums1[last_index] = nums2[n - 1]
            n -= 1
            last_index -= 1

class SolutionBruteForce:
    """
    Naive Solution: Sort
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges then sorts.
        
        Time Complexity: O((m+n) log(m+n))
        Space Complexity: O(1) assumption / sort overhead
        """
        for i in range(n):
            nums1[m + i] = nums2[i]
        nums1.sort()