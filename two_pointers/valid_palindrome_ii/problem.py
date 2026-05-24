"""
==========================================
  Valid Palindrome II (LeetCode 680)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1: Input: s = "aba", Output: true
Example 2: Input: s = "abca", Output: true (You could delete the character 'c'.)
Example 3: Input: s = "abc", Output: false

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Is the word a palindrome if you are allowed to delete EXACTLY ONE character?

    "abca"
    Delete 'c' -> "aba" -> True!

Method: Two Pointers
  Put `L` at start, `R` at end.
  If characters match, move them in `L+=1`, `R-=1`.
  If they DON'T match:
      You have 2 choices. Delete the character at `L`, or delete the character at `R`.
      So, check if `s[L+1 : R+1]` is a palindrome.
      And check if `s[L : R]` string is a palindrome.
      If EITHER of them is a palindrome, return True!
      If not, return False.
"""
