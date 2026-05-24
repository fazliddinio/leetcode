"""
Find All Anagrams in a String
LeetCode 438

Approach: Sliding Window + Frequency Array
Time: O(n) — one pass, array comparison is O(26) = O(1)
Space: O(1) — two fixed-size arrays of 26 elements
Brute: O(n * m log m) — sort each window and compare with sorted p
"""

from typing import List


class Solution:

    def findAnagrams(self, s: str, p: str) -> List[int]:
        """Sliding Window + Frequency Array Approach"""
        if len(p) > len(s):
            return []
            
        p_count = [0] * 26
        window_count = [0] * 26
        result = []
        
        for c in p:
            p_count[ord(c) - ord('a')] += 1
            
        for i in range(len(s)):
            window_count[ord(s[i]) - ord('a')] += 1
            
            if i >= len(p):
                window_count[ord(s[i - len(p)]) - ord('a')] -= 1
                
            if window_count == p_count:
                result.append(i - len(p) + 1)
                
        return result
