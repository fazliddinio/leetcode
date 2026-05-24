"""
==========================================
  Linked List Cycle (LeetCode 141)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given head, the head of a linked list, determine if the linked list has a cycle in it.
Return true if there is a cycle in the linked list. Otherwise, return false.

Example: Input: head = [3,2,0,-4], pos = 1 (tail connects to node index 1)
Output: true

Constraints: The number of the nodes in the list is in the range [0, 10^4].

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Does the linked list loop endlessly in a circle?

Method: Fast and Slow Pointers (Floyd's Tortoise and Hare algorithm).
Imagine two runners on a track. One runs fast (2 steps at a time), one runs slow (1 step).

    If there is a cycle (circle track): The fast runner will eventually LAP the slow runner (they meet).
    If no cycle (straight track): The fast runner hits the end (null).

Implementation:
    slow = head, fast = head
    While fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        If slow == fast: return True!
"""
