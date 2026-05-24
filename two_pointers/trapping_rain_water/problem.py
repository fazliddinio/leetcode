"""
==========================================
  Trapping Rain Water (LeetCode 42)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1: Input: height = [0,1,0,2,1,0,1,3,2,1,2,1], Output: 6
Explanation: The elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Constraints:
n == height.length, 1 <= n <= 2 * 10^4, 0 <= height[i] <= 10^5

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
You have a bunch of varying blocks on the ground. When it rains, water fills the valleys between the blocks. How much water gets stuck?

       #
   #   ## #
_#_##_######
[0,1,0,2,1,0,1,3,2,1,2,1]
Water fills the 6 gaps!

Method: Two Pointers (Left and Right bounds)
  The amount of water over any given block is determined by:
  `min(tallest_block_on_its_left, tallest_block_on_its_right) - its_own_height`

  To do this in O(1) space, put a pointer at `L=0` and `R=n-1`.
  Track `left_max` and `right_max`.
  If `left_max < right_max`:
      Water at L is strictly bound by `left_max`.
      Add `left_max - height[L]` to total water.
      Update `left_max`, move `L` forward.
  Else:
      Water at R is bounded by `right_max`.
      Add `right_max - height[R]` to total water.
      Update `right_max`, move `R` backwards.
"""
