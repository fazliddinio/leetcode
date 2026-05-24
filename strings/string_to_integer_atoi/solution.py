"""
String to Integer (atoi)
LeetCode 8

Approach: Deterministic Logic
Time: O(n) — Process string once.
Space: O(1) — Constant variable space.
Brute: O(n) — Use regex to extract number pattern, convert, then clamp to 32-bit range.
"""


class Solution:

    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0
        sign = 1
        index = 0
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        result = 0
        MAX_INT = 2 ** 31 - 1
        MIN_INT = -2 ** 31
        while index < len(s) and s[index].isdigit():
            digit = int(s[index])
            if result > (MAX_INT - digit) // 10:
                return MAX_INT if sign == 1 else MIN_INT
            result = result * 10 + digit
            index += 1
        return sign * result
