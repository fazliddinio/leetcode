"""
Remove Nth Node From End of List
LeetCode 19

Approach: Two Pointers (one pass)
Time: O(n) — single pass
Space: O(1) — constant variable space
Brute: O(n) — two passes: count total nodes, then traverse to target
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        left = right = dummy

        for _ in range(n + 1):
            right = right.next

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next
