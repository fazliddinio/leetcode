"""
Add Two Numbers
LeetCode 2

Approach: Iterative Addition
Time: O(max(m, n)) — Single pass.
Space: O(max(m, n)) — Output list size.
Brute: O(max(m, n)) — Convert lists to integers, add, then convert sum back to list.
"""

from typing import Optional


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        carry = 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next
