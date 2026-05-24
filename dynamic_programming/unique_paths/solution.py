"""
Unique Paths
LeetCode 62

Approach: Space Optimized DP
Time: O(m * n) — Fill table (conceptually).
Space: O(n) — Store only one row.
Brute: O(2^(m+n)) — Recursive DFS exploring all right/down paths.
"""


class Solution:

    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        for i in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j]
            row = new_row
        return row[0]
