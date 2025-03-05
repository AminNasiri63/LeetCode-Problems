class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        ir = 0
        iw = 0
        k = 0
        while ir < len(nums):
            if nums[ir] != val:
                nums[iw] = nums[ir]
                k += 1
                iw += 1
            ir += 1
        return k
        