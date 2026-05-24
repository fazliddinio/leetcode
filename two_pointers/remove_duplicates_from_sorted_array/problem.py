"""
==========================================
  Remove Duplicates from Sorted Array (LeetCode 26)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Example 1: Input: nums = [1,1,2], Output: 2, nums = [1,2,_]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Squish exactly one copy of each number to the front of the array. The rest of the array doesn't matter.

    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    Desired: [0, 1, 2, 3, 4, ...garbage...]

Method: Two Pointers
  Use `L` to track where the next UNIQUE number should go.
  Since the first number is always unique, start `L` at index 1.
  Use `R` to scan starting from index 1.

  Compare nums[R] with the number BEFORE it (nums[R-1]).
  If it's DIFFERENT, we found a new sequence!
      Drop it into nums[L].
      Move L forward.

    L=1
    [0, 0, 1, 1, 2]
        R=1 (nums[1]==nums[0], ignore)

    L=1
    [0, 0, 1, 1, 2]
           R=2 (nums[2]!=nums[1], Keep it! nums[L]=nums[R])

    L=2
    [0, 1, 1, 1, 2]
"""
