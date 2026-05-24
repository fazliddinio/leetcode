"""
Longest Substring with At Most K Distinct Characters
LeetCode 340

Approach: Sliding Window + Hash Map
Time: O(n) — single pass
Space: O(k) — map stores k distinct characters
Brute: O(n²) — check all substrings for distinct character count
"""

from collections import defaultdict


class Solution:

    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        """Sliding Window Hash Map Approach"""
        if k == 0:
            return 0
            
        left = 0
        max_len = 0
        char_count = defaultdict(int)
        
        for right, char in enumerate(s):
            char_count[char] += 1
            
            while len(char_count) > k:
                left_char = s[left]
                char_count[left_char] -= 1
                if char_count[left_char] == 0:
                    del char_count[left_char]
                left += 1
                
            max_len = max(max_len, right - left + 1)
            
        return max_len
