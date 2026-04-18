# 215. Kth Largest Element in an Array


import heapq
from typing import List

# Max Heap - Time: O(n + k log n) - Space: O(1)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)

        for i in range(n):
            nums[i] = -nums[i]

        heapq.heapify(nums)

        for i in range(k):
            largest = heapq.heappop(nums)

        return -largest


# Min Heap - Time: O(nlog k) - Space: O(k)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            else:
                heapq.heappushpop(min_heap, num)

        return min_heap[0]