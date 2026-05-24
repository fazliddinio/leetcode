"""
==========================================
  Search Insert Position (LeetCode 35)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given a sorted array of distinct integers and a target value, return the
index if the target is found. If not, return the index where it would be
if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
    Input: nums = [1,3,5,6], target = 5
    Output: 2

Example 2:
    Input: nums = [1,3,5,6], target = 2
    Output: 1

Example 3:
    Input: nums = [1,3,5,6], target = 7
    Output: 4

Constraints:
    - 1 <= nums.length <= 10^4
    - -10^4 <= nums[i] <= 10^4
    - nums contains distinct values sorted in ascending order.
    - -10^4 <= target <= 10^4


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Where does the target fit in this sorted array?

    nums = [1, 3, 5, 6]

    target = 5 → it's at index 2 → return 2
    target = 2 → would go between 1 and 3 → return 1
    target = 7 → goes at the end → return 4

    [1, _, 3, 5, 6]
        ↑ insert 2 here (index 1)

Binary search: when the loop ends, `left` is the answer!
    If target found → return mid
    If not found → `left` points to where it should be inserted

    nums = [1, 3, 5, 6]  target = 2

    left=0, right=3, mid=1 → nums[1]=3 > 2 → right=0
    left=0, right=0, mid=0 → nums[0]=1 < 2 → left=1
    left=1 > right=0 → stop! → insert at index 1
"""
