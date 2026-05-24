"""
==========================================
  Reorder List (LeetCode 143)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln

Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example 1: Input: head = [1,2,3,4], Output: [1,4,2,3]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Zip the first half of a linked list with the REVERSED second half!

    1 -> 2 -> 3 -> 4 -> 5
    Head takes 1, tail takes 5.
    1 -> 5 -> 2 -> 4 -> 3

Method: Three Steps
  1. Find the middle of the linked list using Fast and Slow pointers.
  2. Reverse the entire second half of the linked list (starting from Middle).
  3. Weave them together!
     - Take one from the first half, link to one from the reversed second half.
     - Move pointers forward and repeat.
"""
