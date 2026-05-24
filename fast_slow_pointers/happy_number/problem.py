"""
==========================================
  Happy Number (LeetCode 202)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
Write an algorithm to determine if a number n is happy.
A happy number is a number defined by the following process:
Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

Example 1: Input: n = 19, Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
Square the digits of a number, add them up. Do it repeatedly. Do you hit 1? Or do you get stuck in an endless loop?

Method: Fast & Slow Pointers!
  The sequence of numbers is just a Linked List!
  If it loops endlessly, it's a Linked List Cycle.
  - `Slow` runner advances by calculating the sum of squares ONCE.
  - `Fast` runner advances by calculating the sum of squares TWICE.
  If they ever meet before hitting 1, it's NOT a happy number! (Because it's a cycle).
"""
