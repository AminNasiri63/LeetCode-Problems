# 347. Top K Frequent Elements


import heapq
from typing import Counter, List

# Min Heap - Time: O(nlog k) - Space: O(k)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        counter_heap = []

        for key, val in counter.items():
            if len(counter_heap) < k:
                heapq.heappush(counter_heap, (val, key))
            else:
                heapq.heappushpop(counter_heap, (val, key))

        return [i[1] for i in counter_heap]


# Method2 - Time: O(n) - Space: O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        counter = Counter(nums)
        buckets = [0] * (n + 1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)

        result = []
        for i in range(n, -1, -1):
            if buckets[i] != 0:
                result.extend(buckets[i])
            if len(result) == k:
                break

        return result
