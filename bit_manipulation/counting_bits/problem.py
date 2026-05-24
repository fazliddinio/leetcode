"""
==========================================
  Counting Bits (LeetCode 338)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

Example 1: Input: n = 2, Output: [0,1,1]
Example 2: Input: n = 5, Output: [0,1,1,2,1,2]

Constraints: 0 <= n <= 10^5

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Count the 1-bits in every number from 0 to n.

    Number:  0    1    2    3    4    5
    Binary: 000  001  010  011  100  101
    1-bits:  0    1    1    2    1    2

    Answer: [0, 1, 1, 2, 1, 2]

Pattern trick (DP): The number of 1s in i = number of 1s in (i >> 1) + (i & 1)
    i=5 (101) → i>>1 = 2 (10) has 1 one-bit, plus last bit is 1 → total = 2

    Basically: "shift right and check if last bit is 1"
"""
