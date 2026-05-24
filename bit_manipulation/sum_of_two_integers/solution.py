"""
Sum of Two Integers
LeetCode 371

Approach: Bit Manipulation (Carry)
Time: O(1) — constant number of bits (32)
Space: O(1) — constant variable space
Brute: O(|b|) — increment/decrement a by 1 repeatedly b times
"""


class Solution:

    def getSum(self, a: int, b: int) -> int:
        mask = 4294967295
        while b != 0:
            tmp = (a ^ b) & mask
            carry = (a & b) << 1 & mask
            a = tmp
            b = carry
        if a > 2147483647:
            return ~(a ^ mask)
        else:
            return a
