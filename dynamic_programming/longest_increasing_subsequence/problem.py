"""
==========================================
  Longest Increasing Subsequence (LeetCode 300)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer array nums, return the length of the longest strictly increasing subsequence.

Example 1: Input: nums = [10,9,2,5,3,7,101,18], Output: 4
Example 2: Input: nums = [0,1,0,3,2,3], Output: 4
Example 3: Input: nums = [7,7,7,7,7,7,7], Output: 1

Constraints: 1 <= nums.length <= 2500, -10^4 <= nums[i] <= 10^4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the longest sequence of numbers that strictly go up (can skip numbers).

    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    Longest: [2, 3, 7, 101] or [2, 5, 7, 18]  (length 4)

O(N^2) DP Approach:
`dp[i]` stores the max length ending at index `i`.
Initialize `dp` with 1s.
For each number, look back at all smaller numbers before it, and add 1 to their `dp` value.

    nums = [2, 5, 3, 7]
    dp   = [1, 2, 2, 3]  (7 can add itself to either 5 or 3's sequence)
"""
