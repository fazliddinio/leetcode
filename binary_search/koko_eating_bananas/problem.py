"""
==========================================
  Koko Eating Bananas (LeetCode 875)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Koko loves to eat bananas. There are `n` piles of bananas, the i-th pile
has `piles[i]` bananas. The guards have gone and will come back in `h`
hours.

Koko can decide her bananas-per-hour eating speed of `k`. Each hour, she
chooses some pile of bananas and eats k bananas from that pile. If the
pile has less than k bananas, she eats all of them and will not eat any
more bananas during this hour.

Koko likes to eat slowly but wants to finish eating all bananas before
the guards come back.

Return the minimum integer `k` such that she can eat all the bananas
within `h` hours.

Example 1:
    Input: piles = [3,6,7,11], h = 8
    Output: 4

Example 2:
    Input: piles = [30,11,23,4,20], h = 5
    Output: 30

Constraints:
    - 1 <= piles.length <= 10^4
    - piles.length <= h <= 10^9
    - 1 <= piles[i] <= 10^9


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Koko the monkey eats bananas at speed k per hour. What's the SLOWEST
speed where she finishes all piles in h hours?

    Piles: [3, 6, 7, 11]    Hours available: 8

    If k=4 (eat 4/hour):
    Pile 3:  ceil(3/4) = 1 hour
    Pile 6:  ceil(6/4) = 2 hours
    Pile 7:  ceil(7/4) = 2 hours
    Pile 11: ceil(11/4) = 3 hours
    Total: 1+2+2+3 = 8 hours ≤ 8  ✓ → k=4 works!

    If k=3 (eat 3/hour):
    3→1 + 6→2 + 7→3 + 11→4 = 10 hours > 8  ✗ → too slow!

Binary search on k (the speed):
    lo = 1, hi = max(piles) = 11

    k=6 → 1+1+2+2=6 ≤ 8 ✓ → try slower
    k=3 → 1+2+3+4=10 > 8  ✗ → try faster
    k=4 → 1+2+2+3=8 ≤ 8  ✓ → try slower
    k=3 → too slow  ✗
    → Answer: k=4  ★

It's asking: "What's the laziest Koko can be and still finish on time?"
"""
