# Three Number Sum
# Time: O(n^2), Space: O(n)

class Solution:
    def threeNumberSum(self, arr: list[int], target: int) -> list[list[int]]:
        arr.sort()
        result = []
        
        for i in range(len(arr) - 2):
            l, r = i + 1, len(arr) - 1
            while l < r:
                total = arr[i] + arr[l] + arr[r]
                if total == target:
                    result.append([arr[i], arr[l], arr[r]])
                    l += 1
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        
        return result
