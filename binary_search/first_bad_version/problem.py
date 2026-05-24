"""
==========================================
  First Bad Version (LeetCode 278)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are a product manager and currently leading a team to develop a new
product. Unfortunately, the latest version of your product fails the
quality check. Since each version is developed based on the previous
version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the
first bad one, which causes all the following ones to be bad.

You are given an API `bool isBadVersion(version)` which returns whether
version is bad. Implement a function to find the first bad version. You
should minimize the number of calls to the API.

Example 1:
    Input: n = 5, bad = 4
    Output: 4
    Explanation: isBadVersion(3) = false, isBadVersion(5) = true,
                 isBadVersion(4) = true. So 4 is the first bad version.

Example 2:
    Input: n = 1, bad = 1
    Output: 1

Constraints:
    - 1 <= bad <= n <= 2^31 - 1


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Versions go from good to bad at some point. Find WHERE it flips.

    Versions:  1    2    3    4    5
    Status:    ✓    ✓    ✓    ✗    ✗
                              ↑ first bad!

It's like finding when milk went bad — check the middle first:

    [✓  ✓  ✓  ✗  ✗]
            ↑ mid=3 → good → bad must be AFTER this
    [✗  ✗]
     ↑ mid=4 → bad → could be first, check LEFT
    [nothing left]
    → Answer: 4

Binary search:
    - If mid is bad    → first bad is at mid or before → go left
    - If mid is good   → first bad is after mid → go right
"""
