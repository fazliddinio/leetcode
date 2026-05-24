"""
Three Number Sum
AlgoExpert (Similar to LeetCode 15 but targets a given sum)

Approach: Sort + Two Pointers
Time: O(n²) — sorting O(n log n) + nested loop O(n²)
Space: O(1) — excluding output list space
Brute: O(n²) — for each element, use hash set to find complement pair
"""

from typing import List


class Solution:

    def threeNumberSum(self, arr: List[int], target: int) -> List[List[int]]:
        arr.sort()
        result = []
        n = len(arr)
        for i in range(n - 2):
            left, right = i + 1, n - 1
            current_target = target - arr[i]
            while left < right:
                current_sum = arr[left] + arr[right]
                if current_sum == current_target:
                    result.append([arr[i], arr[left], arr[right]])
                    left += 1
                    right -= 1
                elif current_sum < current_target:
                    left += 1
                else:
                    right -= 1
        return result
