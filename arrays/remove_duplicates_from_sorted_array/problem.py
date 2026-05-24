"""
==========================================
  Remove Duplicates from Sorted Array (LeetCode 26)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same. Then return the number
of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you
need to do the following things:
    - Change the array nums such that the first k elements of nums contain the
      unique elements in the order they were present in nums initially.
    - The remaining elements of nums are not important as well as the size of nums.
    - Return k.

Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements
    of nums being 1 and 2 respectively.

Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
    Explanation: Your function should return k = 5, with the first five elements
    of nums being 0, 1, 2, 3, and 4 respectively.

Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Array is already sorted. Remove duplicates in-place and return the count of uniques.

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
                                            ↓
    After: [0, 1, 2, 3, 4, _, _, _, _, _]  → return 5

Two pointer technique:
    - "write" pointer: where to place the next unique value
    - "read" pointer: scans through the array

    [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
     w  r
     ↓
    read=0: same as previous? skip
    read=1: 0==0? yes, skip
    read=2: 1!=0? WRITE! nums[1]=1, w→2
    read=3: 1==1? skip
    read=4: 1==1? skip
    read=5: 2!=1? WRITE! nums[2]=2, w→3
    ...
"""
