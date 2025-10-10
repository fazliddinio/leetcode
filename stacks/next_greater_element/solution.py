# LeetCode 496: Next Greater Element I
# Time: O(n + m), Space: O(n)

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        next_greater = {}
        stack = []
        
        for n in nums2:
            while stack and stack[-1] < n:
                next_greater[stack.pop()] = n
            stack.append(n)
        
        return [next_greater.get(n, -1) for n in nums1]
