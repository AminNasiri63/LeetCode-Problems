# 695. Max Area of Island

from typing import List

# Time Complexity: O(m*n) - Space Complexity: O(m*n)
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_area = 0

        def dfs_recursive(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
                return 0

            grid[i][j] = 0

            return 1 + dfs_recursive(i, j+1) + dfs_recursive(i+1, j) + dfs_recursive(i, j-1) + dfs_recursive(i-1, j)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs_recursive(i, j))

        return max_area
