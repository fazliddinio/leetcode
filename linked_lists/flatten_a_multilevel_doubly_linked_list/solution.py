"""
Flatten a Multilevel Doubly Linked List
LeetCode 430

Approach: Iterative (Inline Stitching)
Time: O(n) — Each node visited at most twice.
Space: O(1) — No extra data structures.
Brute: O(n) — Recursive DFS flattening child subtrees then stitching back.
"""

from typing import Optional


class Solution:

    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        while curr:
            if curr.child:
                child = curr.child
                tail = child
                while tail.next:
                    tail = tail.next
                tail.next = curr.next
                if curr.next:
                    curr.next.prev = tail
                curr.next = child
                child.prev = curr
                curr.child = None
            curr = curr.next
        return head
