"""
==========================================
  Palindrome Partitioning (LeetCode 131)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given a string `s`, partition `s` such that every substring of the
partition is a palindrome. Return all possible palindrome partitioning
of `s`.

Example 1:
    Input: s = "aab"
    Output: [["a","a","b"],["aa","b"]]

Example 2:
    Input: s = "a"
    Output: [["a"]]

Constraints:
    - 1 <= s.length <= 16
    - s contains only lowercase English letters.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Split a string into pieces where EVERY piece reads the same forwards
and backwards (is a palindrome).

    s = "aab"

    Way 1: "a" | "a" | "b"  →  all palindromes? ✓ ✓ ✓  → Valid!
    Way 2: "aa" | "b"       →  all palindromes? ✓ ✓    → Valid!
    Way 3: "aab"            →  palindrome? ✗           → Invalid!
    Way 4: "a" | "ab"       →  palindrome? ✓ ✗         → Invalid!

    Answer: [["a","a","b"], ["aa","b"]]

Think of it as choosing where to cut:

    a | a | b     ← cut after each letter
    a a | b       ← cut after "aa"

At each position, try all possible cuts. If the piece before the cut
is a palindrome, keep going. If not, don't bother.

    "aab" → try cutting after 1 char: "a" (palindrome ✓)
             → remaining: "ab"
               → "a" (✓) → "b" (✓) → FOUND: ["a","a","b"]
               → "ab" (✗) → skip
           → try cutting after 2 chars: "aa" (palindrome ✓)
             → remaining: "b" (✓) → FOUND: ["aa","b"]
           → try cutting after 3 chars: "aab" (✗) → skip
"""
