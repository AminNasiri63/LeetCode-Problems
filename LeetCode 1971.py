
# 1971. Find if Path Exists in Graph

from collections import defaultdict, deque
from typing import List

# recursive method
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)

        def dfs_recursive(node):
            if node == destination:
                return True

            for nei_node in graph[node]:
                if nei_node in seen:
                    continue

                seen.add(nei_node)
                if dfs_recursive(nei_node):
                    return True

            return False

        return dfs_recursive(source)


# stack method
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)
        stack = [source]

        while stack:
            node = stack.pop()

            if node == destination:
                return True

            for nei_node in graph[node]:
                if nei_node in seen:
                    continue

                seen.add(nei_node)
                stack.append(nei_node)

        return False


# queue method
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:

        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        seen = set()
        seen.add(source)
        q = deque()
        q.append(source)

        while q:
            node = q.popleft()

            if node == destination:
                return True

            for nei_node in graph[node]:
                if nei_node in seen:
                    continue

                seen.add(nei_node)
                q.append(nei_node)

        return False