"""
==========================================
  Group Anagrams (LeetCode 49)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word formed by rearranging the letters of a different word.

Example: Input: strs = ["eat","tea","tan","ate","nat","bat"], Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Group words that have the exact same letters!

Method:
  If two words are anagrams, their SORTED letters will be EXACTLY identical!
  `eat` sorted -> `aet`
  `tea` sorted -> `aet`

  Use a Hash Map where the key is the sorted string and the value is a list of words.
  Sort each string, append the original string to the map under the sorted key!
"""
