"""
Reverse Nodes in k-Group
LeetCode 25

Approach: Iterative
Time: O(n) — Single pass (each node visited twice at most).
Space: O(1) — Constant variable space.
Brute: O(n) — Collect values into array, reverse k-sized chunks, write back.
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head
        dummy = ListNode(0, head)
        prev_group_end = dummy
        while True:
            kth = self.getKth(prev_group_end, k)
            if not kth:
                break
            group_start = prev_group_end.next
            next_group_start = kth.next
            kth.next = None
            self.reverse(group_start)
            prev_group_end.next = kth
            group_start.next = next_group_start
            prev_group_end = group_start
        return dummy.next

    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr

    def reverse(self, head):
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
