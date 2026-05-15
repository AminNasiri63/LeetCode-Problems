# 417. Pacific Atlantic Water Flow

from collections import deque
from typing import List

# BFS Method
# Time Complexity: O(m*n) - Space Complexity: O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n  = len(heights), len(heights[0])
        off_set = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        p_que, p_seen = deque(), set()
        a_que, a_seen = deque(), set()

        for j in range(n):
            p_que.append((0, j))
            p_seen.add((0, j))

        for i in range(1, m):
            p_que.append((i, 0))
            p_seen.add((i, 0))

        for i in range(m):
            a_que.append((i, n-1))
            a_seen.add((i, n-1))

        for j in range(n-1):
            a_que.append((m-1, j))
            a_seen.add((m-1, j))

        def get_coord(que, seen):
            while que:
                i, j = que.popleft()

                for i_off, j_off in off_set:
                    r, c = i + i_off , j + j_off

                    if 0 <= r < m and 0 <= c < n and heights[r][c] >= heights[i][j]\
                        and (r, c) not in seen:
                        que.append((r, c))
                        seen.add((r, c))

        get_coord(p_que, p_seen)
        get_coord(a_que, a_seen)

        return list(p_seen.intersection(a_seen))

# DFS Method
# Time Complexity: O(m*n) - Space Complexity: O(m*n)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n  = len(heights), len(heights[0])
        off_set = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        p_seen, a_seen = set(), set()

        def dfs(i, j, seen):
            seen.add((i, j))

            for i_off, j_off in off_set:
                r, c = i + i_off, j + j_off

                if (
                    0 <= r < m and
                    0 <= c < n and
                    (r, c) not in seen and
                    heights[r][c] >= heights[i][j]
                ):
                    dfs(r, c, seen)

        for j in range(n):
            dfs(0, j, p_seen)
        for i in range(1, m):
            dfs(i, 0, p_seen)

        for i in range(m):
            dfs(i, n-1, a_seen)
        for j in range(n-1):
            dfs(m-1, j, a_seen)

        return list(p_seen.intersection(a_seen))