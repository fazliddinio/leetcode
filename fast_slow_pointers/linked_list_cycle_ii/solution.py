"""
Linked List Cycle II
LeetCode 142

Approach: Floyd's Cycle Detection Algorithm
Time: O(n) — linear scan
Space: O(1) — constant variable space
Brute: O(n) — store visited nodes in hash set using O(n) space
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                slow = head
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None
