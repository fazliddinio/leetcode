"""
Sort List
LeetCode 148

Approach: Merge Sort (Top-Down)
Time: O(N log N) — Standard merge sort.
Space: O(log N) — Recursion stack.
Brute: O(N log N) / O(N) — Collect all values into array, sort, write back to list.
"""

from typing import Optional


class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        mid = self.getMid(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.sortList(left)
        right = self.sortList(right)
        return self.merge(left, right)

    def getMid(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def merge(self, left, right):
        dummy = ListNode()
        curr = dummy
        while left and right:
            if left.val <= right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        curr.next = left if left else right
        return dummy.next
