"""
==========================================
  Longest Repeating Character Replacement (LeetCode 424)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1: Input: s = "ABAB", k = 2, Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2: Input: s = "AABABBA", k = 1, Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA". The substring "BBBB" has the longest repeating letters, which is 4.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the longest slice of identical characters if you are allowed to change `k` characters!

Method: Sliding Window
  The trick: `Window Length - Count of Most Frequent Character = Characters to Replace`
  If you have an "AABABBA" window of size 7, and 'B' appears 4 times. You must replace the other 3 characters.
  If `3` > `k` ... the window is INVALID!
  
  1. Expand the window with `R`. Add to a frequency map.
  2. Keep track of the `maxf` (max frequency of any single char in the current window).
  3. While `(R - L + 1) - maxf > k`:
     - The window is invalid. Shrink `L` and remove from map!
  4. Record max valid window.
"""
