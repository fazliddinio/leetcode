"""
==========================================
  Missing Number (LeetCode 268)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Example 1: Input: nums = [3,0,1], Output: 2
Example 2: Input: nums = [0,1], Output: 2
Example 3: Input: nums = [9,6,4,2,3,5,7,0,1], Output: 8

Constraints: n == nums.length, 1 <= n <= 10^4, 0 <= nums[i] <= n, All numbers are unique.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
You have numbers 0 to n, but one is missing. Find it.

    nums = [3, 0, 1]  →  should have {0,1,2,3}  →  missing: 2

Method 1 — Math: sum(0..n) - sum(nums)
    Expected sum = 0+1+2+3 = 6
    Actual sum   = 3+0+1   = 4
    Missing = 6 - 4 = 2  ★

Method 2 — XOR: XOR all indices and values. Pairs cancel out!
    XOR(0,1,2,3, 3,0,1) = 0^0 ^ 1^1 ^ 3^3 ^ 2 = 2  ★
"""
