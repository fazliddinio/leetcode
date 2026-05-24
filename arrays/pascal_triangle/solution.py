"""
Pascal's Triangle
LeetCode 118

Approach: Iterative Dynamic Programming
Time: O(n²) — generating n rows, row i has i+1 elements
Space: O(1) — excluding output, only temporary variables
Brute: O(n²) — recursively generate each row from the previous
"""

from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        """Iterative Dynamic Programming"""
        triangle = []
        for i in range(numRows):
            row = [None] * (i + 1)
            row[0], row[-1] = (1, 1)
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            triangle.append(row)
        return triangle
