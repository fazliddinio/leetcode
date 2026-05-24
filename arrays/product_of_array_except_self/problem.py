"""
==========================================
  Product of Array Except Self (LeetCode 238)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an integer array `nums`, return an array `answer` such that
`answer[i]` is equal to the product of all the elements of `nums` except
`nums[i]`.

The product of any prefix or suffix of nums is guaranteed to fit in a
32-bit integer.

You must write an algorithm that runs in O(n) time and without using the
division operation.

Example 1:
    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Example 2:
    Input: nums = [-1,1,0,-3,3]
    Output: [0,0,9,0,0]

Constraints:
    - 2 <= nums.length <= 10^5
    - -30 <= nums[i] <= 30
    - The product of any prefix or suffix fits in a 32-bit integer.

Follow up: Can you solve it in O(1) extra space complexity?


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

For each number, multiply everything EXCEPT that number.

    nums = [1, 2, 3, 4]

    answer[0] = 2 × 3 × 4 = 24    (skip the 1)
    answer[1] = 1 × 3 × 4 = 12    (skip the 2)
    answer[2] = 1 × 2 × 4 = 8     (skip the 3)
    answer[3] = 1 × 2 × 3 = 6     (skip the 4)

    Answer: [24, 12, 8, 6]

The trick: for each position, the answer is:
    (product of everything LEFT) × (product of everything RIGHT)

    nums:    [1,    2,    3,    4  ]
    left:    [1,    1,    2,    6  ]   ← running product from left
    right:   [24,   12,   4,    1  ]   ← running product from right
    answer:  [1×24, 1×12, 2×4,  6×1]
           = [24,   12,   8,    6  ]

Two passes:
  Pass 1 (left to right): build left products
  Pass 2 (right to left): multiply by right products
"""
