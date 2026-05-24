"""
Distinct Subsequences
LeetCode 115

Approach: DP with Space Optimization
Time: O(M * N) — M=len(s), N=len(t). Nested loop.
Space: O(N) — Two rows of size N.
Brute: O(2^M) — Recursive enumeration of all subsequences of s.
"""


class Solution:

    def numDistinct(self, s: str, t: str) -> int:
        m, n = (len(s), len(t))
        prev = [0] * (n + 1)
        prev[0] = 1
        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = 1
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    curr[j] = prev[j - 1] + prev[j]
                else:
                    curr[j] = prev[j]
            prev = curr
        return prev[n]
