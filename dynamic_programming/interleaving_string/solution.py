"""
Interleaving String
LeetCode 97

Approach: 2D DP
Time: O(M * N) — Fill table of size (M+1)x(N+1).
Space: O(M * N) — DP table size.
Brute: O(2^(M+N)) — Recursive DFS trying all interleaving choices.
"""


class Solution:

    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = (len(s1), len(s2))
        if m + n != len(s3):
            return False
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, m + 1):
            dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j - 1] and s2[j - 1] == s3[j - 1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                valid_s1 = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                valid_s2 = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                dp[i][j] = valid_s1 or valid_s2
        return dp[m][n]
