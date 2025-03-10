class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        val = 0
        count = 0

        for num in nums:

            if count == 0:
                val = num
            
            if num == val:
                count += 1
            else:
                count -= 1
        
        return val
        