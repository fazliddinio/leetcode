"""
==========================================
  Longest Palindromic Substring (LeetCode 5)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s, return the longest palindromic substring in s.

Example 1: Input: s = "babad", Output: "bab" ("aba" is also valid)
Example 2: Input: s = "cbbd", Output: "bb"

Constraints: 1 <= s.length <= 1000, s consist of only digits and English letters.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the longest continuous substring that reads the same backward as forward.

    s = "babad"
    Longest is "bab" or "aba".

How to solve (Expand Around Center):
A palindrome mirrors around its center.
So, treat every character (and every space between characters) as a potential center, and expand outward as long as the left and right characters match!

    Example: "b a b a d"
    Center at 'a' (index 1): expand left to 'b', right to 'b'. They match! -> "bab"
    Center at space between 'b' and 'a': left 'b', right 'a'. NO Match.

Remember to check both ODD length (center is a char) and EVEN length (center is between chars).
"""
