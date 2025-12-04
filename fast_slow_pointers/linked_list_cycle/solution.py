"""
# Linked List Cycle

## Problem Description
Given `head`, the head of a linked list, determine if the linked list has a cycle in it.
Return `true` if there is a cycle in the linked list. Otherwise, return `false`.

## Approaches
1.  **Hash Set** (Brute Force/Alternative): Store visited nodes in a set. If we see a node again, cycle exists.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
2.  **Fast & Slow Pointers** (Optimal): Use two pointers moving at different speeds. If they meet, cycle exists.
    *   Time Complexity: O(n)
    *   Space Complexity: O(1)
"""

from typing import Optional, Set

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Optimal Solution: Fast & Slow Pointers
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Determines if a linked list has a cycle in it using two pointers.
        
        Args:
            head: The head of the linked list.
            
        Returns:
            True if there is a cycle, False otherwise.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return False
            
        slow, fast = head, head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

class SolutionSet:
    """
    Alternative Solution: Hash Set
    """
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Detects cycle using hash set.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        visited = set()
        curr = head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False
