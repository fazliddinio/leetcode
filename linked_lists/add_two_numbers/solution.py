"""
# Add Two Numbers

## Problem Description
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

## Approaches
1.  **Iterative** (Optimal): Traverse both lists, adding values and managing carry.
    *   Time Complexity: O(max(n, m))
    *   Space Complexity: O(max(n, m)) (for the result list)
2.  **Recursive** (Alternative): Recursively add nodes.
    *   Time Complexity: O(max(n, m))
    *   Space Complexity: O(max(n, m)) (Stack space + result)
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
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Adds two numbers represented by linked lists.
        
        Args:
            l1: Head of the first linked list.
            l2: Head of the second linked list.
            
        Returns:
            Head of the linked list representing the sum.
            
        Time Complexity: O(max(n, m))
        Space Complexity: O(max(n, m))
        """
        dummy = ListNode()
        curr = dummy
        
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            # new digit
            val = v1 + v2 + carry
            carry = val // 10
            val = val % 10
            curr.next = ListNode(val)
            
            # update ptrs
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next

class SolutionRecursive:
    """
    Alternative Solution: Recursive
    """
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry: int = 0) -> Optional[ListNode]:
        """
        Adds two numbers recursively.
        
        Time Complexity: O(max(n, m))
        Space Complexity: O(max(n, m))
        """
        if not l1 and not l2 and not carry:
            return None
        
        v1 = l1.val if l1 else 0
        v2 = l2.val if l2 else 0
        val = v1 + v2 + carry
        
        node = ListNode(val % 10)
        
        next_l1 = l1.next if l1 else None
        next_l2 = l2.next if l2 else None
        
        node.next = self.addTwoNumbers(next_l1, next_l2, val // 10)
        return node
