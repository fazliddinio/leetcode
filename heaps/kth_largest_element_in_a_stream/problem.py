"""
==========================================
  Kth Largest Element in a Stream (LeetCode 703)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:
  - KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
  - int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.

Example:
  Input: ["KthLargest", "add", "add", "add", "add", "add"]
         [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
  Output: [null, 4, 5, 5, 8, 8]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Keep track of the K-th biggest number as endless numbers get tossed at you.

Method: Use a Min-Heap!
  If we only care about the top K largest elements, we don't need to store everything!
  Keep a Min-Heap of exactly size K.
  Whenever a new number comes in:
     - Push it onto the heap.
     - If the heap has more than K elements, pop the smallest one!
  The root of the Min-Heap (the smallest element in our top K pool) is exactly the K-th largest element!
"""
