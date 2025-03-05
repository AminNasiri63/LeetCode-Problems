class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lp = 0
        rp = len(nums) - 1
        res = []

        while lp <= rp:
            if abs(nums[rp]) >= abs(nums[lp]):
                res.append(nums[rp] ** 2)
                rp -= 1
            else:
                res.append(nums[lp] ** 2)
                lp += 1
        res.reverse()
        return res
            