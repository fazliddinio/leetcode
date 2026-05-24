"""
Swap Nodes in Pairs
LeetCode 24

Approach: Iterative (Pointer Swap)
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n) / O(n) — Recursive approach swapping first pair then recursing on the rest.
"""

from typing import Optional


class Solution:

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            first = head
            second = head.next
            prev.next = second
            first.next = second.next
            second.next = first
            prev = first
            head = first.next
        return dummy.next
