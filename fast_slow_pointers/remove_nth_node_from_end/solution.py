"""
# Remove Nth Node From End of List

## Problem Description
Given the `head` of a linked list, remove the `n`-th node from the end of the list and return its head.

## Approaches
1.  **Two Pass** (Brute Force/Alternative): Count length `L`, then remove `(L-n+1)`-th node.
    *   Time Complexity: O(n) (Traverse twice)
    *   Space Complexity: O(1)
2.  **One Pass** (Optimal): Use two pointers with a gap of `n`.
    *   Time Complexity: O(n) (Traverse once)
    *   Space Complexity: O(1)
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    Optimal Solution: One Pass (Two Pointers)
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes Nth node from end in one pass.
        
        Args:
            head: The head of the linked list.
            n: The position from the end to remove.
            
        Returns:
            The head of the modified linked list.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        while n > 0 and right:
            right = right.next
            n -= 1
            
        while right:
            left = left.next
            right = right.next
            
        left.next = left.next.next
        return dummy.next

class SolutionTwoPass:
    """
    Alternative Solution: Two Pass
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes Nth node via counting.
        
        Time Complexity: O(n)
        """
        dummy = ListNode(0, head)
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
            
        target_step = length - n
        curr = dummy
        for _ in range(target_step):
            curr = curr.next
            
        curr.next = curr.next.next
        return dummy.next
