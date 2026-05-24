"""
==========================================
  House Robber II (LeetCode 213)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1: Input: nums = [2,3,2], Output: 3
Example 2: Input: nums = [1,2,3,1], Output: 4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Same as House Robber, but the houses are in a CIRCLE.
This means you cannot rob BOTH the first house and the last house!

    nums = [2, 3, 2]
    Rob 1st (2) -> Cannot rob 3rd (2) because they are connected! Output: 3 (just rob the middle)

Trick: Break the circle into two lines and run normal House Robber twice!
  1. Houses from 0 to n-2 (skip the last house)
  2. Houses from 1 to n-1 (skip the first house)

Return the maximum of those two scenarios! (Handle `len(nums) == 1` as a special edge case).
"""
