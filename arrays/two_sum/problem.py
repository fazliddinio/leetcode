"""
==========================================
  Two Sum (LeetCode 1)
==========================================

------------------------------------------
 Part 1: Official LeetCode Description
------------------------------------------

Given an array of integers `nums` and an integer `target`, return indices
of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

You can return the answer in any order.

Example 1:
    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
    Input: nums = [3,2,4], target = 6
    Output: [1,2]

Example 3:
    Input: nums = [3,3], target = 6
    Output: [0,1]

Constraints:
    - 2 <= nums.length <= 10^4
    - -10^9 <= nums[i] <= 10^9
    - -10^9 <= target <= 10^9
    - Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2)?


------------------------------------------
 Part 2: Simpler Explanation
------------------------------------------

Find two numbers in the list that add up to the target. Return their positions.

    nums = [2, 7, 11, 15],  target = 9
                                      ↓
    2 + 7 = 9  ✓    → positions [0, 1]

Instead of checking every pair (slow!), use a dictionary as a "cheat sheet":

    "I need target - current_number. Have I seen it before?"

    Step 1: num=2, need 9-2=7. Seen 7? No.  Remember {2: index 0}
    Step 2: num=7, need 9-7=2. Seen 2? YES! → return [0, 1]  ★

    It's like walking into a room looking for your dance partner:
    - "I need someone who is 7 to make 9 with me (I'm 2)"
    - Nobody yet... I'll wait here.
    - Next person: "I'm 7, anyone need me?"
    - "YES! Person at index 0 needs you!" → Match found!
"""
