class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        def forward():
            answer = []
            f = 1
            for i in nums:
                answer.append(f)
                f *= i
            
            return answer

        def backward(answer):
            b = 1
            for i in range(len(nums) - 1, -1, -1):
                answer[i] *= b
                b *= nums[i]
            
            return answer

        answer = forward()
        return backward(answer)