"""
Valid Perfect Square
LeetCode 367

Approach: Binary Search
Time: O(log num) — search range [1, num/2]
Space: O(1) — constant extra space
Brute: O(sqrt(num)) — subtract consecutive odd numbers until zero
"""


class Solution:

    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
            
        left, right = 2, num // 2
        while left <= right:
            mid = left + (right - left) // 2
            sq = mid * mid
            if sq == num:
                return True
            elif sq < num:
                left = mid + 1
            else:
                right = mid - 1
                
        return False
