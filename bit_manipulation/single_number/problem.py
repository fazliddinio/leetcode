"""
==========================================
  Single Number (LeetCode 136)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one. You must implement a solution with O(n) time and O(1) extra space.

Example 1: Input: nums = [2,2,1], Output: 1
Example 2: Input: nums = [4,1,2,1,2], Output: 4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Every number appears twice except one loner. Find it!

    [4, 1, 2, 1, 2]  →  4 is alone!

Magic trick: XOR (^) cancels pairs!
    a ^ a = 0    (any number XOR itself = 0)
    a ^ 0 = a    (XOR with 0 = itself)

    4 ^ 1 ^ 2 ^ 1 ^ 2
    = 4 ^ (1^1) ^ (2^2)
    = 4 ^ 0 ^ 0
    = 4  ★

Just XOR everything together. Pairs vanish, the loner survives!
"""
