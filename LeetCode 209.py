# 209. Minimum Size Subarray Sum


from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = float('inf')
        lp = 0
        summ = 0
        n = len(nums)

        for rp in range(n):
            summ += nums[rp]

            while summ >= target:
                min_length = min(min_length, rp-lp+1)
                summ -= nums[lp]
                lp += 1

        return min_length if min_length < float('inf') else 0


