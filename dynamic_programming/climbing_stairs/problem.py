"""
==========================================
  Climbing Stairs (LeetCode 70)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Example 1: Input: n = 2, Output: 2
Example 2: Input: n = 3, Output: 3

Constraints: 1 <= n <= 45

------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------
How many different ways can you climb a staircase if you can take 1 or 2 steps at a time?

    n = 3 stairs
    Way 1: 1 step + 1 step + 1 step
    Way 2: 1 step + 2 steps
    Way 3: 2 steps + 1 step
    Output: 3 ways

Trick: To reach step `n`, you must have come from either `n-1` (taking 1 step) or `n-2` (taking 2 steps).
So, ways(n) = ways(n-1) + ways(n-2)

This is just the Fibonacci sequence!
    Stairs: 1, 2, 3, 4, 5...
    Ways:   1, 2, 3, 5, 8...
"""
