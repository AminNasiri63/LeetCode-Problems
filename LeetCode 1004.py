# 1004. Max Consecutive Ones III

from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        lp, zeros, longest = 0, 0, 0
        n = len(nums)

        for rp in range(n):

            if nums[rp] == 0:
                zeros += 1

            while zeros > k:
                if nums[lp] == 0:
                    zeros -= 1
                lp += 1

            w = rp - lp + 1
            longest = max(w, longest)

        return longest