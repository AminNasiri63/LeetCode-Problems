# 215. Kth Largest Element in an Array


import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for i in range(k):
            largest = heapq.heappop(nums)

        return -largest

