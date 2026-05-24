"""
==========================================
  Number of 1 Bits (LeetCode 191)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a positive integer n, write a function that returns the number of set bits in its binary representation (also known as the Hamming weight).

Example 1: Input: n = 11 (1011), Output: 3
Example 2: Input: n = 128 (10000000), Output: 1
Example 3: Input: n = 2147483645 (1111...101), Output: 30

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Count how many 1s are in the binary form of a number.

    11 in binary = 1 0 1 1  →  three 1s  →  answer: 3

Trick: n & (n-1) removes the LOWEST set bit!
    1011 & 1010 = 1010  (removed rightmost 1)
    1010 & 1001 = 1000  (removed next 1)
    1000 & 0111 = 0000  (removed last 1)
    Count: 3 operations = 3 bits  ★
"""
