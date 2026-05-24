"""
Substring with Concatenation of All Words
LeetCode 30

Approach: Sliding Window (Word-by-Word)
Time: O(n * L) — where n is len(s) and L is len(word)
Space: O(m * L) — where m is len(words)
Brute: O(n * m * L) — check every starting index, chunk and compare
"""

from typing import List
from collections import Counter


class Solution:

    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """Sliding Window Word-by-Word Approach"""
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        res = []
        
        for i in range(word_len):
            left = i
            right = i
            current_counts = Counter()
            count = 0
            
            while right + word_len <= len(s):
                w = s[right:right + word_len]
                right += word_len
                
                if w in word_counts:
                    current_counts[w] += 1
                    count += 1
                    
                    while current_counts[w] > word_counts[w]:
                        left_w = s[left:left + word_len]
                        current_counts[left_w] -= 1
                        count -= 1
                        left += word_len
                        
                    if count == num_words:
                        res.append(left)
                else:
                    current_counts.clear()
                    count = 0
                    left = right
                    
        return res
