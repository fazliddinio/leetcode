"""
==========================================
  Ransom Note (LeetCode 383)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1: Input: ransomNote = "a", magazine = "b", Output: false
Example 2: Input: ransomNote = "aa", magazine = "ab", Output: false
Example 3: Input: ransomNote = "aa", magazine = "aab", Output: true

Constraints: 1 <= ransomNote.length, magazine.length <= 10^5
ransomNote and magazine consist of lowercase English letters.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Can you cut out letters from a magazine to spell out your ransom note?

    Note: "aa"
    Magazine: "aab"
    Cut an 'a', cut another 'a'. You have enough! True!

Method: Hash Map / Frequency Array
  1. Count all the letters in the `magazine`. (e.g. `{'a': 2, 'b': 1}`)
  2. Iterate through the `ransomNote`.
  3. For each letter, if it's in the magazine count AND greater than 0, decrement it.
  4. If a letter is missing or hits 0, you don't have enough! Return False.
  5. If you make it to the end, return True.
"""
