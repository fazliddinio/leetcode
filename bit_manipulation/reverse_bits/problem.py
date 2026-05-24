"""
==========================================
  Reverse Bits (LeetCode 190)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Reverse bits of a given 32 bits unsigned integer.

Example 1: Input: n = 43261596 (00000010100101000001111010011100)
Output: 964176192 (00111001011110000010100101000000)

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Flip the 32-bit binary number left-to-right, like reading it backwards.

    Input:  00000010100101000001111010011100
    Output: 00111001011110000010100101000000

How: Process each of the 32 bits from right to left, building result left to right.
    result = 0
    For each of 32 bits:
        result <<= 1           (shift result left to make room)
        result |= (n & 1)      (put rightmost bit of n into result)
        n >>= 1                (move to next bit of n)
"""
