"""
# Longest Common Prefix

## Problem Description
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

## Approaches
1.  **Horizontal Scanning** (Optimal): Take the first string as initial prefix, compare it with the next string, update prefix, and repeat.
    *   Time Complexity: O(S) - where S is the sum of all characters.
    *   Space Complexity: O(1)
2.  **Vertical Scanning** (Alternative): Compare characters from top to bottom (same index of each string).
    *   Time Complexity: O(S)
    *   Space Complexity: O(1)
3.  **Sorting** (Brute Force/Alternative): Sort the strings and compare the first and last string.
    *   Time Complexity: O(N log N * M) where M is max string length.
    *   Space Complexity: O(1) or O(M)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Horizontal Scanning
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string amongst an array of strings.

        Args:
            strs: A list of strings.

        Returns:
            The longest common prefix. Returns an empty string if none exists.

        Time Complexity: O(S) - where S is the sum of all characters in all strings.
        Space Complexity: O(1) - We use constant extra space for variables.
        """
        if not strs:
            return ""
        
        prefix = strs[0]
        
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

class SolutionVertical:
    """
    Alternative Solution: Vertical Scanning
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds LCP column by column.
        
        Time Complexity: O(S)
        Space Complexity: O(1)
        """
        if not strs:
            return ""
            
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != char:
                    return strs[0][:i]
        return strs[0]

class SolutionSorting:
    """
    Alternative Solution: Sorting
    """
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds LCP by sorting and comparing ends.
        
        Time Complexity: O(N log N * M)
        Space Complexity: O(M)
        """
        if not strs:
            return ""
            
        strs.sort()
        s1, s2 = strs[0], strs[-1]
        idx = 0
        while idx < len(s1) and idx < len(s2):
            if s1[idx] != s2[idx]:
                break
            idx += 1
        return s1[:idx]