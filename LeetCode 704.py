
# 704. Binary Search

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        L, R = 0, N - 1

        while L <= R:
            M = L + (R - L) // 2

            if nums[M] == target:
                return M
            elif target < nums[M]:
                R = M - 1
            else:
                L = M + 1

        return -1



