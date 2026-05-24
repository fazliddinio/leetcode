"""
Reverse Integer
LeetCode 7

Approach: Digit Extraction
Time: O(log X) — number of digits, approx O(1) for 32-bit int
Space: O(1) — constant variable space
Brute: O(log X) — convert to string, reverse, clamp to 32-bit range
"""


class Solution:

    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        res = 0
        while x != 0:
            pop = x % 10
            x //= 10
            if res > 214748364 or (res == 214748364 and pop > 7):
                return 0
            if res < -214748364 or (res == -214748364 and pop > 8):
                return 0
            res = res * 10 + pop
        return sign * res
