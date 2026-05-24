"""
Counting Bits
LeetCode 338

Approach: DP / Bit Manipulation
Time: O(N) — single pass through numbers
Space: O(1) — output array doesn't count as extra space
Brute: O(N log N) — for each number, count '1's in its binary representation
"""

from typing import List


class Solution:

    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
