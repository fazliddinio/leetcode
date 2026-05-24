"""
==========================================
  Capacity To Ship Packages Within D Days (LeetCode 1011)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

A conveyor belt has packages that must be shipped from one port to another
within `days` days.

The i-th package on the conveyor belt has a weight of `weights[i]`. Each
day, we load the ship with packages on the conveyor belt (in the given
order). We may not load more weight than the maximum weight capacity of
the ship.

Return the least weight capacity of the ship that will result in all the
packages on the conveyor belt being shipped within `days` days.

Example 1:
    Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
    Output: 15
    Explanation: A ship capacity of 15 is the minimum to ship all
    packages in 5 days:
      Day 1: 1,2,3,4,5
      Day 2: 6,7
      Day 3: 8
      Day 4: 9
      Day 5: 10

Example 2:
    Input: weights = [3,2,2,4,1,4], days = 3
    Output: 6

Example 3:
    Input: weights = [1,2,3,1,1], days = 4
    Output: 3

Constraints:
    - 1 <= days <= weights.length <= 5 * 10^4
    - 1 <= weights[i] <= 500


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

You have packages on a belt and a ship. What's the SMALLEST ship capacity
that lets you ship everything in D days?

    Packages: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    Days: 5

    Can we do it with capacity 10?  → Need 6 days  ✗
    Can we do it with capacity 20?  → Need 3 days  ✓ (too big though)
    Can we do it with capacity 15?  → Need 5 days  ✓ ★ (just right!)

Binary search on the ANSWER (the capacity):
  - Minimum possible capacity = max(weights) = 10  (must fit largest package)
  - Maximum possible capacity = sum(weights) = 55  (ship everything in 1 day)

    Binary search between 10 and 55:
    mid=32 → can ship in 2 days ✓ → try smaller
    mid=21 → can ship in 3 days ✓ → try smaller
    mid=15 → can ship in 5 days ✓ → try smaller
    mid=12 → can ship in 6 days ✗ → too small
    mid=14 → can ship in 6 days ✗ → too small
    mid=15 → answer!  ★

    To check if capacity C works, greedily pack:
    Load packages until adding the next one would exceed C, then new day.
"""
