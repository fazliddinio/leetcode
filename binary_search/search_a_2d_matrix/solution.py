# LeetCode 74: Search a 2D Matrix
# Time: O(log(m*n)), Space: O(1)

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        
        while l <= r:
            mid = (l + r) // 2
            val = matrix[mid // n][mid % n]
            
            if val == target:
                return True
            elif val < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False
