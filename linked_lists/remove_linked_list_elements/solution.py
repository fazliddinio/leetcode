"""
Remove Linked List Elements
LeetCode 203

Approach: Iterative
Time: O(n) — Single pass.
Space: O(1) — In-place removal.
Brute: O(n) — Recursive approach removing matching nodes via recursion stack.
"""

from typing import Optional


class Solution:

    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
        return dummy.next
