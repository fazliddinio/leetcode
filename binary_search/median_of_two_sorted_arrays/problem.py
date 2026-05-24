"""
==========================================
  Median of Two Sorted Arrays (LeetCode 4)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given two sorted arrays `nums1` and `nums2` of size m and n respectively,
return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
    Input: nums1 = [1,3], nums2 = [2]
    Output: 2.00000

Example 2:
    Input: nums1 = [1,2], nums2 = [3,4]
    Output: 2.50000

Constraints:
    - nums1.length == m, nums2.length == n
    - 0 <= m <= 1000, 0 <= n <= 1000
    - 1 <= m + n <= 2000
    - -10^6 <= nums1[i], nums2[i] <= 10^6


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Find the MIDDLE value if you merged both sorted arrays.

    nums1 = [1, 3]    nums2 = [2]
    Merged: [1, 2, 3]  →  median = 2

    nums1 = [1, 2]    nums2 = [3, 4]
    Merged: [1, 2, 3, 4]  →  median = (2+3)/2 = 2.5

But merging takes O(m+n). Can we do O(log(m+n))?

The trick: Binary search on the PARTITION point.
    We want to split both arrays so that:
    - Left side has exactly half the total elements
    - Everything on left ≤ everything on right

    nums1 = [1, 3]     nums2 = [2]
    Total = 3, half = 2

    Try partition: nums1 takes 1 element, nums2 takes 1 element:
    Left:  [1] [2]     Right: [3]
    max(left)=2, min(right)=3
    2 ≤ 3 ✓ → median = max(left) = 2

It's like finding where to "cut" two sorted ropes so the left pile
weighs the same as the right pile.
"""
