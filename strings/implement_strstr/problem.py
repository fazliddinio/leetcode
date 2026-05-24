"""
==========================================
  Find the Index of the First Occurrence in a String (LeetCode 28)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1: Input: haystack = "sadbutsad", needle = "sad", Output: 0
Explanation: "sad" occurs at index 0 and 6. The first occurrence is at index 0, so we return 0.
Example 2: Input: haystack = "leetcode", needle = "leeto", Output: -1

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the first time a small word appears inside a big word. Just like finding a needle in a haystack!

    Haystack: "sadbutsad"
    Needle:   "sad"
    Answer: 0 (it starts at index 0).

Method: Sliding Window
  Let the needle length be `L`.
  Scan a window of length `L` along the haystack!
  `haystack[i : i+L] == needle`? If yes, return `i`.
  If you reach the end without a match, return -1.
"""
