"""
==========================================
  Intersection of Two Arrays II (LeetCode 350)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given two integer arrays `nums1` and `nums2`, return an array of their
intersection. Each element in the result must appear as many times as it
shows in both arrays and you may return the result in any order.

Example 1:
    Input: nums1 = [1,2,2,1], nums2 = [2,2]
    Output: [2,2]

Example 2:
    Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
    Output: [4,9]
    Explanation: [9,4] is also accepted.

Constraints:
    - 1 <= nums1.length, nums2.length <= 1000
    - 0 <= nums1[i], nums2[i] <= 1000

Follow up:
    - What if the given array is already sorted?
    - What if nums1's size is small compared to nums2's size?
    - What if elements of nums2 are stored on disk?


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

You have two lists. Find the numbers that appear in BOTH lists.
If a number appears twice in both, include it twice.

    List A: [1, 2, 2, 1]
    List B: [2, 2]

    Which numbers are in both?
    - 1 is in A but NOT in B  → skip
    - 2 is in both A and B   → include
    - 2 is in both (again)   → include again

    Answer: [2, 2]

Think of it like matching socks:

    Drawer A: 🧦1  🧦2  🧦2  🧦1
    Drawer B: 🧦2  🧦2

    Pairs that match: 🧦2  🧦2

How to solve:
  1. Count how many of each number is in List A (use a dictionary).
  2. Go through List B. If a number is in the dictionary with count > 0,
     add it to result and decrease the count.

    Count of A: {1: 2, 2: 2}
    Check B[0]=2 → count[2]=2 > 0 → result=[2], count[2]=1
    Check B[1]=2 → count[2]=1 > 0 → result=[2,2], count[2]=0

Answer: [2, 2]
"""
