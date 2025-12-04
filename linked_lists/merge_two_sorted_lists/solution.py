"""
# Merge Two Sorted Lists

## Problem Description
You are given the heads of two sorted linked lists `list1` and `list2`.
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

## Approaches
1.  **Iterative** (Optimal): Use a dummy node and a current pointer to build the new list.
    *   Time Complexity: O(n + m)
    *   Space Complexity: O(1)
2.  **Recursive** (Alternative): Recursively decide which node is smaller and attach the rest.
    *   Time Complexity: O(n + m)
    *   Space Complexity: O(n + m) (Stack space)
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two sorted linked lists iteratively.
        
        Args:
            list1: Head of the first sorted linked list.
            list2: Head of the second sorted linked list.
            
        Returns:
            Head of the merged sorted linked list.
            
        Time Complexity: O(n + m)
        Space Complexity: O(1)
        """
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2
            
        return dummy.next

class SolutionRecursive:
    """
    Alternative Solution: Recursive
    """
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges using recursion.
        
        Time Complexity: O(n + m)
        Space Complexity: O(n + m)
        """
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
