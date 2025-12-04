"""
# Valid Anagram

## Problem Description
Given two strings `s` and `t`, return `true` if `t` is an anagram of `s`, and `false` otherwise.

## Approaches
1.  **Sorting** (Brute Force/Alternative): Sort both strings and compare them.
    *   Time Complexity: O(N log N)
    *   Space Complexity: O(1) or O(N) depending on sort implementation.
2.  **Hash Map** (Optimal): Count frequency of each character.
    *   Time Complexity: O(N)
    *   Space Complexity: O(1) (fixed alphabet size).
3.  **Fixed Array** (Alternative): Use an array of size 26 for frequency.
    *   Time Complexity: O(N)
    *   Space Complexity: O(1)
"""

from typing import Dict, List

class Solution:
    """
    Optimal Solution: Hash Map
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Given two strings s and t, return true if t is an anagram of s, and false otherwise.

        Args:
            s: The first string.
            t: The second string.

        Returns:
            True if t is an anagram of s, False otherwise.

        Time Complexity: O(n) - We iterate through both strings once.
        Space Complexity: O(1) - The character set is limited.
        """
        if len(s) != len(t):
            return False
            
        count_s: Dict[str, int] = {}
        count_t: Dict[str, int] = {}
        
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            
        return count_s == count_t

class SolutionSorting:
    """
    Alternative Solution: Sorting
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks anagram by sorting.
        
        Time Complexity: O(N log N)
        Space Complexity: O(N) (Python sorted returns a new list)
        """
        return sorted(s) == sorted(t)

class SolutionArray:
    """
    Alternative Solution: Fixed Array
    """
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks anagram using fixed size array.
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        if len(s) != len(t):
            return False
            
        count = [0] * 26
        offset = ord('a')
        
        for char in s:
            count[ord(char) - offset] += 1
        for char in t:
            count[ord(char) - offset] -= 1
            
        for c in count:
            if c != 0:
                return False
        return True