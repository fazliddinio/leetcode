"""
==========================================
  Find Peak Element (LeetCode 162)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array `nums`, find a peak element, and return
its index. If the array contains multiple peaks, return the index to any
of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element
is always considered to be strictly greater than a neighbor that is
outside the array.

You must write an algorithm that runs in O(log n) time.

Example 1:
    Input: nums = [1,2,3,1]
    Output: 2
    Explanation: 3 is a peak element at index 2.

Example 2:
    Input: nums = [1,2,1,3,5,6,4]
    Output: 5
    Explanation: Either index 2 or 5. 6 is a peak at index 5.

Constraints:
    - 1 <= nums.length <= 1000
    - -2^31 <= nums[i] <= 2^31 - 1
    - nums[i] != nums[i + 1] for all valid i.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Find ANY peak — a number bigger than both its neighbors.

    [1, 2, 1, 3, 5, 6, 4]
        ↑              ↑
       peak           peak
    (2>1, 2>1)      (6>5, 6>4)

Why binary search works:
    If nums[mid] < nums[mid+1], there MUST be a peak to the RIGHT.
    (Because the array goes up, and eventually must come down or hit the edge)

    [1, 2, 1, 3, 5, 6, 4]
              ↑ mid
              3 < 5 → go RIGHT (uphill = peak ahead!)
    [5, 6, 4]
     ↑ mid
     6 > 5 and 6 > 4 → peak found at index 5!

It's like climbing a hill blindfolded:
    - Feel the slope: going up? Keep going that way.
    - You'll eventually reach a top! 🏔️
"""
