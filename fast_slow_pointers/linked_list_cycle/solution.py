"""
Linked List Cycle
LeetCode 141

Approach: Floyd's Tortoise and Hare
Time: O(n) — linear scan
Space: O(1) — constant variable space
Brute: O(n) — store visited nodes in a hash set using O(n) space
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
