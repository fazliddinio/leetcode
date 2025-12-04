"""
# Intersection of Two Linked Lists

## Problem Description
Given the heads of two singly linked-lists `headA` and `headB`, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return `null`.

## Approaches
1.  **Hash Set** (Brute Force/Alternative): Store nodes of list A in a set, check list B nodes against it.
    *   Time Complexity: O(n + m)
    *   Space Complexity: O(n)
2.  **Two Pointers** (Optimal): Iterate both lists. When one ends, switch to other list's head.
    *   Time Complexity: O(n + m)
    *   Space Complexity: O(1)
"""

from typing import Optional, Set

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Optimal Solution: Two Pointers
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Finds intersection using O(1) space.
        
        Args:
            headA: Head of list A.
            headB: Head of list B.
            
        Returns:
            The intersected node if present, else None.
            
        Time Complexity: O(m + n)
        Space Complexity: O(1)
        """
        if not headA or not headB:
            return None
            
        l1, l2 = headA, headB
        while l1 != l2:
            l1 = l1.next if l1 else headB
            l2 = l2.next if l2 else headA
        return l1

class SolutionSet:
    """
    Alternative Solution: Hash Set
    """
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        """
        Finds intersection using hash set.
        
        Time Complexity: O(n + m)
        Space Complexity: O(n)
        """
        nodes_a = set()
        curr = headA
        while curr:
            nodes_a.add(curr)
            curr = curr.next
            
        curr = headB
        while curr:
            if curr in nodes_a:
                return curr
            curr = curr.next
        return None
