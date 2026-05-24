"""
==========================================
  Plus One (LeetCode 66)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

You are given a large integer represented as an integer array `digits`,
where each `digits[i]` is the i-th digit of the integer. The digits are
ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
    Input: digits = [1,2,3]
    Output: [1,2,4]
    Explanation: The array represents the integer 123. 123 + 1 = 124.

Example 2:
    Input: digits = [4,3,2,1]
    Output: [4,3,2,2]

Example 3:
    Input: digits = [9]
    Output: [1,0]

Constraints:
    - 1 <= digits.length <= 100
    - 0 <= digits[i] <= 9
    - digits does not contain any leading 0's.


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

You have a number, but it's split into an array of digits. Add 1 to it.

    [1, 2, 3]  →  123 + 1 = 124  →  [1, 2, 4]

Easy case: last digit is not 9.
    [1, 2, 3] → just add 1 to last digit → [1, 2, 4] ✓

Tricky case: last digit IS 9 (carry!).
    [1, 2, 9] → 9+1=10 → carry the 1 → [1, 3, 0]

Really tricky case: ALL nines!
    [9, 9, 9] → carry, carry, carry → [1, 0, 0, 0]

    Step by step for [9, 9, 9]:
        [9, 9, 9]  start from the right
              ↑  9+1=10, set to 0, carry=1
        [9, 9, 0]
           ↑     9+1=10, set to 0, carry=1
        [9, 0, 0]
        ↑        9+1=10, set to 0, carry=1
        [0, 0, 0]
        Still have carry? → prepend 1:
        [1, 0, 0, 0]  ✓
"""
