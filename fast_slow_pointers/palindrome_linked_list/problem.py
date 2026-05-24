"""
==========================================
  Palindrome Linked List (LeetCode 234)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

Example 1: Input: head = [1,2,2,1], Output: true
Example 2: Input: head = [1,2], Output: false

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Is the linked list the same backwards as forwards?

    List: 1 -> 2 -> 2 -> 1 (Yes!)

Method:
  Step 1: Find the middle using Fast/Slow pointers.
  Step 2: REVERSE the second half of the linked list in place.
          `1 -> 2` and `1 -> 2`
  Step 3: Compare both halves step by step.
  Step 4: (Optional) Restore the reversed half to keep the input pristine.
"""
