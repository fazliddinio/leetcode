"""
==========================================
  Minimize Max Distance to Gas Station (LeetCode 774)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given an integer array `stations` that represents the positions
of gas stations on a number line, sorted in ascending order. You are also
given an integer `k`.

You want to add `k` new gas stations. You want to minimize the maximum
distance between adjacent gas stations after adding the new stations.

Return the minimum possible value of the maximum distance between
adjacent gas stations after adding k new stations. Answers within 10^-6
will be accepted.

Example 1:
    Input: stations = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 9
    Output: 0.5

Example 2:
    Input: stations = [23, 24, 36, 39, 46, 56, 57, 65, 84, 98], k = 1
    Output: 14.0

Constraints:
    - 10 <= stations.length <= 2000
    - 0 <= stations[i] <= 10^8
    - stations is sorted in strictly increasing order.
    - 1 <= k <= 10^6


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Gas stations are placed on a road. You can add k MORE stations anywhere.
Place them to minimize the longest gap between any two stations.

    Stations: [1, 5, 9]    k = 1 (add 1 station)

    Gaps: 4 (between 1-5) and 4 (between 5-9)

    Best placement: add at position 3 or 7
    [1, 3, 5, 9] → gaps: 2, 2, 4 → max gap = 4
    [1, 5, 7, 9] → gaps: 4, 2, 2 → max gap = 4

    Actually try: [1, 3, 5, 7, 9]? But we only have k=1!

Binary search on the ANSWER (the max distance D):
    "Can we make all gaps ≤ D using at most k new stations?"

    For each gap, how many stations needed? = ceil(gap / D) - 1

    If total stations needed ≤ k → D works, try smaller D.
    If total > k → D is too small, try larger D.

A "binary search on the answer" pattern — search on a decimal range!
"""
