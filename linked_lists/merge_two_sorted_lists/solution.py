"""
Merge Two Sorted Lists
LeetCode 21

Approach: Iterative
Time: O(n + m) — Single pass.
Space: O(1) — Constant variable space.
Brute: O(n + m) — Recursive approach choosing the smaller head each call.
"""

from typing import Optional


class Solution:

    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2
        return dummy.next
