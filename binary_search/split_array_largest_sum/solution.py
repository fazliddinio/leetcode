# LeetCode 410: Split Array Largest Sum
# Time: O(n * log(sum)), Space: O(1)

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        def can_split(max_sum):
            count = 1
            curr = 0
            for n in nums:
                if curr + n > max_sum:
                    count += 1
                    curr = n
                else:
                    curr += n
            return count <= k
        
        l, r = max(nums), sum(nums)
        while l < r:
            mid = (l + r) // 2
            if can_split(mid):
                r = mid
            else:
                l = mid + 1
        return l
