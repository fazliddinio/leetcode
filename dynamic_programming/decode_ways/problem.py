"""
==========================================
  Decode Ways (LeetCode 91)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
A message containing letters from A-Z can be encoded into numbers using the following mapping:
'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"

To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways).

Given a string s containing only digits, return the number of ways to decode it.

Example 1: Input: s = "12", Output: 2 ("AB" or "L")
Example 2: Input: s = "226", Output: 3 ("BZ", "VF", "BBF")
Example 3: Input: s = "06", Output: 0

Constraints: 1 <= s.length <= 100, s contains only digits.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
How many ways can you turn numbers back into letters? (1=A ... 26=Z)

    s = "226"
    Way 1: 2, 2, 6 (B, B, F)
    Way 2: 22, 6 (V, F)
    Way 3: 2, 26 (B, Z)
    Output: 3

Warning: "0" cannot be decoded alone! "06" is invalid.

DP Approach: Similar to Fibonacci / Climbing Stairs!
`dp[i]` = ways to decode up to index `i`.

    For each digit:
    If 1 digit (1-9): add ways from `dp[i-1]`
    If 2 digits (10-26): add ways from `dp[i-2]`
"""
