"""
==========================================
  Linked List Cycle II (LeetCode 142)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.

Example: Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
Output: tail connects to node index 1

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find exactly WHERE the circle track begins!

Method:
  Step 1: Use Floyd's Tortoise and Hare to find if a cycle exists (fast stops at slow).
  Step 2: Reset slow back to `head`. Move BOTH one step at a time! Where they meet again is the start of the loop.

Why?
  Because of math. Distance from head to cycle start is exactly the same as distance from the meeting point to cycle start!
"""
