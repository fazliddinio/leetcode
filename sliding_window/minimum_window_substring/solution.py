"""
Minimum Window Substring
LeetCode 76

Approach: Sliding Window + Match Count
Time: O(n + m) — where n and m are lengths of s and t
Space: O(m) — hash map stores character counts from t
Brute: O(n² * m) — check all substrings for containing t
"""

from collections import Counter, defaultdict


class Solution:

    def minWindow(self, s: str, t: str) -> str:
        """Sliding Window + Match Count Approach"""
        if not t or not s:
            return ""
            
        t_count = Counter(t)
        required = len(t_count)
        formed = 0
        window_counts = defaultdict(int)
        
        left = 0
        min_len = float('inf')
        min_window = (0, 0)
        
        for right in range(len(s)):
            char = s[right]
            window_counts[char] += 1
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
                
            while formed == required and left <= right:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = (left, right)
                    
                left_char = s[left]
                window_counts[left_char] -= 1
                if left_char in t_count and window_counts[left_char] < t_count[left_char]:
                    formed -= 1
                left += 1
                
        return "" if min_len == float('inf') else s[min_window[0]:min_window[1] + 1]
