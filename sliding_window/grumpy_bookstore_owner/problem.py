"""
==========================================
  Grumpy Bookstore Owner (LeetCode 1052)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the owner is grumpy during the ith minute, and is 0 otherwise.
When the owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.

Return the maximum number of customers that can be satisfied throughout the day.

Example 1: Input: customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3, Output: 16

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
You have a superpower to force the grumpy owner to be happy for exactly `X` consecutive minutes. Find the window of `X` minutes that saves the MOST angry customers!

Method: Fixed Sliding Window
  1. Calculate the base number of satisfied customers (the ones where grumpy is 0).
  2. Now, slide a window of size `X` across the array.
  3. Inside that window, count how many customers are ANGRY. This is how many customers you "save" with the superpower.
  4. Slide the window: Drop the left angry customer count, add the right angry customer count. Track the maximum saved!
  5. Add `base_satisfied` + `max_saved`.
"""
