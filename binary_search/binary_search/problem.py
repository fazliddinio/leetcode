"""
==========================================
  Binary Search (LeetCode 704)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an array of integers `nums` which is sorted in ascending order, and
an integer `target`, write a function to search `target` in `nums`. If
`target` exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [-1,0,3,5,9,12], target = 9
    Output: 4
    Explanation: 9 exists in nums and its index is 4.

Example 2:
    Input: nums = [-1,0,3,5,9,12], target = 2
    Output: -1
    Explanation: 2 does not exist in nums so return -1.

Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 < nums[i], target < 10^4
    - All the integers in nums are unique.
    - nums is sorted in ascending order.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Find a number in a SORTED list. You can do it fast by always checking
the middle.

    nums = [-1, 0, 3, 5, 9, 12]   target = 9

    Think of it like guessing a number:

    Step 1: Check middle (index 2, value 3)
            [-1, 0, [3], 5, 9, 12]
            3 < 9 → target is in the RIGHT half

    Step 2: Check middle of right half (index 4, value 9)
            [5, [9], 12]
            9 == 9 → FOUND at index 4!  ★

    Each step cuts the search space in HALF.
    1000 items → only ~10 steps! (log2(1000) ≈ 10)

    How:
      left = 0, right = len-1
      while left <= right:
          mid = (left + right) // 2
          if nums[mid] == target → found!
          if nums[mid] < target → left = mid + 1  (go right)
          if nums[mid] > target → right = mid - 1 (go left)
"""
