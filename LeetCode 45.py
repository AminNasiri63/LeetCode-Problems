class Solution:
    def jump(self, nums: List[int]) -> int:

        nearInd, farInd, jump = 0, 0, 0

        while farInd < len(nums) - 1:
            farthestInd = 0
            for i in range(nearInd, farInd + 1):
                farthestInd = max(farthestInd, i + nums[i])
            
            nearInd = farInd + 1
            farInd = farthestInd
            jump += 1
        return jump