"""
==========================================
  Minimum Window Substring (LeetCode 76)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".
The testcases will be generated such that the answer is unique.

Example 1: Input: s = "ADOBECODEBANC", t = "ABC", Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2: Input: s = "a", t = "a", Output: "a"

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Find the SHORTEST slice of the master string that contains ALL the required letters.

    s: "ADOBECODEBANC", t: "ABC"
    [ADOBEC] -> Has ABC! Len 6.
    [BANC] -> Has ABC! Len 4. (Winner!)

Method: Sliding Window (Expand then Shrink)
  Use two Hash Maps: `target_map` (for `t`) and `window_map` (for `s`).
  Track `have` (how many matched characters) and `need` (total distinct characters in `t`).
  
  1. EXPAND: Move `R` forward. Add `s[R]` to `window_map`.
     - If `s[R]` completes a required count, `have += 1`.
  2. SHRINK: While `have == need` (our window is valid!):
     - Record the string if it's the minimum so far!
     - Drop `s[L]` from the window to try and find an even smaller one.
     - Move `L` forward.
"""
