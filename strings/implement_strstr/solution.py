"""
Find the Index of the First Occurrence in a String (Implement strStr)
LeetCode 28

Approach: Built-in / Sliding Window
Time: O(n*m) — Worst-case substring matching.
Space: O(1) — Constant variable space.
Brute: O(n*m) — Manually slide a window and compare substrings character by character.
"""


class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
