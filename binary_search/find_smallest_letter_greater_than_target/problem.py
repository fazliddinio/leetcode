"""
==========================================
  Find Smallest Letter Greater Than Target (LeetCode 744)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given an array of characters `letters` that is sorted in
non-decreasing order, and a character `target`. There are at least two
different characters in `letters`.

Return the smallest character in `letters` that is lexicographically
greater than `target`. If such a character does not exist, return the
first character in `letters`.

Note that the letters wrap around.

Example 1:
    Input: letters = ["c","f","j"], target = "a"
    Output: "c"

Example 2:
    Input: letters = ["c","f","j"], target = "c"
    Output: "f"

Example 3:
    Input: letters = ["x","x","y","y"], target = "z"
    Output: "x"

Constraints:
    - 2 <= letters.length <= 10^4
    - letters[i] is a lowercase English letter.
    - letters is sorted in non-decreasing order.
    - target is a lowercase English letter.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

In a sorted list of letters, find the NEXT letter after the target.
If there's nothing bigger, wrap around to the first letter.

    letters = [c, f, j]    target = "c"

    c → not greater than c (equal doesn't count!)
    f → YES! This is the smallest letter > c  ★

    Answer: "f"

    letters = [x, x, y, y]  target = "z"
    Nothing is > z → wrap around → answer: "x"

Binary search for the first letter STRICTLY greater than target:

    [c, f, j]  target = c

    left=0, right=2
    mid=1 → 'f' > 'c' → could be answer, go left
    mid=0 → 'c' not > 'c' → go right
    → answer at index 1: 'f'

It's like finding the next bus after your arrival time on a circular schedule!
"""
