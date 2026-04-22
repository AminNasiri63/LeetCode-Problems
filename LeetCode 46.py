# 46. Permutations


from typing import List

# Time: O(n! * n) - Space: O(n! * n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n, sol, res = len(nums), [], []

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return

            for num in nums:
                if num not in sol:
                    sol.append(num)
                    backtrack()
                    sol.pop()

        backtrack()
        return res


