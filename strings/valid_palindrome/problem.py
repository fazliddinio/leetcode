"""
==========================================
  Valid Palindrome (LeetCode 125)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Example 1: Input: s = "A man, a plan, a canal: Panama", Output: true
Example 2: Input: s = "race a car", Output: false

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Is the sentence a palindrome if you ignore spaces, punctuation, and capitalization?

    "A man, a plan, a canal: Panama"
    Turns into: "amanaplanacanalpanama"
    Read backwards: It's the exact same! True!

Method: Two Pointers
  Use a `Left` pointer at the start (0) and a `Right` pointer at the end (len - 1).
  Loop while Left < Right:
    If Left character is NOT a letter/number -> move Left forward.
    If Right character is NOT a letter/number -> move Right backward.
    If they both are letters:
        Compare them (lowercase).
        If they don't match, return False!
        If they match, move both inward.
"""
