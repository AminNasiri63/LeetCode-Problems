# 39. Combinations Sum


from typing import List


# Time: O(2**(target / min(candidates))) - Space: O(n)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(i, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return

            if cur_sum > target or i == n:
                return

            backtrack(i+1, cur_sum)

            sol.append(candidates[i])
            backtrack(i, cur_sum+candidates[i])
            sol.pop()

        backtrack(0, 0)

        return res


# Method 2
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        n = len(candidates)

        def backtrack(start, cur_sum):
            if cur_sum == target:
                res.append(sol[:])
                return

            if cur_sum > target:
                return

            for i in range(start, n):
                sol.append(candidates[i])
                backtrack(i, cur_sum + candidates[i])
                sol.pop()

        backtrack(0, 0)
        return res
