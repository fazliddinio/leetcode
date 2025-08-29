# LeetCode 3: Longest Substring Without Repeating Characters
# Time: O(n), Space: O(min(n, m))

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        left = 0
        max_len = 0
        
        for right, c in enumerate(s):
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            max_len = max(max_len, right - left + 1)
        
        return max_len
