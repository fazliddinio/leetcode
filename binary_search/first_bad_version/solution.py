"""
# First Bad Version

## Problem Description
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have `n` versions `[1, 2, ..., n]` and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API `bool isBadVersion(version)` which returns whether `version` is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

## Approaches
1.  **Linear Search** (Brute Force): Check each version starting from 1.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
2.  **Binary Search** (Optimal): Binary search on the version numbers.
    *   Time Complexity: O(log n)
    *   Space Complexity: O(1)
"""

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Dummy definition for local testing context (will be mocked in tests)
if 'isBadVersion' not in globals():
    def isBadVersion(version: int) -> bool:
        return False

class Solution:
    """
    Optimal Solution: Binary Search
    """
    def firstBadVersion(self, n: int) -> int:
        """
        Finds first bad version using binary search.
        
        Args:
            n: Total versions.
            
        Returns:
            First bad version.
            
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        l, r = 1, n
        res = n
        
        while l <= r:
            m = (l + r) // 2
            if isBadVersion(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res

class SolutionBruteForce:
    """
    Alternative Solution: Linear Search
    """
    def firstBadVersion(self, n: int) -> int:
        """
        Finds first bad version by checking one by one.
        Time Complexity: O(n)
        """
        for i in range(1, n + 1):
            if isBadVersion(i):
                return i
        return n # Should not reach if bad exists
