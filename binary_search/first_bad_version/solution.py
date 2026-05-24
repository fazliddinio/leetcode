"""
First Bad Version
LeetCode 278

Approach: Binary Search
Time: O(log n) — logarithmic number of API calls
Space: O(1) — constant variable space
Brute: O(n) — linear scan checking each version from 1 to n
"""

_BAD_VERSION = 1
def isBadVersion(version: int) -> bool:
    global _BAD_VERSION
    return version >= _BAD_VERSION

class Solution:

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
