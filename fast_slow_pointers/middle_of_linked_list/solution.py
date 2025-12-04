"""
# Middle of the Linked List

## Problem Description
Given the `head` of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.

## Approaches
1.  **Count Length** (Brute Force/Alternative): Traverse to find length `L`, then traverse to `L // 2`.
    *   Time Complexity: O(n) (Two passes)
    *   Space Complexity: O(1)
2.  **Fast & Slow Pointers** (Optimal): Use two pointers. When fast reaches end, slow is at middle.
    *   Time Complexity: O(n) (One pass)
    *   Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Optimal Solution: Fast & Slow Pointers
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds the middle node.
        
        Args:
            head: The head of the linked list.
            
        Returns:
            The middle node.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow

class SolutionCount:
    """
    Alternative Solution: Count Length
    """
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Finds middle via counting.
        
        Time Complexity: O(n)
        """
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        mid = length // 2
        curr = head
        for _ in range(mid):
            curr = curr.next
        return curr
