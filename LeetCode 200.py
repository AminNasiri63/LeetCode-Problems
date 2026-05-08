# 200. Number of Islands

from typing import List

# Time Complexity: O(m*n) - Space Complexity: O(m*n)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        num_island = 0

        def dfs_recursive(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != "1":
                return

            grid[i][j] = "0"
            dfs_recursive(i, j+1)
            dfs_recursive(i+1, j)
            dfs_recursive(i, j-1)
            dfs_recursive(i-1, j)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    num_island += 1
                    dfs_recursive(i, j)

        return num_island




