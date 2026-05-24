"""
Isomorphic Strings
LeetCode 205

Approach: Two Hash Maps
Time: O(n) — Single pass.
Space: O(1) — Charset size is fixed (ASCII 256).
Brute: O(n^2) — Transform each string to canonical index pattern and compare.
"""


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s_t = {}
        map_t_s = {}
        for c1, c2 in zip(s, t):
            if c1 in map_s_t and map_s_t[c1] != c2 or (c2 in map_t_s and map_t_s[c2] != c1):
                return False
            map_s_t[c1] = c2
            map_t_s[c2] = c1
        return True
