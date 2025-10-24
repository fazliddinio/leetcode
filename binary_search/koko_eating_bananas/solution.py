# LeetCode 875: Koko Eating Bananas
# Time: O(n * log(max)), Space: O(1)

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 1, max(piles)
        
        while l < r:
            mid = (l + r) // 2
            hours = sum((p + mid - 1) // mid for p in piles)
            
            if hours <= h:
                r = mid
            else:
                l = mid + 1
        
        return l
