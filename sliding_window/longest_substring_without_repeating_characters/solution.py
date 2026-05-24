"""
Longest Substring Without Repeating Characters
LeetCode 3

Approach: Sliding Window + Hash Map (Index Jump)
Time: O(n) — single pass, skips redundant left pointer steps
Space: O(min(m, n)) — map stores character indices
Brute: O(n³) — check all substrings for character uniqueness
"""


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        """Sliding Window Hash Map Approach (Jump)"""
        char_index = {}
        left = 0
        max_length = 0
        
        for right, char in enumerate(s):
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1
            char_index[char] = right
            max_length = max(max_length, right - left + 1)
            
        return max_length
