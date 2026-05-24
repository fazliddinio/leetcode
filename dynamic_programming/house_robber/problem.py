"""
==========================================
  House Robber (LeetCode 198)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1: Input: nums = [1,2,3,1], Output: 4
Example 2: Input: nums = [2,7,9,3,1], Output: 12

Constraints: 1 <= nums.length <= 100, 0 <= nums[i] <= 400

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Rob houses to get max money, but you CANNOT rob two adjacent houses!

    nums = [1, 2, 3, 1]
    Rob 1st (1) + 3rd (3) = 4

How to solve:
At each house, the robber decides:
  1. Rob this house (and add money from 2 houses ago)
  2. Skip this house (and keep money from previous house)

Formula: `dp[i] = max(rob_current + dp[i-2], skip_current + dp[i-1])`
Since we only need the last two values, we can optimize space to O(1) by keeping track of `rob1` and `rob2`.
"""
