"""
==========================================
  Middle of the Linked List (LeetCode 876)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

Example 1: Input: head = [1,2,3,4,5], Output: [3,4,5] (middle is 3)
Example 2: Input: head = [1,2,3,4,5,6], Output: [4,5,6] (second middle is 4)

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the middle node in one pass!

Method: Fast and Slow Pointers.
Imagine two runners again. Fast runs 2 steps, Slow runs 1 step.
By the time Fast reaches the end... Slow is exactly in the middle!

    Example: 1 -> 2 -> 3 -> 4 -> 5
    Round 1: S at 2, F at 3
    Round 2: S at 3, F at 5 (end) -> Middle is 3!
"""
