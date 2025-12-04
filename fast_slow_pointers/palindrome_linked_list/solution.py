"""
# Palindrome Linked List

## Problem Description
Given the `head` of a singly linked list, return `true` if it is a palindrome.

## Approaches
1.  **Array/List** (Brute Force/Alternative): Copy Linked List to an array and check if array is palindrome.
    *   Time Complexity: O(n)
    *   Space Complexity: O(n)
2.  **Fast & Slow Pointers** (Optimal): Find middle, reverse second half, and compare.
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
    Optimal Solution: Fast & Slow Pointers + Reverse
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Checks palindrome using O(1) space.
        
        Args:
            head: The head of the linked list.
            
        Returns:
            True if palindrome, False otherwise.
            
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        fast = head
        slow = head
        
        # Find middle (slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        # Reverse second half
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
            
        # Check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True

class SolutionArray:
    """
    Alternative Solution: Copy to Array
    """
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        Checks palindrome using O(n) space.
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals == vals[::-1]
