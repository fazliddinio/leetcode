"""
==========================================
  Container With Most Water (LeetCode 11)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Example 1: Input: height = [1,8,6,2,5,4,8,3,7], Output: 49
Explanation: The vertical lines at index 1 and 8 form a container. Height = min(8,7)=7, Width = 8-1=7. Area = 7*7 = 49.
Example 2: Input: height = [1,1], Output: 1

Constraints: n == height.length, 2 <= n <= 10^5, 0 <= height[i] <= 10^4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Imagine a bunch of walls of varying heights. You want to pick exactly two walls to act as the sides of a fish tank.
Your goal is to hold the MOST water.

    8 |   #                   #
    7 |   #                   #      #
    6 |   #   #               #      #
    5 |   #   #       #       #      #
    4 |   #   #       #   #   #      #
    3 |   #   #       #   #   #   #  #
    2 |   #   #   #   #   #   #   #  #
    1 | # #   #   #   #   #   #   #  #
      0 1 2 3 4 5 6 7 8 9
      (Wall indices on the bottom)

Water is limited by the SHORTER of the two walls (otherwise it spills).
So Area = `min(height[left], height[right]) * (right - left)`.

Method: Two Pointers (Outside In)
  Start with the widest container: Left at 0, Right at end.
  Calculate the area and save the maximum.
  To find a bigger area, the ONLY way is to find a taller wall.
  So, whichever wall is shorter right now, abandon it!
  Move the shorter pointer inward.
"""
