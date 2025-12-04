"""
# Remove Duplicates from Sorted List

## Problem Description
Given the `head` of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

## Approaches
1.  **Iterative** (Optimal): Iterate and skip duplicates.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
2.  **Recursive** (Alternative): Recursively process and return head.
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
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes all duplicates iteratively.
        
        Args:
            head: The head of the sorted linked list.
            
        Returns:
            The head of the modified linked list.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        cur = head
        while cur:
            while cur.next and cur.next.val == cur.val:
                cur.next = cur.next.next
            cur = cur.next
        return head

class SolutionRecursive:
    """
    Alternative Solution: Recursive
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Deletes duplicates recursively.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        if not head or not head.next:
            return head
        
        head.next = self.deleteDuplicates(head.next)
        
        if head.val == head.next.val:
            return head.next
        else:
            return head
