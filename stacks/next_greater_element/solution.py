"""
# Next Greater Element I

## Problem Description
The **next greater element** of some element x in an array is the first greater element that is to the right of x in the same array.
You are given two distinct 0-indexed integer arrays `nums1` and `nums2`, where `nums1` is a subset of `nums2`.
For each `0 <= i < nums1.length`, find the index `j` such that `nums1[i] == nums2[j]` and determine the next greater element of `nums2[j]` in `nums2`. If there is no next greater element, then the answer for this query is `-1`.
Return an array `ans` of length `nums1.length` such that `ans[i]` is the next greater element as described above.

## Approaches
1.  **Brute Force**: For each element in `nums1`, find it in `nums2`, then scan right.
    *   Time Complexity: O(n * m)
    *   Space Complexity: O(1)
2.  **Monotonic Stack + Map** (Optimal): Precompute next greater for all elements in `nums2` using stack and map.
    *   Time Complexity: O(n + m)
    *   Space Complexity: O(m)
"""

from typing import List, Dict

class Solution:
    """
    Optimal Solution: Monotonic Stack + Map
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds next greater element.
        
        Args:
            nums1: Subset.
            nums2: Superset.
            
        Returns:
            List of next greater elements.
            
        Time Complexity: O(n + m)
        Space Complexity: O(m)
        """
        nums1_idx: Dict[int, int] = {n: i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)
        
        stack: List[int] = []
        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                if val in nums1_idx:
                    res[nums1_idx[val]] = cur
            stack.append(cur)
        return res

class SolutionBruteForce:
    """
    Naive Solution: Nested Search
    """
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Finds next greater using brute force.
        Time Complexity: O(n * m)
        """
        res = []
        for n1 in nums1:
            found = False
            val = -1
            for n2 in nums2:
                if n2 == n1:
                    found = True
                if found and n2 > n1:
                    val = n2
                    break
            res.append(val)
        return res
