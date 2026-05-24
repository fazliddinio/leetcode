"""
==========================================
  Valid Perfect Square (LeetCode 367)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given a positive integer `num`, return `true` if `num` is a perfect
square or `false` otherwise.

A perfect square is an integer that is the square of an integer. In other
words, it is the product of some integer with itself.

You must not use any built-in library function, such as `sqrt`.

Example 1:
    Input: num = 16
    Output: true
    Explanation: 4 * 4 = 16

Example 2:
    Input: num = 14
    Output: false

Constraints:
    - 1 <= num <= 2^31 - 1


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Is this number a perfect square? (Can some integer times itself equal it?)

    16 → 4 × 4 = 16 → YES ✓
    14 → 3² = 9, 4² = 16 → nothing works → NO ✗

Binary search for the answer:

    num = 16
    lo=1, hi=16

    mid=8 → 8²=64 > 16 → too big → hi=7
    mid=4 → 4²=16 == 16 → FOUND! ★ → return True

    num = 14
    lo=1, hi=14

    mid=7 → 49 > 14 → hi=6
    mid=3 → 9 < 14  → lo=4
    mid=5 → 25 > 14 → hi=4
    mid=4 → 16 > 14 → hi=3
    lo=4 > hi=3 → not found → return False
"""
