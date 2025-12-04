"""
# Find All Anagrams in a String

## Problem Description
Given two strings `s` and `p`, return an array of all the start indices of `p`'s anagrams in `s`. You may return the answer in any order.

## Approaches
1.  **Sorting** (Brute Force): For every window of length `p` in `s`, sort and compare with sorted `p`.
    *   Time Complexity: O(n * m log m) where n is s.length, m is p.length.
    *   Space Complexity: O(m)
2.  **Sliding Window** (Optimal): Maintain frequency counts in a window.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1) (fixed size 26).
"""

from typing import List, Dict

class Solution:
    """
    Optimal Solution: Sliding Window (Array/Map)
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Finds all start indices of p's anagrams in s.
        
        Args:
            s: The string to search in.
            p: The string to find anagrams of.
            
        Returns:
            Indices of anagrams.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if len(p) > len(s):
            return []
            
        p_count: Dict[str, int] = {}
        s_count: Dict[str, int] = {}
        
        for i in range(len(p)):
            p_count[p[i]] = 1 + p_count.get(p[i], 0)
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            
        res = [0] if s_count == p_count else []
        l = 0
        
        for r in range(len(p), len(s)):
            s_count[s[r]] = 1 + s_count.get(s[r], 0)
            s_count[s[l]] -= 1
            
            if s_count[s[l]] == 0:
                del s_count[s[l]]
            l += 1
            
            if s_count == p_count:
                res.append(l)
                
        return res

class SolutionBruteForce:
    """
    Naive Solution: Sorting
    """
    def findAnagrams(self, s: str, p: str) -> List[int]:
        """
        Finds anagrams by sorting.
        """
        n, m = len(s), len(p)
        if n < m: return []
        
        sorted_p = sorted(p)
        res = []
        
        for i in range(n - m + 1):
            if sorted(s[i:i+m]) == sorted_p:
                res.append(i)
        return res
