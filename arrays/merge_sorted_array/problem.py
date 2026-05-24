"""
==========================================
  Merge Sorted Array (LeetCode 88)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given two integer arrays `nums1` and `nums2`, sorted in
non-decreasing order, and two integers `m` and `n`, representing the
number of elements in `nums1` and `nums2` respectively.

Merge `nums2` into `nums1` as one sorted array.

The final sorted array should not be returned by the function, but instead
be stored inside the array `nums1`. To accommodate this, `nums1` has a
length of m + n, where the first m elements denote the elements that
should be merged, and the last n elements are set to 0 and should be
ignored. `nums2` has a length of n.

Example 1:
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]

Example 2:
    Input: nums1 = [1], m = 1, nums2 = [], n = 0
    Output: [1]

Constraints:
    - nums1.length == m + n
    - nums2.length == n
    - 0 <= m, n <= 200
    - -10^9 <= nums1[i], nums2[j] <= 10^9


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

You have two sorted rows of people by height. Merge them into one sorted row.
The twist: do it INSIDE the first row (which has empty spots at the end).

    nums1 = [1, 2, 3, _, _, _]    (3 real numbers + 3 empty slots)
    nums2 = [2, 5, 6]

Trick: Fill from the END! Compare the largest elements from each array.

    Step 1: Compare 3 vs 6 → 6 is bigger → place 6 at end
            [1, 2, 3, _, _, 6]

    Step 2: Compare 3 vs 5 → 5 is bigger → place 5
            [1, 2, 3, _, 5, 6]

    Step 3: Compare 3 vs 2 → 3 is bigger → place 3
            [1, 2, _, 3, 5, 6]

    Step 4: Compare 2 vs 2 → equal → place nums2's 2
            [1, 2, 2, 3, 5, 6]

    Done! nums2 is exhausted.

    Result: [1, 2, 2, 3, 5, 6]

Why fill from the end?
  → We won't overwrite numbers we still need!
"""
