"""
==========================================
  Reverse Vowels of a String (LeetCode 345)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1: Input: s = "hello", Output: "holle"
Example 2: Input: s = "leetcode", Output: "leotcede"

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Only flip the vowels in the sentence, leave consonants where they are!

    "hello" -> 'e' and 'o' are vowels. Swap them! -> "holle"

Method: Two Pointers
  Use a list of the string since strings are immutable in Python.
  Put `L` at start, `R` at end.
  While `L < R`:
      If `L` is NOT a vowel, move `L` forward.
      If `R` is NOT a vowel, move `R` backward.
      If BOTH are vowels:
          Swap them!
          Move `L` forward and `R` backward.
"""
