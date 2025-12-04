"""
# Permutation in String

## Problem Description
Given two strings `s1` and `s2`, return `true` if `s2` contains a permutation of `s1`, or `false` otherwise.
In other words, return `true` if one of `s1`'s permutations is the substring of `s2`.

## Approaches
1.  **Sorting** (Brute Force): For every window of length `len(s1)` in `s2`, sort it and compare with sorted `s1`.
    *   Time Complexity: O(N * L1 log L1)
    *   Space Complexity: O(L1)
2.  **Sliding Window with Array** (Optimal): Use frequency array of size 26. Slide window and update counts.
    *   Time Complexity: O(l1 + l2)
    *   Space Complexity: O(1)
"""

from typing import List

class Solution:
    """
    Optimal Solution: Sliding Window (Array)
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Checks if s2 contains a permutation of s1.

        Args:
            s1: The string to find a permutation of.
            s2: The string to search in.

        Returns:
            True if s2 contains a permutation of s1, False otherwise.

        Time Complexity: O(l1 + l2)
        Space Complexity: O(1)
        """
        if len(s1) > len(s2):
            return False
            
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
            
        matches = 0
        for i in range(26):
            if s1_count[i] == s2_count[i]:
                matches += 1
                
        l = 0
        for r in range(len(s1), len(s2)):
            if matches == 26:
                return True
                
            index = ord(s2[r]) - ord('a')
            s2_count[index] += 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] + 1 == s2_count[index]:
                matches -= 1
                
            index = ord(s2[l]) - ord('a')
            s2_count[index] -= 1
            if s1_count[index] == s2_count[index]:
                matches += 1
            elif s1_count[index] - 1 == s2_count[index]:
                matches -= 1
            l += 1
            
        return matches == 26

class SolutionSorting:
    """
    Alternative Solution: Sorting Windows
    """
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Checks by sorting every window.
        
        Time Complexity: O(N * M log M)
        """
        if len(s1) > len(s2):
            return False
        
        sorted_s1 = sorted(s1)
        m = len(s1)
        
        for i in range(len(s2) - m + 1):
            window = s2[i:i+m]
            if sorted(window) == sorted_s1:
                return True
        return False
