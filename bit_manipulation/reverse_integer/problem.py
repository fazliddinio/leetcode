"""
==========================================
  Reverse Integer (LeetCode 7)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], then return 0.

Example 1: Input: x = 123, Output: 321
Example 2: Input: x = -123, Output: -321
Example 3: Input: x = 120, Output: 21

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Read the number backwards. Watch out for overflow!

    123  → 321
    -123 → -321
    120  → 21  (leading zeros disappear)

How: Pop digits from the end, push them to a new number.
    123 → pop 3 → result = 3
        → pop 2 → result = 32
        → pop 1 → result = 321

    pop: digit = x % 10,  x = x // 10
    push: result = result * 10 + digit

Before each push, check if result would overflow 32-bit range!
"""
