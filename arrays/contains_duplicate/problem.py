"""
==========================================
  Contains Duplicate (LeetCode 217)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array `nums`, return `true` if any value appears at least
twice in the array, and return `false` if every element is distinct.

Example 1:
    Input: nums = [1,2,3,1]
    Output: true

Example 2:
    Input: nums = [1,2,3,4]
    Output: false

Example 3:
    Input: nums = [1,1,1,3,3,4,3,2,4,2]
    Output: true

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^9 <= nums[i] <= 10^9


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

You have a bag of numbers. Are any of them the same?

    [1, 2, 3, 1]  →  Yes! The number 1 appears twice.
    [1, 2, 3, 4]  →  No, all different.

Think of it like checking IDs at a party:
  - Keep a guest list (a set).
  - As each guest arrives, check: "Have I seen you before?"
  - If yes → duplicate found! Return True.
  - If no  → add them to the list and continue.

    Guest 1 arrives → List: {1}         New!
    Guest 2 arrives → List: {1, 2}      New!
    Guest 3 arrives → List: {1, 2, 3}   New!
    Guest 1 arrives → Already in list!  ★ DUPLICATE!

Answer: True
"""
