"""
==========================================
  Longest Common Prefix (LeetCode 14)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1: Input: strs = ["flower","flow","flight"], Output: "fl"
Example 2: Input: strs = ["dog","racecar","car"], Output: ""

Constraints: 1 <= strs.length <= 200, 0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
What is the longest starting chunk of letters that ALL the words share?

    Words: "flower", "flow", "flight"
    All start with "f" -> Yes.
    All start with "fl" -> Yes.
    All start with "flo" -> "flight" does not! 
    Output: "fl"

Method: Vertical Scanning or Sorting
  Sorting Trick:
    Sort the array of strings alphabetically.
    Now, you only need to compare the FIRST word and the LAST word! 
    Because if they share a prefix, everything sorted in between them must also share it.
    Loop through characters of the first and last word until they don't match, and return that slice.
"""
