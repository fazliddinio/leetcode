# LeetCode 438: Find All Anagrams in a String
# Time: O(n), Space: O(1)

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        
        p_count = [0] * 26
        s_count = [0] * 26
        result = []
        
        for c in p:
            p_count[ord(c) - ord('a')] += 1
        
        for i in range(len(s)):
            s_count[ord(s[i]) - ord('a')] += 1
            
            if i >= len(p):
                s_count[ord(s[i - len(p)]) - ord('a')] -= 1
            
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result
