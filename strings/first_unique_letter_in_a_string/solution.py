from typing import List
from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        freq = Counter(s)
        
        for i, char in enumerate(s):
            if freq[char] == 1:
                return i
        return -1
    
    # Time: O(n), Space: O(1)
    def first_uniq_char(s):
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1