"""
Remove Duplicates from Sorted List II
LeetCode 82

Approach: Iterative (Dummy Node)
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n) — Count occurrences with a counter, keep only values appearing once.
"""

from typing import Optional


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return dummy.next
