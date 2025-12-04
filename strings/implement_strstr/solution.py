"""
# Implement strStr()

## Problem Description
Given two strings `needle` and `haystack`, return the index of the first occurrence of `needle` in `haystack`, or `-1` if `needle` is not part of `haystack`.

## Approaches
1.  **Brute Force** (Explicit): Check every starting position `i` in `haystack`. For each `i`, check if substring matches `needle`.
    *   Time Complexity: O(N * M) where N is haystack len, M is needle len.
    *   Space Complexity: O(1)
2.  **Slicing** (Pythonic/Alternative): Use Python slicing to compare substrings.
    *   Time Complexity: O(N * M) potentially, though optimized in C.
    *   Space Complexity: O(M) or O(1) depending on implementation details of slice comparison.
3.  **Built-in** (Alternative): `haystack.find(needle)`.
    *   Time Complexity: O(N * M) worst case.
    *   Space Complexity: O(1)
"""

class Solution:
    """
    Solution: Slicing (Common Python Approach)
    """
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds the index of the first occurrence of needle in haystack.

        Args:
            haystack: The main string to search in.
            needle: The substring to search for.

        Returns:
            The index of the first occurrence, or -1.

        Time Complexity: O(n * m)
        Space Complexity: O(1)
        """
        if not needle:
            return 0
        if needle == haystack:
            return 0
            
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            if haystack[i : i + m] == needle:
                return i
        return -1

class SolutionBruteForce:
    """
    Naive Solution: Explicit Nested Loops
    """
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds index using explicit loops.
        
        Time Complexity: O(N*M)
        Space Complexity: O(1)
        """
        if not needle:
            return 0
        n, m = len(haystack), len(needle)
        
        for i in range(n - m + 1):
            match = True
            for j in range(m):
                if haystack[i + j] != needle[j]:
                    match = False
                    break
            if match:
                return i
        return -1

class SolutionBuiltIn:
    """
    Alternative Solution: Built-in
    """
    def strStr(self, haystack: str, needle: str) -> int:
        """
        Finds index using find().
        """
        return haystack.find(needle)
