"""
Number of 1 Bits
LeetCode 191

Approach: Loop and Flip (Brian Kernighan's Algorithm)
Time: O(1) — max 32 operations
Space: O(1) — constant variable space
Brute: O(1) — convert to binary string and count '1' characters
"""


class Solution:

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count
