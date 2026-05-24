"""
==========================================
  Find All Anagrams in a String (LeetCode 438)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1: Input: s = "cbaebabacd", p = "abc", Output: [0,6]
Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2: Input: s = "abab", p = "ab", Output: [0,1,2]

Constraints: 1 <= s.length, p.length <= 3 * 10^4

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find every substring of `s` that holds the exact same letters (and counts) as `p`.

    s: cbaebabacd, p: abc
    Win: [cba]ebabacd -> "cba" has 1 A, 1 B, 1 C. Valid! Index 0!
    Win: c[bae]babacd -> has E. Invalid.

Method: Sliding Window + Hash Map
  Build a target Hash Map or Array of size 26 for `p`.
  Build a sliding window Hash Map of the exact same size `len(p)` for `s`.
  Slide the window one character to the right:
      Add the new character `s[R]` to your map.
      Remove the oldest character `s[L]` from your map!
      Check if your map EXACTLY equals the target map! If so, save `L`.
"""
