"""
# Copy List with Random Pointer

## Problem Description
A linked list of length `n` is given such that each node contains an additional random pointer, which could point to any node in the list, or `null`.
Construct a deep copy of the list.

## Approaches
1.  **Hash Map** (Original/Alternative): Use a map to store `old_node -> new_node`.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
2.  **Interleaving** (Optimal): Create copy nodes next to original nodes. `A -> A' -> B -> B'`. Then link randoms. Then separate.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1) (excluding result)
"""

from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random

class Solution:
    """
    Optimal Solution: Interleaving
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Deep copies using O(1) extra space.
        
        Args:
            head: The head of the linked list.
            
        Returns:
            The head of the copied linked list.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return None
            
        # 1. Interleave
        cur = head
        while cur:
            copy = Node(cur.val, cur.next)
            cur.next = copy
            cur = copy.next
            
        # 2. Link Randoms
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            
        # 3. Separate
        cur = head
        copyHead = head.next
        while cur:
            copy = cur.next
            cur.next = copy.next
            if copy.next:
                copy.next = copy.next.next
            cur = cur.next
            
        return copyHead

class SolutionMap:
    """
    Alternative Solution: Hash Map
    """
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        Deep copies using Hash Map.
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        oldToCopy = {None: None}
        
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
            
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
            
        return oldToCopy[head]
