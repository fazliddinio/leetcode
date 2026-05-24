"""
==========================================
  Find K Closest Elements (LeetCode 658)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given a sorted integer array `arr`, two integers `k` and `x`, return the
`k` closest integers to `x` in the array. The result should also be
sorted in ascending order.

An integer `a` is closer to `x` than an integer `b` if:
    |a - x| < |b - x|, or
    |a - x| == |b - x| and a < b

Example 1:
    Input: arr = [1,2,3,4,5], k = 4, x = 3
    Output: [1,2,3,4]

Example 2:
    Input: arr = [1,1,2,3,4,5], k = 4, x = -1
    Output: [1,1,2,3]

Constraints:
    - 1 <= k <= arr.length
    - 1 <= arr.length <= 10^4
    - arr is sorted in ascending order.
    - -10^4 <= arr[i], x <= 10^4


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

From a sorted list, find the k numbers closest to x.

    arr = [1, 2, 3, 4, 5],  k=4,  x=3

    Distance from 3:
    |1-3|=2  |2-3|=1  |3-3|=0  |4-3|=1  |5-3|=2

    Pick 4 closest: [1, 2, 3, 4]  (1 ties with 5, pick smaller)

Think of it as a sliding window of size k:
    [1,2,3,4] 5     ← window starts here
    1 [2,3,4,5]     ← or here?

Binary search for the LEFT edge of the window:
    Compare arr[mid] and arr[mid+k]:
    - If x - arr[mid] > arr[mid+k] - x → shrink from left
    - Otherwise → shrink from right

    The window that's "pulled closer" to x wins!
"""
