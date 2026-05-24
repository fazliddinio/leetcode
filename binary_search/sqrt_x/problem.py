"""
==========================================
  Sqrt(x) (LeetCode 69)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given a non-negative integer `x`, return the square root of `x` rounded
down to the nearest integer. The returned integer should be non-negative
as well.

You must not use any built-in exponent function or operator.

Example 1:
    Input: x = 4
    Output: 2

Example 2:
    Input: x = 8
    Output: 2
    Explanation: The square root of 8 is 2.82842..., and since we round
                 it down to the nearest integer, 2 is returned.

Constraints:
    - 0 <= x <= 2^31 - 1


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Find the biggest whole number whose square is ≤ x.

    sqrt(4) = 2      (2² = 4 ≤ 4 ✓)
    sqrt(8) = 2      (2² = 4 ≤ 8 ✓, but 3² = 9 > 8 ✗)
    sqrt(16) = 4     (4² = 16 ≤ 16 ✓)

Binary search between 0 and x:

    x = 8
    lo=0, hi=8

    mid=4 → 4²=16 > 8  → too big, go left  → hi=3
    mid=1 → 1²=1 ≤ 8   → could work, go right → lo=2
    mid=2 → 2²=4 ≤ 8   → could work, go right → lo=3
    lo=3 > hi=3 → stop! → answer = 2 (last valid mid)

It's like guessing a number between 0 and x, checking if your
guess squared is too big or too small.
"""
