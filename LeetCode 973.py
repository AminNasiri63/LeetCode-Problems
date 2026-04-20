# 973. K Closest Points to Origin


import heapq
from typing import List

# Min Heap - Time: O(nlog k) - Space: O(k)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return p[0] ** 2 + p[1] ** 2
        dis_heap = []

        for point in points:
            dis = dist(point)
            if len(dis_heap) < k:
                heapq.heappush(dis_heap, (-dis, point))
            else:
                heapq.heappushpop(dis_heap, (-dis, point))

        return [p for d, p in dis_heap]

