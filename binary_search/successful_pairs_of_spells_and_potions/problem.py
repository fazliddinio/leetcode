"""
==========================================
  Successful Pairs of Spells and Potions (LeetCode 2300)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given two positive integer arrays `spells` and `potions` of
length n and m respectively. spells[i] represents the strength of the
i-th spell and potions[j] represents the strength of the j-th potion.

A spell and potion pair is considered successful if the product of their
strengths is at least `success`.

Return an integer array `pairs` of length n where `pairs[i]` is the
number of potions that will form a successful pair with the i-th spell.

Example 1:
    Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
    Output: [4,0,3]

Example 2:
    Input: spells = [3,1,2], potions = [8,5,8], success = 16
    Output: [2,0,2]

Constraints:
    - n == spells.length, m == potions.length
    - 1 <= n, m <= 10^5
    - 1 <= spells[i], potions[j] <= 10^5
    - 1 <= success <= 10^10


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Each spell pairs with each potion. A pair is "successful" if:
    spell × potion ≥ success

For each spell, count how many potions make it successful.

    spells=[5,1,3]  potions=[1,2,3,4,5]  success=7

    Spell 5: needs potion ≥ 7/5 = 1.4 → potions ≥ 2: [2,3,4,5] = 4
    Spell 1: needs potion ≥ 7/1 = 7   → none qualify = 0
    Spell 3: needs potion ≥ 7/3 = 2.3 → potions ≥ 3: [3,4,5] = 3

    Answer: [4, 0, 3]

Trick: Sort potions first, then binary search!
    Sorted potions: [1, 2, 3, 4, 5]

    For spell=5, need potion ≥ ceil(7/5) = 2
    Binary search for 2 in sorted potions → index 1
    Count = 5 - 1 = 4 potions work  ★
"""
