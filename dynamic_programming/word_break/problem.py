"""
==========================================
  Word Break (LeetCode 139)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Example 1: Input: s = "leetcode", wordDict = ["leet","code"], Output: true
Example 2: Input: s = "applepenapple", wordDict = ["apple","pen"], Output: true
Example 3: Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"], Output: false

Constraints: 1 <= s.length <= 300, 1 <= wordDict.length <= 1000

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Can you split a string entirely into dictionary words?

    s = "applepenapple", dict = ["apple", "pen"]
    apple | pen | apple --> True

How to solve:
Use a boolean DP array `dp` of size `len(s) + 1`. `dp[i]` is True if `s[0:i]` can be segmented.
Base case: `dp[0] = True` (empty string is always True).

    Loop `i` from 1 to len(s).
    Loop `j` from 0 to `i`:
        If `dp[j]` is True AND `s[j:i]` is in wordDict:
            `dp[i] = True` and break!
"""
