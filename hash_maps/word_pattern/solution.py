"""
Word Pattern
LeetCode 290

Approach: Two Hash Maps
Time: O(n) — Single pass.
Space: O(n) — Store mapping.
Brute: O(n^2) — Transform to index patterns and compare.
"""

from typing import List


class Solution:

    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        char_to_word = {}
        word_to_char = {}
        for c, w in zip(pattern, words):
            if c in char_to_word and char_to_word[c] != w:
                return False
            if w in word_to_char and word_to_char[w] != c:
                return False
            char_to_word[c] = w
            word_to_char[w] = c
        return True
