from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
    # Time: O(n), Space: O(n)
    def contains_duplicate(nums):
        return len(nums) != len(set(nums))
