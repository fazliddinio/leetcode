"""
Copy List with Random Pointer
LeetCode 138

Approach: Hash Map
Time: O(n) — Two passes (create mapping, then link).
Space: O(n) — Map stores mapping from old to new nodes.
Brute: O(n) — Interleave copies between originals, link random pointers, then separate.
"""

from typing import Optional


class Solution:

    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None
        old_to_new = {}
        current = head
        while current:
            old_to_new[current] = Node(current.val)
            current = current.next
        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)
            current = current.next
        return old_to_new[head]
