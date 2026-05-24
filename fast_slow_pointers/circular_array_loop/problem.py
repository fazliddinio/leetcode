"""
==========================================
  Circular Array Loop (LeetCode 457)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are playing a game involving a circular array of non-zero integers nums. Each nums[i] denotes the number of indices forward/backward you must move if you are located at index i.
Return true if there is a cycle in nums, or false otherwise.
A cycle must follow these constraints:
- It involves at least two elements.
- The directions of the movements are all the same (all forward or all backward).

Example 1: Input: nums = [2,-1,1,2,2], Output: true
Example 2: Input: nums = [-1,-2,-3,-4,-5,6], Output: false

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Jump through an array by treating numbers as steps. If you land on `2`, jump 2 spaces right. If `-1`, jump 1 space left.
Does this create a valid infinite loop? (Must be all same direction, > 1 node).

Method: Fast & Slow Pointers
  For every unvisited node, launch a Fast and Slow pointer.
  When advancing, use `(index + nums[index]) % len(nums)` to wrap around.
  If the direction changes (positive becomes negative) or you hit a cycle of length 1 (nums[i] % len == 0), the loop is invalid!
  If `Slow == Fast`, you found a valid cycle!
"""
