# 2239. Find Closest Number to Zero


from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = nums[0]

        for num in nums:
            if abs(num) < abs(res):
                res = num
            elif abs(num) == abs(res):
                res = max(num, res)

        return res
