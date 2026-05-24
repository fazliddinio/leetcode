"""
Reverse Linked List II
LeetCode 92

Approach: Iterative (Sublist Reverse)
Time: O(n) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n) — Extract values into array, reverse the subarray, write back.
"""

from typing import Optional


class Solution:

    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next
        curr = prev.next
        for _ in range(right - left):
            temp = curr.next
            curr.next = temp.next
            temp.next = prev.next
            prev.next = temp
        return dummy.next
