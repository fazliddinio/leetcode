"""
# Longest Repeating Character Replacement

## Problem Description
You are given a string `s` and an integer `k`. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most `k` times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

## Approaches
1.  **Brute Force**: Check every substring. For each substring, count max freq char. If `length - max_freq <= k`, it's valid.
    *   Time Complexity: O(n^3) (or O(n^2) with optimized check)
    *   Space Complexity: O(1)
2.  **Sliding Window** (Optimal): Maintain window and track max frequency char.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import Dict, Counter

class Solution:
    """
    Optimal Solution: Sliding Window
    """
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds length of longest valid repeating char substring.
        
        Args:
            s: Input string.
            k: Max replacements.
            
        Returns:
            Max length.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        count: Dict[str, int] = {}
        res = 0
        l = 0
        maxf = 0
        
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])
            
            # (r - l + 1) is current window length
            # if window length - max frequency char > k, we need to replace more than k chars
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
                
            res = max(res, r - l + 1)
        return res

class SolutionBruteForce:
    """
    Naive Solution: Check All Substrings
    """
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds length using brute force.
        Time Complexity: O(n^2) * O(26)
        """
        n = len(s)
        res = 0
        for i in range(n):
            count = Counter()
            max_f = 0
            for j in range(i, n):
                count[s[j]] += 1
                max_f = max(max_f, count[s[j]])
                
                length = j - i + 1
                if length - max_f <= k:
                    res = max(res, length)
                else:
                    # Optimization: If already invalid, extending won't help if k doesn't increase (not strictly true, next char could be max_f)
                    # Actually, if we just want max length, we can continue.
                    pass
        return res
