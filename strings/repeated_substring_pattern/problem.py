"""
==========================================
  Repeated Substring Pattern (LeetCode 459)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1: Input: s = "abab", Output: true (It's the substring "ab" twice.)
Example 2: Input: s = "aba", Output: false
Example 3: Input: s = "abcabcabcabc", Output: true (It's the substring "abc" four times.)

Constraints: 1 <= s.length <= 10^4, s consists of lowercase English letters.

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Can the word be built by just copy-pasting a smaller chunk of it over and over?

    s = "abab" -> "ab" + "ab". True!
    s = "aba" -> No chunk works. False.

Method 1: String Concatenation Trick
  If a string `S` is made of a repeating pattern `P` (like S = P + P + P), then if we put TWO of the strings together (`S + S`), the pattern will look like `P + P + P + P + P + P`.
  If we chop off the very first character and the very last character of `S + S`, the original string `S` will STILL be found inside it if it's a repeating pattern!
  Result: `return s in (s + s)[1:-1]`

Method 2: Check all divisors (Brute Force)
  Try every possible length `i` from 1 to `len(s) // 2`.
  If `len(s) % i == 0` (it divides perfectly), check if `s[:i] * (len(s)//i) == s`.
"""
