
# 643. Maximum Average Subarray I

from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        win_sum = 0

        for i in range(k):
            win_sum += nums[i]

        win_ave = win_sum / k

        for i in range(k, n):
            win_sum += nums[i]
            win_sum -= nums[i-k]

            win_ave = max(win_ave, win_sum/k)

        return win_ave



