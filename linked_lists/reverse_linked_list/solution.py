"""
Reverse Linked List
LeetCode 206

Approach: Iterative
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n) — Recursive approach reversing from the tail back.
"""

from typing import Optional


class Solution:

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
