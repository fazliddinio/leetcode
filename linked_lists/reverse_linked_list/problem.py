"""
==========================================
  Reverse Linked List (LeetCode 206)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given the head of a singly linked list, reverse the list, and return the reversed list.

Example 1: Input: head = [1,2,3,4,5], Output: [5,4,3,2,1]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Flip all arrows in the linked list around so it goes backwards.

    Before: 1 -> 2 -> 3 -> null
    After:  null <- 1 <- 2 <- 3

Method: Iterative approach. You need 3 pointers (prev, curr, next).
  1. Save `curr.next` to `next_node`.
  2. Aim `curr.next` backwards at `prev`.
  3. Slide `prev` forward to `curr`.
  4. Slide `curr` forward to `next_node`.
  Repeat until `curr` is null! Return `prev` as the new head.
"""
