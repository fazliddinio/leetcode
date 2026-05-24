"""
==========================================
  Sliding Window Maximum (LeetCode 239)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
Return the max sliding window.

Example 1: Input: nums = [1,3,-1,-3,5,3,6,7], k = 3, Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Slide a magnifying glass of size K across the array. What is the biggest number visible at every step?

Method: Monotonic Decreasing Deque (O(N) Time!)
  We only care about the BIGGEST number. If a new big number enters the window, any smaller number currently in the window will NEVER be the max again!
  
  1. Maintain a Double-Ended Queue (Deque) of INDICES.
  2. The Deque must always be STRICTLY DECREASING!
     - Before adding `nums[R]`, pop smaller numbers from the BACK of the Deque.
  3. Ensure the Deque only holds indices within the current window:
     - If the index at the FRONT of the Deque is `< L`, pop it from the front!
  4. The max element for the current window is always at the FRONT of the deque!
"""
