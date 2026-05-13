# 210. Course Schedule

from collections import defaultdict
from typing import List

# Time Complexity: O(V+E) - Space Complexity: O(V+E)
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        g = defaultdict(list)
        for a, b in prerequisites:
            g[a].append(b)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        states = [UNVISITED] * numCourses
        order = []

        def dfs(node):
            state = states[node]
            if state == VISITED: return True
            if state == VISITING: return False

            states[node] = VISITING

            for nei in g[node]:
                if not dfs(nei):
                    return False

            states[node] = VISITED
            order.append(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order