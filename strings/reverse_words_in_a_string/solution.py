"""
Reverse Words in a String
LeetCode 151

Approach: Built-in Split/Reverse
Time: O(n) — Split and Join operations.
Space: O(n) — List of words.
Brute: O(n) — Manually extract words character by character, then reverse the list.
"""


class Solution:

    def reverseWords(self, s: str) -> str:
        words = s.split()
        return ' '.join(reversed(words))
