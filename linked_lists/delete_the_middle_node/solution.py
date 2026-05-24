"""
Delete the Middle Node of a Linked List
LeetCode 2095

Approach: Fast & Slow Pointers
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n) — Two-pass approach counting length first, then walking to middle.
"""

from typing import Optional


class Solution:

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        slow = head
        fast = head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        slow.next = slow.next.next
        return head
