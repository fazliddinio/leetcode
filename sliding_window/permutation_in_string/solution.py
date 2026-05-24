"""
Permutation in String
LeetCode 567

Approach: Sliding Window + Frequency Array
Time: O(n) — one pass through s2, array comparison is O(26) = O(1)
Space: O(1) — fixed-size arrays of 26 elements
Brute: O(n * m log m) — sort each window of s2 and compare with sorted s1
"""


class Solution:

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Sliding Window + Frequency Array Approach"""
        if len(s1) > len(s2):
            return False
            
        s1_count = [0] * 26
        window_count = [0] * 26
        
        for c in s1:
            s1_count[ord(c) - ord('a')] += 1
            
        for i in range(len(s2)):
            window_count[ord(s2[i]) - ord('a')] += 1
            
            if i >= len(s1):
                window_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
                
            if s1_count == window_count:
                return True
                
        return False
