"""
Partition List
LeetCode 86

Approach: Two Pointers (Less/Greater)
Time: O(n) — Single pass.
Space: O(1) — Reorder in-place.
Brute: O(n) — Collect values into array, partition by threshold, write back.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_head = ListNode(0)
        less = less_head
        greater_head = ListNode(0)
        greater = greater_head
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                greater.next = head
                greater = greater.next
            head = head.next
        greater.next = None
        less.next = greater_head.next
        return less_head.next
