"""
# Longest Substring Without Repeating Characters

## Problem Description
Given a string `s`, find the length of the longest substring without repeating characters.

## Approaches
1.  **Brute Force**: Check all substrings for uniqueness.
    *   Time Complexity: O(n^3)
    *   Space Complexity: O(min(n, m)) for set in check.
2.  **Sliding Window with Set** (Optimal): Use a set to track characters in the current window.
    *   Time Complexity: O(n)
    *   Space Complexity: O(min(m, n)) where m is charset size.
3.  **Sliding Window with Map** (Alternative): Store index of each char to jump `l` directly.
    *   Time Complexity: O(n)
    *   Space Complexity: O(min(m, n))
"""

from typing import Set, Dict

class Solution:
    """
    Optimal Solution: Sliding Window (Set)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds length of longest substring without repeats.
        
        Args:
            s: Input string.
            
        Returns:
            Max length.
            
        Time Complexity: O(n)
        Space Complexity: O(min(m, n))
        """
        char_set: Set[str] = set()
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            res = max(res, r - l + 1)
        return res

class SolutionBruteForce:
    """
    Naive Solution: Check All Substrings
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds length using brute force.
        Time Complexity: O(n^3)
        """
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if self.is_unique(s, i, j):
                    res = max(res, j - i + 1)
        return res

    def is_unique(self, s, start, end):
        chars = set()
        for k in range(start, end + 1):
            if s[k] in chars:
                return False
            chars.add(s[k])
        return True

class SolutionMap:
    """
    Alternative Solution: Sliding Window (Map Optimization)
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds length using map to skip.
        
        Time Complexity: O(n)
        Space Complexity: O(min(m, n))
        """
        char_map: Dict[str, int] = {} # char -> index
        l = 0
        res = 0
        
        for r in range(len(s)):
            if s[r] in char_map:
                l = max(l, char_map[s[r]] + 1)
            char_map[s[r]] = r
            res = max(res, r - l + 1)
        return res
