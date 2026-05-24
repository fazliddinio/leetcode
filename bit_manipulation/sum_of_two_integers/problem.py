"""
==========================================
  Sum of Two Integers (LeetCode 371)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given two integers a and b, return the sum of the two integers without using the operators + and -.

Example 1: Input: a = 1, b = 2, Output: 3
Example 2: Input: a = 2, b = 3, Output: 5

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Add two numbers WITHOUT using + or -. Use binary math!

    a=2 (10), b=3 (11)

    Step 1: XOR gives sum without carry:  10 ^ 11 = 01
    Step 2: AND + shift gives carry:      (10 & 11) << 1 = 10 << 1 = 100

    Now add 01 + 100 (repeat!):
    Step 3: XOR: 001 ^ 100 = 101 (=5)
    Step 4: AND+shift: (001 & 100) << 1 = 0

    Carry is 0 → done!  Answer: 5 (101)  ★

Think of it like grade-school addition in binary:
      1 0    (2)
    + 1 1    (3)
    -----
    1 0 1    (5)
"""
