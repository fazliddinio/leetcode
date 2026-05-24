"""
Intersection of Two Linked Lists
LeetCode 160

Approach: Two Pointers
Time: O(m + n) — Visit both lists.
Space: O(1) — Constant variable space.
Brute: O(m + n) / O(m) — Store all nodes of list A in a hash set, find first match in list B.
"""

from typing import Optional


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        ptrA, ptrB = (headA, headB)
        while ptrA != ptrB:
            ptrA = ptrA.next if ptrA else headB
            ptrB = ptrB.next if ptrB else headA
        return ptrA
