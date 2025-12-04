"""
# Reverse Linked List

## Problem Description
Given the `head` of a singly linked list, reverse the list, and return the reversed list.

## Approaches
1.  **Iterative** (Optimal): Use `prev`, `curr` pointers to reverse links in place.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
2.  **Recursive** (Alternative): Recursively reverse the rest of the list and link new next.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n) (Stack space)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Optimal Solution: Iterative
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses a singly linked list iteratively.
        
        Args:
            head: The head of the linked list.
            
        Returns:
            The head of the reversed linked list.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

class SolutionRecursive:
    """
    Alternative Solution: Recursive
    """
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverses utilizing recursion stack.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head or not head.next:
            return head
        
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res
