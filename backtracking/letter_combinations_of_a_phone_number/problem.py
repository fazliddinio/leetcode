"""
==========================================
  Letter Combinations of a Phone Number (LeetCode 17)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given a string containing digits from 2-9 inclusive, return all possible
letter combinations that the digit could represent. Return the answer in
any order.

A mapping of digits to letters (just like on the telephone buttons):
    2 → abc,  3 → def,  4 → ghi,  5 → jkl,
    6 → mno,  7 → pqrs, 8 → tuv,  9 → wxyz

Example 1:
    Input: digits = "23"
    Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

Example 2:
    Input: digits = ""
    Output: []

Example 3:
    Input: digits = "2"
    Output: ["a","b","c"]

Constraints:
    - 0 <= digits.length <= 4
    - digits[i] is a digit in the range ['2', '9'].


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Remember old phone keypads? Each number maps to letters:

    [1]       [2]abc   [3]def
    [4]ghi    [5]jkl   [6]mno
    [7]pqrs   [8]tuv   [9]wxyz

Given digits "23", generate ALL possible letter combos:

    Digit 2 → {a, b, c}
    Digit 3 → {d, e, f}

    Pair every letter from 2 with every letter from 3:

    a + d = "ad"    b + d = "bd"    c + d = "cd"
    a + e = "ae"    b + e = "be"    c + e = "ce"
    a + f = "af"    b + f = "bf"    c + f = "cf"

It's like a combination lock:
    First dial: [a, b, c]
    Second dial: [d, e, f]
    → 3 × 3 = 9 total combinations
"""
