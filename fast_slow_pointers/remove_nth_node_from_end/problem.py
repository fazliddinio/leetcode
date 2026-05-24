"""
==========================================
  Remove Nth Node From End of List (LeetCode 19)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1: Input: head = [1,2,3,4,5], n = 2, Output: [1,2,3,5]
Example 2: Input: head = [1], n = 1, Output: []

Constraints: The number of nodes in the list is sz. 1 <= sz <= 30, 0 <= Node.val <= 100, 1 <= n <= sz

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Remove the N-th node counting strictly from the END of a linked list. Do it in one pass!

    List: 1 -> 2 -> 3 -> 4 -> 5, n = 2
    2nd from end is 4.
    List: 1 -> 2 -> 3 -> 5

Method: Fast & Slow Pointers (Gap)
  1. We need a gap of exactly `n` nodes between a Fast pointer and a Slow pointer.
  2. Move `Fast` forward `n` times.
  3. Now move BOTH `Fast` and `Slow` forward step-by-step.
  4. When `Fast` hits the very end (null), `Slow` is exactly *at the node right before the one to delete*.
  5. Just redirect `Slow.next` to `Slow.next.next`!
  *Note: Use a dummy node at the beginning to handle edge cases where you delete the original head.*
"""
