# 217. Contains Duplicate


from typing import List

# method 1
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        senn = set()

        for num in nums:
            if num in senn:
                return True
            senn.add(num)

        return False


# method 2
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)

        if len(nums) != len(nums_set):
            return True

        return False
