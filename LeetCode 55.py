class Solution:
    def canJump(self, nums: List[int]) -> bool:

        pointer = 0

        for num in nums:

            if pointer < 0:
                return False

            if num > pointer:
                pointer = num
            
            pointer -= 1
        
        return True
        