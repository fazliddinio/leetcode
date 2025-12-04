"""
# Three Sum

## Problem Description
Given an integer array nums, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.
Notice that the solution set must not contain duplicate triplets.

## Approaches
1.  **Brute Force**: Three nested loops to check every triplet.
    *   Time Complexity: O(n^3)
    *   Space Complexity: O(1) (or O(m) to store results, need Set to avoid duplicates)
2.  **Hash Map** (Alternative): Fix one number, then solve 2-Sum with Hash Map.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(n) (for hash map)
3.  **Sorting + Two Pointers** (Optimal): Sort array, fix one number, use two pointers for the other two. Easy to skip duplicates.
    *   Time Complexity: O(n^2)
    *   Space Complexity: O(1) or O(n) depending on sort.
"""

from typing import List

class Solution:
    """
    Optimal Solution: Sorting + Two Pointers
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds all unique triplets in the array which gives the sum of zero.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists, where each inner list is a triplet.
        
        Time Complexity: O(n^2)
        Space Complexity: O(1) (excluding output)
        """
        res = []
        nums.sort()
        
        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res

class SolutionBruteForce:
    """
    Naive Solution: Triple Loop
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds triplets using brute force.
        Time Complexity: O(n^3)
        """
        nums.sort() # Sorting helps to handle duplicates easier
        res = set()
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        res.add((nums[i], nums[j], nums[k]))
        return [list(x) for x in res]

class SolutionHash:
    """
    Alternative Solution: Hash Map (Fix one, 2-Sum Hash)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Finds triplets using Hash Set for 2-Sum.
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        """
        nums.sort()
        res = set()
        for i in range(len(nums)):
            target = -nums[i]
            seen = set()
            for j in range(i + 1, len(nums)):
                complement = target - nums[j]
                if complement in seen:
                    res.add((nums[i], complement, nums[j]))
                seen.add(nums[j])
        return [list(x) for x in res]
