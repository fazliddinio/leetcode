"""
==========================================
  Valid Mountain Array (LeetCode 941)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an array of integers `arr`, return `true` if and only if it is a
valid mountain array.

Recall that arr is a mountain array if and only if:
  - arr.length >= 3
  - There exists some i with 0 < i < arr.length - 1 such that:
    - arr[0] < arr[1] < ... < arr[i-1] < arr[i]
    - arr[i] > arr[i+1] > ... > arr[arr.length - 1]

Example 1:
    Input: arr = [2,1]
    Output: false

Example 2:
    Input: arr = [3,5,5]
    Output: false

Example 3:
    Input: arr = [0,3,2,1]
    Output: true

Constraints:
    - 1 <= arr.length <= 10^4
    - 0 <= arr[i] <= 10^4


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Does the array go UP then DOWN like a mountain? (No flat parts!)

    Valid mountain:         NOT a mountain:
          3                     5 5
         / \\                   / \
        2   2                 3   3
       /     \\               /
      0       1             1
    [0,2,3,2,1] ✓         [1,3,5,5,3] ✗ (flat top!)

    Also NOT mountains:
    [1,2,3]  ✗ (only goes up, no down)
    [3,2,1]  ✗ (only goes down, no up)
    [2,1]    ✗ (too short, need at least 3)

How to check:
  1. Walk UP from the left while numbers increase.
  2. Walk DOWN from there while numbers decrease.
  3. If you reach the end AND the peak wasn't at the start/end → it's a mountain!

    arr = [0, 3, 2, 1]

    Walk up:   0 → 3  (i stops at index 1, the peak)
    Walk down: 3 → 2 → 1  (reaches the end!)
    Peak at index 1 (not start, not end) ✓

    Answer: True
"""
