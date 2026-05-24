"""
==========================================
  Permutation in String (LeetCode 567)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
In other words, return true if one of s1's permutations is the substring of s2.

Example 1: Input: s1 = "ab", s2 = "eidbaooo", Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2: Input: s1 = "ab", s2 = "eidboaoo", Output: false

Constraints: 1 <= s1.length, s2.length <= 10^4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Exactly like "Find All Anagrams in a String". But instead of returning all starting indices, you just return True the moment you find one!

    s1: "ab", s2: "eidbaooo"
    "ba" is inside! Return True.

Method: Fixed Sliding Window
  Same logic. Target frequency array for `s1`.
  Window frequency array of size `len(s1)` scanning across `s2`.
  Add right char, remove left char.
  If arrays match, return True! Return False at the end.
"""
