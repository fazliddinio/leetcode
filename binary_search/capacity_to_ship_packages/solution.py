# LeetCode 1011: Capacity To Ship Packages Within D Days
# Time: O(n * log(sum)), Space: O(1)

class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        def can_ship(capacity):
            d = 1
            curr = 0
            for w in weights:
                if curr + w > capacity:
                    d += 1
                    curr = w
                else:
                    curr += w
            return d <= days
        
        l, r = max(weights), sum(weights)
        while l < r:
            mid = (l + r) // 2
            if can_ship(mid):
                r = mid
            else:
                l = mid + 1
        return l
