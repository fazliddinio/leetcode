"""
# Reorder List

## Problem Description
You are given the head of a singly linked-list. The list can be represented as:
L0 -> L1 -> ... -> Ln - 1 -> Ln
Reorder the list to be on the following form:
L0 -> Ln -> L1 -> Ln - 1 -> L2 -> Ln - 2 -> ...
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

## Approaches
1.  **Array/Deque** (Brute Force/Alternative): Store nodes in array/deque, pop from ends to reconstruct.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
2.  **Reverse Second Half** (Optimal): Find middle, reverse second half, merge two sorted lists.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Optimal Solution: Reverse Second Half
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders list in-place using O(1) space.
        
        Args:
            head: The head of the linked list.
            
        Returns:
            None.
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return
            
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        second = slow.next
        slow.next = None # split
        prev = None
        
        # reverse second
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
            
        # merge
        second = prev
        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

class SolutionArray:
    """
    Alternative Solution: Array
    """
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorders using array.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head: return
        
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
            
        l, r = 0, len(nodes) - 1
        last = head  # dummy start
        
        while l <= r:
            if l == r:
                last.next = nodes[l]
                last = nodes[l]
                break
            
            nodes[l].next = nodes[r]
            last.next = nodes[l]
            last = nodes[r]
            
            l += 1
            r -= 1
        last.next = None
        # Head is already nodes[0], check if we broke cycle correctly relative to head.
        # Actually logic is: if we just change pointers:
        # L0 -> Ln -> L1 ...
        # My logic above is slightly messy with 'last'.
        # Let's simple reconstruct:
        
        l, r = 0, len(nodes) - 1
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            if l == r:
                nodes[r].next = None
                break
            nodes[r].next = nodes[l]
            r -= 1
        nodes[l].next = None
