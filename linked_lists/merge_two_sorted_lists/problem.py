"""
==========================================
  Merge Two Sorted Lists (LeetCode 21)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.

Example 1: Input: list1 = [1,2,4], list2 = [1,3,4], Output: [1,1,2,3,4,4]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Zip two sorted linked lists together!

    List 1: 1 -> 2 -> 4
    List 2: 1 -> 3 -> 4

Method: Use a dummy head node.
  Maintain a `tail` pointer.
  Compare the current nodes of `list1` and `list2`.
  Point `tail.next` to the smaller one and move that list forward.
  When one list hits null, just point `tail.next` to the entire remaining other list!
"""
