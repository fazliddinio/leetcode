"""
==========================================
  Longest Substring Without Repeating Characters (LeetCode 3)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s, find the length of the longest substring without repeating characters.

Example 1: Input: s = "abcabcbb", Output: 3 ("abc" with length 3)
Example 2: Input: s = "bbbbb", Output: 1 ("b" with length 1)
Example 3: Input: s = "pwwkew", Output: 3 ("wke" with length 3)

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the longest stretch of unique characters in a string string.

    s = "abcabcbb" -> stretch "abc" is unique (len 3). Stretch "bca" is unique. Stretch "cab" is unique.

Method: Sliding Window with a Hash Set.
  Left and Right pointers define a window.
  Move Right forward and add the character to a set.
  If the character at Right is ALREADY in the set: We have a repeating character!
  Move Left forward, removing characters from the set, until the repeat is gone!
  At every step, `max_len = max(max_len, Right - Left + 1)`.
"""
