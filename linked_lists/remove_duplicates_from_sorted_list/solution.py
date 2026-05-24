"""
Remove Duplicates from Sorted List
LeetCode 83

Approach: Iterative
Time: O(n) — Single pass.
Space: O(1) — In-place removal.
Brute: O(n) — Recursive approach skipping duplicates by comparing current with next.
"""

from typing import Optional


class Solution:

    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
