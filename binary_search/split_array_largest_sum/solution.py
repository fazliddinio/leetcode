"""
Split Array Largest Sum
LeetCode 410

Approach: Binary Search on Answer
Time: O(n * log(sum(nums))) — search range from max(nums) to sum(nums)
Space: O(1) — constant variable space
Brute: O(k * n^2) — dynamic programming with memoization
"""

from typing import List


class Solution:

    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(max_sum: int) -> bool:
            count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > max_sum:
                    count += 1
                    current_sum = num
                    if count > k:
                        return False
                else:
                    current_sum += num
            return True
            
        left, right = max(nums), sum(nums)
        ans = right
        
        while left <= right:
            mid = left + (right - left) // 2
            if canSplit(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
                
        return ans
