"""
==========================================
  Palindromic Substrings (LeetCode 647)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.
A substring is a contiguous sequence of characters within the string.

Example 1: Input: s = "abc", Output: 3 ("a", "b", "c")
Example 2: Input: s = "aaa", Output: 6 ("a", "a", "a", "aa", "aa", "aaa")

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Count EVERY single palindrome substring inside the string.

    s = "aaa"
    Palindromes: "a", "a", "a", "aa", "aa", "aaa" (Total: 6)

How to solve:
Exactly the same as Longest Palindromic Substring!
Use the "Expand Around Center" approach.
For every possible center (each character, and each space between characters):
    Expand outwards. Every time the left and right characters match, increment the counter by 1!
"""
