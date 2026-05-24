"""
Palindrome Linked List
LeetCode 234

Approach: Reverse Second Half
Time: O(n) — find middle + reverse + compare
Space: O(1) — in-place reverse
Brute: O(n) — copy values to array and check with two pointers using O(n) space
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node

        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True
