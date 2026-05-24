"""
Longest Repeating Character Replacement
LeetCode 424

Approach: Sliding Window + Max Freq Optimization
Time: O(n) — single pass, max frequency only updated when it increases
Space: O(1) — fixed size map (26 chars)
Brute: O(26 * n²) — check all substrings with frequency count
"""

from collections import defaultdict


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        """Sliding Window with Max Freq Optimization"""
        freq = defaultdict(int)
        left = 0
        max_freq = 0
        max_length = 0
        
        for right in range(len(s)):
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            
            # window_length - max_freq = number of chars to replace
            if (right - left + 1) - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                
            max_length = max(max_length, right - left + 1)
            
        return max_length
