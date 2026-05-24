"""
==========================================
  Longest Turbulent Subarray (LeetCode 978)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an integer array arr, return the length of a maximum size turbulent subarray of arr.
A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

Example 1: Input: arr = [9,4,2,10,7,8,8,1,9], Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]  (4 > 2 < 10 > 7 < 8)

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the longest alternating zigzag of up/down trends between numbers.

    [4, 2, 10, 7, 8]
    4 -> 2: Down
    2 -> 10: Up
    10 -> 7: Down
    7 -> 8: Up
    Perfect Zig-Zag! Length = 5.

Method: Sliding Window (Two Pointers)
  Track the expected sign (1 for up, -1 for down).
  Move `Right` forward. 
  Check the sign between `arr[Right]` and `arr[Right-1]`.
  If it's the STRICTLY OPPOSITE to the last sign:
      Keep going! Update the last sign.
  If it's the SAME sign as the last one:
      The zigzag broke! Reset the window to length 2 (starting at Right-1).
  If elements are EQUAL:
      The zigzag super broke. Reset window to length 1 (starting at Right).
"""
