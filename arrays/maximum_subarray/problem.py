"""
==========================================
  Maximum Subarray (LeetCode 53)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array `nums`, find the subarray with the largest sum,
and return its sum.

Example 1:
    Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
    Output: 6
    Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
    Input: nums = [1]
    Output: 1

Example 3:
    Input: nums = [5,4,-1,7,8]
    Output: 23

Constraints:
    - 1 <= nums.length <= 10^5
    - -10^4 <= nums[i] <= 10^4

Follow up: If you have figured out the O(n) solution, try coding another
solution using the divide and conquer approach.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Find a contiguous chunk of the array that adds up to the biggest number.

    [-2, 1, -3, 4, -1, 2, 1, -5, 4]
                 ~~~~~~~~~~~~
                 [4, -1, 2, 1] = 6  ← this is the best!

The trick (Kadane's Algorithm):
  As you walk through the array, keep a running sum.
  At each step, ask: "Should I continue the old subarray, or start fresh?"

  If the running sum goes negative, RESTART from the current number.

    Index:  0    1    2    3    4    5    6    7    8
    Num:   -2    1   -3    4   -1    2    1   -5    4
    Sum:   -2    1   -2    4    3    5    6    1    5
           ↑    ↑         ↑                   ↑
         start  restart   restart           best=6

    Step-by-step:
    -2 → sum=-2, best=-2  (negative, will restart next)
     1 → sum=1,  best=1   (restart! 1 > -2+1)
    -3 → sum=-2, best=1
     4 → sum=4,  best=4   (restart! 4 > -2+4)
    -1 → sum=3,  best=4
     2 → sum=5,  best=5
     1 → sum=6,  best=6  ★
    -5 → sum=1,  best=6
     4 → sum=5,  best=6

Answer: 6
"""
