
# 78. Subsets

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        cur, res = [], []

        def backtrack(i):
            if i == n:
                res.append(cur[:])
                return

            backtrack(i+1)

            cur.append(nums[i])
            backtrack(i+1)
            cur.pop()

        backtrack(0)
        return res



