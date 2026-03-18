
# 1046. Last Stone Weight

import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        n = len(stones)
        for i in range(n):
            stones[i] = -stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            heaviest = heapq.heappop(stones)
            next_heaviest = heapq.heappop(stones)

            if heaviest != next_heaviest:
                heapq.heappush(stones, heaviest - next_heaviest)

        return -stones[0] if stones else 0


