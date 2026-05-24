"""
==========================================
  Remove Element (LeetCode 27)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array `nums` and an integer `val`, remove all occurrences
of `val` in `nums` in-place. The order of the elements may be changed.
Then return the number of elements in `nums` which are not equal to `val`.

Consider the number of elements in nums which are not equal to val be k,
to get accepted, you need to do the following things:
  - Change the array nums such that the first k elements of nums contain
    the elements which are not equal to val.
  - Return k.

Example 1:
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]

Example 2:
    Input: nums = [0,1,2,2,3,0,4,2], val = 2
    Output: 5, nums = [0,1,4,0,3,_,_,_]

Constraints:
    - 0 <= nums.length <= 100
    - 0 <= nums[i] <= 50
    - 0 <= val <= 100


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Remove all copies of a number from the array, IN-PLACE (no new array).
Return how many elements are left.

    nums = [3, 2, 2, 3],  remove val = 3

    Use a "write pointer" (k) that only moves when we keep an element:

    Read index 0: nums[0]=3 → it's val, SKIP
    Read index 1: nums[1]=2 → KEEP, write at k=0 → nums=[2,2,2,3], k=1
    Read index 2: nums[2]=2 → KEEP, write at k=1 → nums=[2,2,2,3], k=2
    Read index 3: nums[3]=3 → it's val, SKIP

    k=0  k=1
     ↓    ↓
    [2,   2,  _, _]    ← first k=2 elements are the answer
     ↑    ↑
    kept  kept

    Return k = 2
"""
