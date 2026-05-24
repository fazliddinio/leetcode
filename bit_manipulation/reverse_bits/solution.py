"""
Reverse Bits
LeetCode 190

Approach: Bit Manipulation
Time: O(1) — 32 iterations (constant)
Space: O(1) — constant variable space
Brute: O(1) — convert to 32-bit binary string, reverse, convert back
"""


class Solution:

    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1 | n & 1
            n >>= 1
        return res
