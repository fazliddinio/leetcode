"""
Split Linked List in Parts
LeetCode 725

Approach: Calculate Length & Split
Time: O(n) — Single pass (or two passes).
Space: O(1) — Output array not counted.
Brute: O(n) — Collect all nodes into array, then slice and relink.
"""

from typing import List, Optional


class Solution:

    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr = head
        length = 0
        while curr:
            curr = curr.next
            length += 1
        base_size = length // k
        remainder = length % k
        res = []
        curr = head
        for i in range(k):
            res.append(curr)
            part_size = base_size + (1 if remainder > 0 else 0)
            remainder -= 1
            for j in range(part_size - 1):
                if curr:
                    curr = curr.next
            if curr:
                nxt = curr.next
                curr.next = None
                curr = nxt
        return res
