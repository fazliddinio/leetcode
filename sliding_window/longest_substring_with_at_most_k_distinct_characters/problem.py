"""
==========================================
  Longest Substring with At Most K Distinct Characters (LeetCode 340)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s and an integer k, return the length of the longest substring of s that contains at most k distinct characters.

Example 1: Input: s = "eceba", k = 2, Output: 3
Explanation: The substring is "ece" with length 3.

Example 2: Input: s = "aa", k = 1, Output: 2

Constraints: 1 <= s.length <= 5 * 10^4, 0 <= k <= 50

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the longest stretch of text that only uses `K` different types of letters.

    s: "eceba", k: 2
    "ece" -> Uses 'e', 'c'. (2 distinct). Length 3.
    "ceb" -> Uses 'c', 'e', 'b'. (3 distinct). Invalid!

Method: Sliding Window + Hash Map
  Use a Hash Map to count the frequencies of characters inside our window.
  Expand the window by moving Right forward and adding `s[Right]` to the map.
  While the Hash Map has MORE than `K` keys (meaning more than K distinct letters):
      Shrink the window!
      Remove `s[Left]` from the map.
      If a letter's count drops to 0, completely delete it from the map.
      Move Left forward.
  Update max_len = max(max_len, Right - Left + 1)!
"""
